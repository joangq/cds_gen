from __future__ import annotations
from typing import List
from dataclasses import dataclass
from abc import ABC as AbstractBaseClass, abstractmethod
from typing import Generic, TypeVar, Any, Tuple, Optional, Dict
import json
from lyra.common import MISSING_IMPLEMENTATION, TODO
from lyra.enum import StrEnum

I = TypeVar('I')
O = TypeVar('O')
T = TypeVar('T')

def is_path(x: str) -> bool: ...

def is_valid_object(x: dict) -> bool:
    return (
        isinstance(x, dict)
        # TODO: Add checks
    )

def parse(form: str | List):
    if not isinstance(form, str):
        return parse_form(form)

    if not is_path(form):
        return parse_form(json.loads(form))

    with open(form) as f:
        return parse_form(json.load(f))
    
global AVAILABLE_PARSERS
AVAILABLE_PARSERS = dict()

MISSING_PARSER_DATACLASS_OPTIONS = dict(
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

@dataclass(**MISSING_PARSER_DATACLASS_OPTIONS)
class MissingParser:
    parser_name: str
    data: Optional[Any] = None

def parse_form(form: List) -> List[MissingParser | ParamType]:
    assert isinstance(form, list)
    assert all(is_valid_object(x) for x in form)
    return [
        (MissingParser(t, data=x)
         if not parser 
         else parser.parse(x))

        for x in form
        for t in (x['type'], ) # alias
        for parser in (AVAILABLE_PARSERS.get(t, None), ) # alias
    ]

class Parser(AbstractBaseClass, Generic[I, O]):
    @classmethod
    @abstractmethod
    def parse(cls, x: I) -> O:
        MISSING_IMPLEMENTATION()

    @classmethod
    @abstractmethod
    def __parse__(cls, *args, **kwargs) -> O:
        MISSING_IMPLEMENTATION()
    
    def __init_subclass__(cls):
        global AVAILABLE_PARSERS
        AVAILABLE_PARSERS[cls.__name__] = cls
        return super().__init_subclass__()

parser_object_dataclass_options = dict(
      init        = True
    , repr        = False
    , eq          = True
    , order       = False
    , unsafe_hash = False
    , frozen      = False
    , match_args  = True
    , kw_only     = False
    , slots       = False
)

class Object(AbstractBaseClass):
    def __init_subclass__(cls):
        global parser_object_dataclass_options
        result = dataclass(cls, **parser_object_dataclass_options)
        
        def __repr__(self):
            class_name = type(self).__name__
            indented_fields = ', '.join(
                f'{k}={v!r}'
                for k, v in vars(self).items()
            )
            return f'{class_name}({indented_fields})'
        
        result.__repr__ = __repr__
        return result

class ParamType(Parser[dict, Object], Object):
    label: str

    @staticmethod
    def __base_parse__(item: dict) -> dict:
        MISSING_IMPLEMENTATION()
    
    @classmethod
    def parse(cls, x: dict) -> Object:
        if not 'type' in x:
            return cls.__parse__(**cls.__base_parse__(x))

        kind = x['type']
        if not kind == cls.__name__:
            raise ValueError(f"Expected type '{kind}', got '{cls.__name__}'")
        
        return cls.__parse__(**cls.__base_parse__(x))

class BaseParamType(ParamType):
    name: str
    required: bool

    @staticmethod
    def __base_parse__(item: dict) -> Tuple[Optional[str], Optional[str], Dict]:
        return dict(
              name     = item.get('name')
            , label    = item['label']
            , kind     = item.get('type')
            , details  = item.get('details', {})
            , required = item.get('required', False)
        )

class Option(Object, Generic[T]):
    value: T
    label: str

class StringListWidget(BaseParamType):
    options: List[Option]

    @classmethod
    def __parse__(
        cls, 
        name     : Optional[str], 
        label    : str, 
        kind     : Optional[str], 
        required : bool,
        details  : Dict) -> Object:
        
        values = details.get('values', [])
        labels = details.get('labels', [])
        options = [
            Option(val, labels.get(val, val))
            for val in values
        ]

        return cls(name=name, label=label, options=options, required=required)

class StringChoiceWidget(StringListWidget): ...

class Group(ParamType):
    label: str
    options: List[Option]

    @staticmethod
    def __base_parse__(group: dict) -> Tuple[str, List[Option]]:
        return dict(
            label  = group.get('label', 'Unknown Group'),
            values = group.get('values', []),
            labels = group.get('labels', {}),
        )
    
    @classmethod
    def __parse__(cls, label: str, values: List, labels: Dict) -> Object:
        options = [
            Option(val, labels.get(val, val))
            for val in values
        ]

        return cls(label=label, options=options)

class StringListArrayWidget(BaseParamType):
    groups: List[Group]

    @classmethod
    def __parse__(
        cls, 
        name     : Optional[str], 
        label    : str, 
        kind     : Optional[str], 
        required : bool,
        details  : Dict) -> Object:

        groups = details.get('groups', [])

        return cls(
            name   = name, 
            label  = label, 
            groups = [Group.parse(group) for group in groups],
            required = required
        )

class MISSING_VALUE(object): ...

class ExclusiveGroupWidget(ParamType, Generic[T]):
    __MISSING_VALUE__ = MISSING_VALUE()
    children: List[T]
    name: str
    default: Optional[T] = __MISSING_VALUE__

    @staticmethod
    def __base_parse__(item: dict) -> dict:
        return dict(
            name     = item.get('name'),
            label    = item['label'],
            kind     = item.get('type'),
            details  = item.get('details', {}),
            children = item.get('children', []),
        )

    @classmethod
    def __parse__(
        cls,
        name     : Optional[str],
        label    : str,
        children : List[T],
        kind     : Optional[str],
        details  : Dict) -> Object:

        default = details.get('default', cls.__MISSING_VALUE__)
        return cls(name=name, label=label, children=children, default=default)

number = TypeVar('number', int, float)

# GEOGRAPHIC_EXTENT_LABELS = dict(
class GeographicExtentLabel(StrEnum):
    n = 'North'
    w = 'West'
    s = 'South'
    e = 'East'

# INVERSE_GEOGRAPHIC_EXTENT_LABELS = {
#     v: k
#     for k, v in GEOGRAPHIC_EXTENT_LABELS.items()
# }

INVERSE_GEOGRAPHIC_EXTENT_LABELS = {
    label.value: label.name
    for label in GeographicExtentLabel
}

class GeographicExtentWidget(BaseParamType):
    precision: number
    range: Dict[GeographicExtentLabel, number]

    @classmethod
    def __parse__(
        cls, 
        name     : Optional[str], 
        label    : str, 
        kind     : Optional[str], 
        required : bool,
        details  : Dict) -> Object:

        precision = details.get('precision', 2)
        default_range = details.get('default', {})
        range = details.get('range', default_range)
        return cls(
              name      = name
            , label     = label
            , precision = precision
            , range     = range
            , required  = required
        )

class License(Object):
    id: str
    label: str
    contents_url: str
    attachment_url: str
    revision: Optional[int]

class LicenceWidget(BaseParamType): # [sic]
    licences: List[License]

    @classmethod
    def __parse__(
        cls, 
        name     : Optional[str], 
        label    : str, 
        kind     : Optional[str], 
        required : bool,
        details  : Dict) -> Object:

        licences = details.get('licences', [])
        licenses = [License(**license) for license in licences]

        return cls(
                name      = name
            ,   label     = label
            ,   licences  = licences
            ,   required  = required
        )
    
class ExclusiveFrameWidget(ParamType):
    widgets: List[str]
    required: bool
    id: Optional[int] = None
    
    @staticmethod
    def __base_parse__(item: dict) -> dict:
        return dict(
              id       = item.get('id')
            , label    = item['label']
            , kind     = item.get('type')
            , details  = item.get('details', {})
            , widgets  = item.get('widgets', [])
            , required = item.get('required', False)
        )
    
    @classmethod
    def __parse__(
        cls, 
        id       : Optional[int], 
        label    : str, 
        kind     : Optional[str], 
        details  : Dict, 
        required : bool,
        widgets  : List[str]) -> Object:

        id = details.get('id', None)
        
        return cls(id=id, label=label, widgets=widgets, required=required)
    
class GeographicExtentMapWidget(BaseParamType):
    range: Dict[GeographicExtentLabel, number]
    default: List[number]
    precision: number
    fullheight: bool
    wrapping: bool

    @classmethod
    def __parse__(
        cls, 
        name     : Optional[str], 
        label    : str, 
        kind     : Optional[str], 
        required : bool,
        details  : Dict) -> Object:

        precision     = details.get('precision', 2)
        default_range = details.get('default', {})
        range         = details.get('range', default_range)
        fullheight    = details.get('fullheight', False)
        wrapping      = details.get('wrapping', False)

        return cls(
              name       = name
            , label      = label
            , default    = default_range
            , precision  = precision
            , range      = range
            , fullheight = fullheight
            , wrapping   = wrapping
            , required   = required
        )
    

class LabelWidget(BaseParamType):
    accordion: bool
    information: str

    @classmethod
    def __parse__(
        cls, 
        name     : Optional[str], 
        label    : str, 
        kind     : Optional[str], 
        required : bool,
        details  : Dict) -> Object:

        information = details.get('information', '')
        accordion   = details.get('accordion', False)

        return cls(
              name        = name
            , label       = label
            , information = information
            , accordion   = accordion
            , required    = required
        )
    
class FreeEditionWidget(LabelWidget): ...

__all__ = [
          'parse'
        , 'Parser'
        , 'Object'
        , 'ParamType'
        , 'BaseParamType'
        , 'Option'
        , 'StringListWidget'
        , 'StringChoiceWidget'
        , 'Group'
        , 'StringListArrayWidget'
        , 'ExclusiveGroupWidget'
        , 'number'
        , 'GeographicExtentLabel'
        , 'INVERSE_GEOGRAPHIC_EXTENT_LABELS'
        , 'GeographicExtentWidget'
        , 'License'
        , 'LicenceWidget'
        , 'ExclusiveFrameWidget'
        , 'GeographicExtentMapWidget'
        , 'LabelWidget'
        , 'FreeEditionWidget'
        , 'MISSING_VALUE'
]