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

class Collection_satellite_ice_sheet_elevation_change(Collection):
    collection_name = 'satellite-ice-sheet-elevation-change'
    valid_values = dict(
        climate_data_record_type = ['icdr', 'tcdr'],
        domain = ['antarctica', 'greenland'],
        version = ['2_0', '3_0', '4_0', '5_0'],
        variable = ['all'],
    )

    @Collection.wrapper
    def download(cls, climate_data_record_type: OneOrMore[str], domain: OneOrMore[str], version: OneOrMore[str], variable: str = 'all'): 
        """
        Parameters
        ----------
        :param climate_data_record_type:
        :type climate_data_record_type: str

        **Valid values:**
        
        - icdr

        
        - tcdr

        ---

        :param domain:
        :type domain: str

        **Valid values:**
        
        - antarctica

        
        - greenland

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - 2_0

        
        - 3_0

        
        - 4_0

        
        - 5_0

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

def download_satellite_ice_sheet_elevation_change(climate_data_record_type: OneOrMore[str], domain: OneOrMore[str], version: OneOrMore[str], variable: str = 'all'):
    return Collection_satellite_ice_sheet_elevation_change.download(climate_data_record_type=climate_data_record_type, domain=domain, version=version, variable=variable)

