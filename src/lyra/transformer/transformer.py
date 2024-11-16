from dataclasses import dataclass
import lyra.parser
from lyra.common import MISSING_IMPLEMENTATION, TODO
from abc import ABC as AbstractBaseClass, abstractmethod
from typing import Generic, TypeVar, Optional, Any, cast
from lyra.parser import (
    BaseParamType,
    ParamType,
    Object,
)

T = TypeVar('T') # Tipo del objeto a transformar
P = TypeVar('P') # Tipo del parámetro devuelto

STRING_PARAM_TYPES = {
    lyra.parser.StringChoiceWidget,
    lyra.parser.StringListArrayWidget,
    lyra.parser.StringListWidget
}

class Transformer(AbstractBaseClass, Generic[T, P]):
    @classmethod
    @abstractmethod
    def transform(cls, obj: T) -> P:
        MISSING_IMPLEMENTATION()

@dataclass
class Parameter:
    name: str
    innertype: type | str
    default: any
    required: bool

    def __str__(self):
        if isinstance(self.innertype, type):
            innertype_str = self.innertype.__name__
        else:
            innertype_str = self.innertype

        if self.default is None and not self.required:
            innertype_str = f"Optional[{innertype_str}]"

        if (self.default is not None 
            or (self.default is None and not self.required)):
            default_str = f" = {repr(self.default)}"
        else:
            default_str = ""

        return f"{self.name}: {innertype_str}{default_str}"
    

global AVAILABLE_TRANSFORMERS
AVAILABLE_TRANSFORMERS = dict()

class ParamTypeTransformer(Transformer[ParamType, Parameter]):
    def __init_subclass__(cls):
        AVAILABLE_TRANSFORMERS[cls.__name__] = cls
        return super().__init_subclass__()
    

MISSING_TRANSFORMER_DATACLASS_OPTIONS = dict(
      init        = True
    , repr        = True
    , eq          = True
    , order       = False
    , unsafe_hash = True
    , frozen      = False
    , match_args  = True
    , kw_only     = False
    , slots       = False
)

@dataclass(**MISSING_TRANSFORMER_DATACLASS_OPTIONS)
class MissingTransformer:
    transformer_name: str
    data: Optional[Any] = None

def transform_form(form: list[ParamType]) -> list[MissingTransformer | Parameter]:
    return [
        (MissingTransformer(t, data=x)
         if not transformer 
         else 
            str(transformer.transform(x)) # DEBUG ONLY. REMOVE LATER.
         )

        for x in form
        for t in (type(x).__name__ + 'Transformer', )
        for transformer in (AVAILABLE_TRANSFORMERS.get(t, None), ) # alias

        # type annotation
        for transformer in 
            (cast(ParamTypeTransformer, transformer), )
    ]

class StringListWidgetTransformer(ParamTypeTransformer):
    @classmethod
    def transform(cls, obj: ParamType) -> Parameter:
        assert isinstance(obj, lyra.parser.StringListWidget)
        return Parameter(
            name = obj.name,
            innertype = str,
            default = None,
            required = obj.required
        )