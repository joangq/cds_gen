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

class Collection_sis_health_vector(Collection):
    collection_name = 'sis-health-vector'
    valid_values = dict(
        ensemble_statistic = ['ensemble_members_average', 'ensemble_members_standard_deviation'],
        experiment = ['rcp4_5', 'rcp8_5'],
        variable = ['suitability', 'season_length'],
    )

    @Collection.wrapper
    def download(cls, ensemble_statistic: OneOrMore[str], experiment: OneOrMore[str], variable: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param ensemble_statistic:
        :type ensemble_statistic: str

        **Valid values:**
        
        - ensemble_members_average

        
        - ensemble_members_standard_deviation

        ---

        :param experiment:
        :type experiment: str

        **Valid values:**
        
        - rcp4_5

        
        - rcp8_5

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - suitability

        
        - season_length

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_health_vector(ensemble_statistic: OneOrMore[str], experiment: OneOrMore[str], variable: OneOrMore[str]):
    return Collection_sis_health_vector.download(ensemble_statistic=ensemble_statistic, experiment=experiment, variable=variable)

