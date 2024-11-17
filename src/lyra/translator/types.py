from typing import Any, Dict
from abc import ABC as AbstractBaseClass, abstractmethod
from lyra.common import MISSING_IMPLEMENTATION
from functools import wraps
from lyra.downloader import download_data
from inspect import signature
from warnings import warn
from lyra.common import OneOrMore
from collections.abc import Iterable

class BaseCollection(AbstractBaseClass):
    collection_name: str
    valid_values: Dict[str, Any] = {}

    @classmethod
    def wrapper(cls, f):

        sig = signature(f)
        default_values = {k: v.default for k,v in sig.parameters.items() if v.default != v.empty}
        type_of = {k: v.annotation for k,v in sig.parameters.items() if v.annotation != v.empty}
        cls.types = type_of

        @classmethod
        @wraps(f)
        def download(cls, **kwargs) -> None:
            new_kwargs = default_values | kwargs

            for k,v in new_kwargs.items():
                t = type_of[k]

                if t != OneOrMore and (hasattr(t, 'mro') and t.mro()[0] != OneOrMore):
                    continue

                if not isinstance(v, (list, tuple, set, frozenset, dict)):
                    new_kwargs[k] = [v]

            return cls.__download__(
                **new_kwargs
            )
        
        return download
        
    
    @classmethod
    @abstractmethod
    def __download__(cls, **kwargs) -> None:
        MISSING_IMPLEMENTATION()

class Collection(BaseCollection):
    @classmethod
    def __download__(cls, **kwargs):
        for k,v in kwargs.items():
            if k not in cls.valid_values:
                # warn(f"Invalid parameter '{k}'")
                continue
            
            t = cls.types[k]
            is_one_or_more = t == OneOrMore or (hasattr(t, 'mro') and t.mro()[0] == OneOrMore)
            if is_one_or_more:
                assert isinstance(v, Iterable), f"Invalid value for '{k}': {v}, expected an iterable"
                assert all(x in cls.valid_values[k] for x in v), f"Invalid value for '{k}': {v}, expected one of {', '.join(cls.valid_values[k])}"
            else:
                assert v in cls.valid_values[k], f"Invalid value for '{k}': {v}, expected one of {', '.join(cls.valid_values[k])}"
        return download_data(collection_name=cls.collection_name, **kwargs)