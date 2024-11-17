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

class Collection_satellite_ice_sheet_mass_balance(Collection):
    collection_name = 'satellite-ice-sheet-mass-balance'
    valid_values = dict(
        variable = ['all'],
    )

    @Collection.wrapper
    def download(cls, variable: str = 'all'): 
        """
        Parameters
        ----------
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

def download_satellite_ice_sheet_mass_balance(variable: str = 'all'):
    return Collection_satellite_ice_sheet_mass_balance.download(variable=variable)

