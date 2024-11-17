from .types import Collection
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
from lyra.downloader import download_data
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

    @Collection.wrapper
    def download(cls, {parameters}): UNREACHABLE()
    
    @classmethod
    def __download__(cls, {parameters}):
{body}
"""

base_quote = base_quote.strip()

def make_collection(name: str, parameters: list[Parameter]):
    _parameters = ', '.join(str(x) for x in parameters)
    
    body = []
    for p in parameters:
        varname = p.name
        valid_values = p.valid_values

        if not valid_values:
            continue

        valid_values = repr(valid_values)

        body += [
            f'{varname}_valid_values = {valid_values}',
            f'assert {varname} in {varname}_valid_values\n',
        ]


    body.append('return download_data(' + ', '.join(f'{p.name}={p.name}' 
                                                    for p in parameters) + ')')
    body = '\n'.join('        ' + x for x in body)
    body += '\n'

    kw_parameters = set(str(p.name) for p in parameters)
    kw_parameters = ', '.join(str(f'{s}={s}') for s in kw_parameters)
    base = base_quote.format(
        name=name, 
        parameters=_parameters,
        kw_parameters=kw_parameters,
        body=body)

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
        mappings.append(_name)
    
    mappings = '\n'.join(mappings)
    return mapping_quote.format(mappings=mappings)