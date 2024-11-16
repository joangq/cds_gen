import sys
import importlib.util

spec = importlib.util.spec_from_file_location("lyra", "src/lyra/__init__.py")
lyra = importlib.util.module_from_spec(spec)
sys.modules["lyra"] = lyra
spec.loader.exec_module(lyra)

Parameter = lyra.Parameter

from unittest import TestCase, main

"""
Parameter(foo, int, None, True) -> "foo: int"
Parameter(bar, str, None, False) -> "bar: Optional[str] = None"
Parameter(baz, "Any", {2: True}, True) -> "baz: Any = {2: True}"
"""

class TestParameter(TestCase):
    def test_a(self):
        self.assertEqual(str(Parameter("foo", int, None, True)), "foo: int")
    
    def test_b(self):
        self.assertEqual(str(Parameter("bar", str, None, False)), "bar: Optional[str] = None")

    def test_c(self):
        self.assertEqual(str(Parameter("baz", "Any", {2: True}, True)), "baz: Any = {2: True}")


if __name__ == '__main__':
    main()