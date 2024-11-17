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

class Collection_sis_ocean_wave_indicators(Collection):
    collection_name = 'sis-ocean-wave-indicators'
    valid_values = dict(
        experiment = ['historical', 'era5_reanalysis', 'rcp4_5', 'rcp8_5'],
        period = ['1976_2005', '2001_2017', '2041_2070', '2071_2100'],
        statistic = ['90th_percentile', '90th_100th_percentile_average', '95th_percentile', '99th_percentile', '100_year_return_period'],
        variable = ['peak_wave_period', 'significant_wave_height'],
    )

    @Collection.wrapper
    def download(cls, experiment: str, period: OneOrMore[str], statistic: OneOrMore[str], variable: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param experiment:
        :type experiment: str

        **Valid values:**
        
        - historical

        
        - era5_reanalysis

        
        - rcp4_5

        
        - rcp8_5

        ---

        :param period:
        :type period: str

        **Valid values:**
        
        - 1976_2005

        
        - 2001_2017

        
        - 2041_2070

        
        - 2071_2100

        ---

        :param statistic:
        :type statistic: str

        **Valid values:**
        
        - 90th_percentile

        
        - 90th_100th_percentile_average

        
        - 95th_percentile

        
        - 99th_percentile

        
        - 100_year_return_period

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - peak_wave_period

        
        - significant_wave_height

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_ocean_wave_indicators(experiment: str, period: OneOrMore[str], statistic: OneOrMore[str], variable: OneOrMore[str]):
    return Collection_sis_ocean_wave_indicators.download(experiment=experiment, period=period, statistic=statistic, variable=variable)

