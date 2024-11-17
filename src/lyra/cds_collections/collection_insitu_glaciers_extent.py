from lyra.translator import Collection
from lyra.common import OneOrMore
from lyra.common import GeographicExtentType
from lyra.common import GeographicExtentMapType
from lyra.common import LabelType
from lyra.common import FreeEditionType
from lyra.common import UNREACHABLE
from typing import Union, Optional

"""
This code has been automatically generated
by Lyra. Specifically, the format for
this code can be found in

`lyra.translator.translate`
"""

class Collection_insitu_glaciers_extent(Collection):
    collection_name = 'insitu-glaciers-extent'
    valid_values = dict(
        product_type = ['gridded', 'vector', 'hypsometry'],
        variable = ['glacier_area'],
        version = ['rgi_5_0', 'rgi_6_0', 'rgi_7_0'],
    )

    @Collection.wrapper
    def download(cls, product_type: OneOrMore[str], variable: OneOrMore[str], version: str = '7'): 
        """
        Parameters
        ----------
        :param product_type:
        :type product_type: str

        **Valid values:**
        
        - gridded

        
        - vector

        
        - hypsometry

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - glacier_area

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - rgi_5_0

        
        - rgi_6_0

        
        - rgi_7_0

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_insitu_glaciers_extent(product_type: OneOrMore[str], variable: OneOrMore[str], version: str = '7'):
    return Collection_insitu_glaciers_extent.download(product_type=product_type, variable=variable, version=version)

