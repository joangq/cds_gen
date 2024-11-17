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

class Collection_sis_agroclimatic_indicators(Collection):
    collection_name = 'sis-agroclimatic-indicators'
    valid_values = dict(
        experiment = ['historical', 'rcp2_6', 'rcp4_5', 'rcp6_0', 'rcp8_5'],
        origin = ['miroc_esm_chem_model', 'ipsl_cm5a_lr_model', 'noresm1_m_model', 'hadgem2_es_model', 'gfdl_esm2m_model', 'era_interim_reanalysis'],
        period = ['195101_198012', '198101_201012', '201101_204012', '204101_207012', '207101_209912'],
        temporal_aggregation = ['10_day', 'season', 'annual'],
        variable = ['biologically_effective_degree_days', 'growing_season_length', 'maximum_number_of_consecutive_dry_days', 'maximum_number_of_consecutive_frost_days', 'cold_spell_duration_index', 'maximum_number_of_consecutive_summer_days', 'maximum_number_of_consecutive_wet_days', 'mean_of_diurnal_temperature_range', 'frost_days', 'ice_days', 'heavy_precipitation_days', 'very_heavy_precipitation_days', 'precipitation_sum', 'wet_days', 'simple_daily_intensity_index', 'summer_days', 'mean_of_daily_mean_temperature', 'mean_of_daily_minimum_temperature', 'minimum_of_daily_minimum_temperature', 'maximum_of_daily_minimum_temperature', 'tropical_nights', 'mean_of_daily_maximum_temperature', 'minimum_of_daily_maximum_temperature', 'maximum_of_daily_maximum_temperature', 'warm_spell_duration_index', 'warm_and_wet_days'],
        version = ['1_0', '1_1'],
    )

    @Collection.wrapper
    def download(cls, experiment: str, origin: str, period: OneOrMore[str], temporal_aggregation: str, variable: OneOrMore[str], version: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param experiment:
        :type experiment: str

        **Valid values:**
        
        - historical

        
        - rcp2_6

        
        - rcp4_5

        
        - rcp6_0

        
        - rcp8_5

        ---

        :param origin:
        :type origin: str

        **Valid values:**
        
        - miroc_esm_chem_model

        
        - ipsl_cm5a_lr_model

        
        - noresm1_m_model

        
        - hadgem2_es_model

        
        - gfdl_esm2m_model

        
        - era_interim_reanalysis

        ---

        :param period:
        :type period: str

        **Valid values:**
        
        - 195101_198012

        
        - 198101_201012

        
        - 201101_204012

        
        - 204101_207012

        
        - 207101_209912

        ---

        :param temporal_aggregation:
        :type temporal_aggregation: str

        **Valid values:**
        
        - 10_day

        
        - season

        
        - annual

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - biologically_effective_degree_days

        
        - growing_season_length

        
        - maximum_number_of_consecutive_dry_days

        
        - maximum_number_of_consecutive_frost_days

        
        - cold_spell_duration_index

        
        - maximum_number_of_consecutive_summer_days

        
        - maximum_number_of_consecutive_wet_days

        
        - mean_of_diurnal_temperature_range

        
        - frost_days

        
        - ice_days

        
        - heavy_precipitation_days

        
        - very_heavy_precipitation_days

        
        - precipitation_sum

        
        - wet_days

        
        - simple_daily_intensity_index

        
        - summer_days

        
        - mean_of_daily_mean_temperature

        
        - mean_of_daily_minimum_temperature

        
        - minimum_of_daily_minimum_temperature

        
        - maximum_of_daily_minimum_temperature

        
        - tropical_nights

        
        - mean_of_daily_maximum_temperature

        
        - minimum_of_daily_maximum_temperature

        
        - maximum_of_daily_maximum_temperature

        
        - warm_spell_duration_index

        
        - warm_and_wet_days

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - 1_0

        
        - 1_1

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_agroclimatic_indicators(experiment: str, origin: str, period: OneOrMore[str], temporal_aggregation: str, variable: OneOrMore[str], version: OneOrMore[str]):
    return Collection_sis_agroclimatic_indicators.download(experiment=experiment, origin=origin, period=period, temporal_aggregation=temporal_aggregation, variable=variable, version=version)

