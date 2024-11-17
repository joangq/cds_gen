from .types import BaseCollection
from lyra.transformer import Parameter

imports = \
"""
from lyra.translator import Collection
from lyra.common import OneOrMore
from lyra.common import GeographicExtentType
from lyra.common import GeographicExtentMapType
from lyra.common import LabelType
from lyra.common import FreeEditionType
from lyra.common import UNREACHABLE
from typing import Union, Optional

\"\"\"
This code has been automatically generated
by Lyra. Specifically, the format for
this code can be found in

`lyra.translator.translate`
\"\"\"
"""

imports = imports.strip() + '\n\n'

base_quote = \
"""
class Collection_{name}(Collection):
    collection_name = {cname}
    valid_values = dict(
        {valid_values_params}
    )

    @Collection.wrapper
    def download(cls, {parameters}): 
        \"\"\"
        {docstring}
        \"\"\"
        UNREACHABLE()

def download_{name}({parameters}):
    return Collection_{name}.download({kw})
"""

# """
# def download_{name}({parameters}):
#     return Collection_{name}.download({kw})
# """

base_quote = base_quote.strip() + '\n\n'

def make_collection(name: str, parameters: list[Parameter], normalizer=lambda x: x):
    _parameters = ', '.join(str(x) for x in parameters)
    kw = ', '.join(f'{p.name}={p.name}' for p in parameters)
    dict_items = '\n        '.join(f'{p.name} = {p.valid_values},' for p in parameters if hasattr(p, 'valid_values') and p.valid_values)

    docstring = [f'Parameters', '----------']
    for p in parameters:
        docstring += [f':param {p.name}:']
        docstring += [f':type {p.name}: str\n']
        # valid values
        if hasattr(p, 'valid_values') and p.valid_values:
            docstring.append("**Valid values:**")
            valid_values = ['\n        - ' + p_vv + '\n' for p_vv in p.valid_values]
            docstring += valid_values
        docstring.append('---\n')
    docstring += [f'Returns', '-------']
    docstring += [f':return: The data requested']
    docstring += [f':rtype: Any']
    docstring = '\n        '.join(docstring)

    base = base_quote.format(
        docstring=docstring,
        kw=kw,
        valid_values_params=dict_items,
        name=normalizer(name),
        cname=repr(name),
        parameters=_parameters)

    return base


mapping_quote = \
"""
cds_collections = {{
{mappings}
}}
"""

mapping_quote = mapping_quote.strip()

def make_mapping(names: list[str], prefix = 'Collection_', normalizer = lambda x: x):
    mappings = []
    for name in names:
        _name = f'    "{name}": \\\n\t{prefix}{normalizer(name)},\n'
        #_name = f'    "{name}": \\\n\tdownload_{normalizer(name)},\n'
        mappings.append(_name)
    
    mappings = '\n'.join(mappings)
    return mapping_quote.format(mappings=mappings)


def make___all__(names: list[str], prefix = 'Collection_', normalizer = lambda x: x, extra = []):
    _list = [f'"{prefix}{normalizer(name)}"' for name in names] + list(map(repr, extra))
    _names = ', \n'.join(_list)
    return f'__all__ = [{_names}]'