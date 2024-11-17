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

class Collection_insitu_gridded_observations_alpine_precipitation(Collection):
    collection_name = 'insitu-gridded-observations-alpine-precipitation'
    valid_values = dict(
        dataset_issue = ['laprec1871', 'laprec1901'],
        variable = ['precipitation'],
        version = ['1_1', '1_2'],
    )

    @Collection.wrapper
    def download(cls, dataset_issue: OneOrMore[str], variable: str = 'precipitation', version: OneOrMore[str] = '1.2'): 
        """
        Parameters
        ----------
        :param dataset_issue:
        :type dataset_issue: str

        **Valid values:**
        
        - laprec1871

        
        - laprec1901

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - precipitation

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - 1_1

        
        - 1_2

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_insitu_gridded_observations_alpine_precipitation(dataset_issue: OneOrMore[str], variable: str = 'precipitation', version: OneOrMore[str] = '1.2'):
    return Collection_insitu_gridded_observations_alpine_precipitation.download(dataset_issue=dataset_issue, variable=variable, version=version)

