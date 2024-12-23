from typing import Generic, TypeVar

T = TypeVar('T')

def TODO() -> None:
    raise NotImplementedError("TODO")

def MISSING_IMPLEMENTATION() -> None:
    raise NotImplementedError("This method is not implemented")

def UNREACHABLE() -> None:
    raise Exception("This should not have been reached")

class OneOrMore(Generic[T]): ...

class GeographicExtentType: ...
class FreeEditionType: ...
class GeographicExtentMapType: ...
class LabelType: ...