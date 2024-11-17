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

class Collection_sis_heat_and_cold_spells(Collection):
    collection_name = 'sis-heat-and-cold-spells'
    valid_values = dict(
        definition = ['climatological_related', 'health_related', 'country_related'],
        ensemble_statistic = ['ensemble_members_average', 'ensemble_members_standard_deviation'],
        experiment = ['rcp4_5', 'rcp8_5'],
        variable = ['heat_wave_days', 'cold_spell_days'],
    )

    @Collection.wrapper
    def download(cls, definition: str, ensemble_statistic: OneOrMore[str], experiment: OneOrMore[str], variable: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param definition:
        :type definition: str

        **Valid values:**
        
        - climatological_related

        
        - health_related

        
        - country_related

        ---

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
        
        - heat_wave_days

        
        - cold_spell_days

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_heat_and_cold_spells(definition: str, ensemble_statistic: OneOrMore[str], experiment: OneOrMore[str], variable: OneOrMore[str]):
    return Collection_sis_heat_and_cold_spells.download(definition=definition, ensemble_statistic=ensemble_statistic, experiment=experiment, variable=variable)

