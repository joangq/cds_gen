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

class Collection_sis_temperature_statistics(Collection):
    collection_name = 'sis-temperature-statistics'
    valid_values = dict(
        ensemble_statistic = ['ensemble_members_average', 'ensemble_members_standard_deviation'],
        experiment = ['rcp4_5', 'rcp8_5'],
        period = ['summer', 'winter', 'year'],
        statistic = ['time_average', '1st_percentile', '5th_percentile', '10th_percentile', '25th_percentile', '50th_percentile', '75th_percentile', '90th_percentile', '95th_percentile', '97th_percentile', '99th_percentile'],
        variable = ['maximum_temperature', 'minimum_temperature', 'average_temperature'],
    )

    @Collection.wrapper
    def download(cls, ensemble_statistic: OneOrMore[str], experiment: OneOrMore[str], period: str, statistic: OneOrMore[str], variable: str): 
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

        :param period:
        :type period: str

        **Valid values:**
        
        - summer

        
        - winter

        
        - year

        ---

        :param statistic:
        :type statistic: str

        **Valid values:**
        
        - time_average

        
        - 1st_percentile

        
        - 5th_percentile

        
        - 10th_percentile

        
        - 25th_percentile

        
        - 50th_percentile

        
        - 75th_percentile

        
        - 90th_percentile

        
        - 95th_percentile

        
        - 97th_percentile

        
        - 99th_percentile

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - maximum_temperature

        
        - minimum_temperature

        
        - average_temperature

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_temperature_statistics(ensemble_statistic: OneOrMore[str], experiment: OneOrMore[str], period: str, statistic: OneOrMore[str], variable: str):
    return Collection_sis_temperature_statistics.download(ensemble_statistic=ensemble_statistic, experiment=experiment, period=period, statistic=statistic, variable=variable)

