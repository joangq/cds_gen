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

class Collection_satellite_greenland_ice_sheet_velocity(Collection):
    collection_name = 'satellite-greenland-ice-sheet-velocity'
    valid_values = dict(
        period = ['2017_2018', '2018_2019', '2019_2020', '2020_2021'],
        version = ['1_2', '1_3', '1_4'],
        variable = ['all'],
    )

    @Collection.wrapper
    def download(cls, period: OneOrMore[str], version: OneOrMore[str], variable: str = 'all'): 
        """
        Parameters
        ----------
        :param period:
        :type period: str

        **Valid values:**
        
        - 2017_2018

        
        - 2018_2019

        
        - 2019_2020

        
        - 2020_2021

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - 1_2

        
        - 1_3

        
        - 1_4

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - all

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_satellite_greenland_ice_sheet_velocity(period: OneOrMore[str], version: OneOrMore[str], variable: str = 'all'):
    return Collection_satellite_greenland_ice_sheet_velocity.download(period=period, version=version, variable=variable)

