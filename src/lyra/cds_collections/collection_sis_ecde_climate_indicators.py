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

class Collection_sis_ecde_climate_indicators(Collection):
    collection_name = 'sis-ecde-climate-indicators'
    valid_values = dict(
        ensemble_member = ['r12i1p1', 'r1i1p1', 'r2i1p1', 'r3i1p1'],
        experiment = ['historical', 'rcp4_5', 'rcp8_5', 'ssp5_8_5'],
        gcm = ['cm2_vhr4', 'cm5a_mr', 'cnrm_cm5', 'ec_earth', 'ec_earth3p_hr', 'hadgem2_es', 'hadgem3_gc31_hm', 'hadgem3_gc31_hm_sst', 'ipsl_cm5a_mr', 'mpi_esm_lr', 'noresm1_m'],
        hydrological_model = ['e_hype', 'vic_wur'],
        origin = ['reanalysis', 'projections'],
        other_parameters = ['max', 'mean', 'min', '30_c', '35_c', '40_c', '1_in_2_year', '1_in_5_year', '1_in_10_year', '1_in_50_year'],
        rcm = ['aladin53', 'cclm4_8_17', 'hirham5', 'racmo22e', 'rca4', 'this_is_another_remo2009', 'wrf331f', 'wrf381p', 'csc_remo2009'],
        regional_layer = ['nuts_level_0', 'nuts_level_1', 'nuts_level_2', 'nuts_level_3', 'non_nuts', 'adriatic_ionian', 'alpine_space', 'northern_periphery_and_arctic', 'atlantic_area', 'baltic_sea_region', 'central_europe', 'danube', 'mediterranean', 'north_sea', 'north_west_europe', 'south_west_europe', 'eu_27', 'eea_32', 'eea_38'],
        spatial_aggregation = ['gridded', 'regional_layer'],
        temporal_aggregation = ['monthly', 'seasonal', 'yearly'],
        variable = ['mean_temperature', 'growing_degree_days', 'heating_degree_days', 'cooling_degree_days', 'tropical_nights', 'hot_days', 'warmest_three_day_period', 'heatwave_days', 'high_utci_days', 'frost_days', 'daily_maximum_temperature', 'daily_minimum_temperature', 'total_precipitation', 'maximum_consecutive_five_day_precipitation', 'extreme_precipitation_total', 'frequency_of_extreme_precipitation', 'flood_recurrence', 'mean_river_discharge', 'aridity_actual', 'consecutive_dry_days', 'duration_of_meteorological_droughts', 'magnitude_of_meteorological_droughts', 'mean_soil_moisture', 'days_with_high_fire_danger', 'mean_wind_speed', 'extreme_wind_speed_days', 'fire_weather_index', 'snowfall_amount', 'relative_sea_level_rise', 'extreme_sea_level'],
    )

    @Collection.wrapper
    def download(cls, ensemble_member: OneOrMore[str], experiment: OneOrMore[str], gcm: OneOrMore[str], hydrological_model: OneOrMore[str], origin: str, other_parameters: OneOrMore[str], rcm: OneOrMore[str], regional_layer: OneOrMore[str], spatial_aggregation: str, temporal_aggregation: OneOrMore[str], variable: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param ensemble_member:
        :type ensemble_member: str

        **Valid values:**
        
        - r12i1p1

        
        - r1i1p1

        
        - r2i1p1

        
        - r3i1p1

        ---

        :param experiment:
        :type experiment: str

        **Valid values:**
        
        - historical

        
        - rcp4_5

        
        - rcp8_5

        
        - ssp5_8_5

        ---

        :param gcm:
        :type gcm: str

        **Valid values:**
        
        - cm2_vhr4

        
        - cm5a_mr

        
        - cnrm_cm5

        
        - ec_earth

        
        - ec_earth3p_hr

        
        - hadgem2_es

        
        - hadgem3_gc31_hm

        
        - hadgem3_gc31_hm_sst

        
        - ipsl_cm5a_mr

        
        - mpi_esm_lr

        
        - noresm1_m

        ---

        :param hydrological_model:
        :type hydrological_model: str

        **Valid values:**
        
        - e_hype

        
        - vic_wur

        ---

        :param origin:
        :type origin: str

        **Valid values:**
        
        - reanalysis

        
        - projections

        ---

        :param other_parameters:
        :type other_parameters: str

        **Valid values:**
        
        - max

        
        - mean

        
        - min

        
        - 30_c

        
        - 35_c

        
        - 40_c

        
        - 1_in_2_year

        
        - 1_in_5_year

        
        - 1_in_10_year

        
        - 1_in_50_year

        ---

        :param rcm:
        :type rcm: str

        **Valid values:**
        
        - aladin53

        
        - cclm4_8_17

        
        - hirham5

        
        - racmo22e

        
        - rca4

        
        - this_is_another_remo2009

        
        - wrf331f

        
        - wrf381p

        
        - csc_remo2009

        ---

        :param regional_layer:
        :type regional_layer: str

        **Valid values:**
        
        - nuts_level_0

        
        - nuts_level_1

        
        - nuts_level_2

        
        - nuts_level_3

        
        - non_nuts

        
        - adriatic_ionian

        
        - alpine_space

        
        - northern_periphery_and_arctic

        
        - atlantic_area

        
        - baltic_sea_region

        
        - central_europe

        
        - danube

        
        - mediterranean

        
        - north_sea

        
        - north_west_europe

        
        - south_west_europe

        
        - eu_27

        
        - eea_32

        
        - eea_38

        ---

        :param spatial_aggregation:
        :type spatial_aggregation: str

        **Valid values:**
        
        - gridded

        
        - regional_layer

        ---

        :param temporal_aggregation:
        :type temporal_aggregation: str

        **Valid values:**
        
        - monthly

        
        - seasonal

        
        - yearly

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - mean_temperature

        
        - growing_degree_days

        
        - heating_degree_days

        
        - cooling_degree_days

        
        - tropical_nights

        
        - hot_days

        
        - warmest_three_day_period

        
        - heatwave_days

        
        - high_utci_days

        
        - frost_days

        
        - daily_maximum_temperature

        
        - daily_minimum_temperature

        
        - total_precipitation

        
        - maximum_consecutive_five_day_precipitation

        
        - extreme_precipitation_total

        
        - frequency_of_extreme_precipitation

        
        - flood_recurrence

        
        - mean_river_discharge

        
        - aridity_actual

        
        - consecutive_dry_days

        
        - duration_of_meteorological_droughts

        
        - magnitude_of_meteorological_droughts

        
        - mean_soil_moisture

        
        - days_with_high_fire_danger

        
        - mean_wind_speed

        
        - extreme_wind_speed_days

        
        - fire_weather_index

        
        - snowfall_amount

        
        - relative_sea_level_rise

        
        - extreme_sea_level

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_ecde_climate_indicators(ensemble_member: OneOrMore[str], experiment: OneOrMore[str], gcm: OneOrMore[str], hydrological_model: OneOrMore[str], origin: str, other_parameters: OneOrMore[str], rcm: OneOrMore[str], regional_layer: OneOrMore[str], spatial_aggregation: str, temporal_aggregation: OneOrMore[str], variable: OneOrMore[str]):
    return Collection_sis_ecde_climate_indicators.download(ensemble_member=ensemble_member, experiment=experiment, gcm=gcm, hydrological_model=hydrological_model, origin=origin, other_parameters=other_parameters, rcm=rcm, regional_layer=regional_layer, spatial_aggregation=spatial_aggregation, temporal_aggregation=temporal_aggregation, variable=variable)

