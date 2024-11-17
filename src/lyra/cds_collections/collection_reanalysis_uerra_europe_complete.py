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

class Collection_reanalysis_uerra_europe_complete(Collection):
    collection_name = 'reanalysis-uerra-europe-complete'
    valid_values = dict(
        
    )

    @Collection.wrapper
    def download(cls, download_instructions: Optional[str] = None): 
        """
        Parameters
        ----------
        :param download_instructions:
        :type download_instructions: str

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_reanalysis_uerra_europe_complete(download_instructions: Optional[str] = None):
    return Collection_reanalysis_uerra_europe_complete.download(download_instructions=download_instructions)

