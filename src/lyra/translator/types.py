from typing import Any, Dict
from abc import ABC as AbstractBaseClass, abstractmethod
from lyra.common import MISSING_IMPLEMENTATION
from functools import wraps

class Collection(AbstractBaseClass):
    valid_values: Dict[str, Any] = {}

    @classmethod
    def wrapper(cls, f):

        @classmethod
        @wraps(f)
        def download(cls, **kwargs) -> None:
            return cls.__download__(
                **kwargs
            )
        
        return download
        
    
    @classmethod
    @abstractmethod
    def __download__(cls, **kwargs) -> None:
        MISSING_IMPLEMENTATION()

