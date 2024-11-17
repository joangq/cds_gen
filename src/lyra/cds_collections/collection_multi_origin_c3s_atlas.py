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

class Collection_multi_origin_c3s_atlas(Collection):
    collection_name = 'multi-origin-c3s-atlas'
    valid_values = dict(
        domain = ['europe', 'euro_cordex', 'global', 'global_mosaic'],
        experiment = ['historical', 'rcp_2_6', 'rcp_4_5', 'rcp_8_5', 'ssp1_2_6', 'ssp2_4_5', 'ssp3_7_0', 'ssp5_8_5'],
        origin = ['cmip5', 'cmip6', 'cordex_core', 'cordex_eur_11', 'e_obs', 'era5', 'era5_land', 'oras5'],
        period = ['1850-2005', '1850-2014', '1940-2022', '1950-2021', '1950-2022', '1958-2014', '1970-2005', '2006-2100', '2015-2100'],
        variable = ['monthly_mean_of_daily_accumulated_evaporation', 'monthly_mean_of_daily_accumulated_precipitation', 'monthly_sea_level_pressure', 'monthly_near_surface_specific_humidity', 'monthly_mean_of_daily_accumulated_runoff', 'monthly_mean_of_daily_accumulated_snowfall_precipitation', 'monthly_mean_of_daily_accumulated_soil_moisture_in_upper_soil_portion', 'monthly_surface_thermal_radiation_downwards', 'monthly_surface_solar_radiation_downwards', 'monthly_fraction_of_cloud_cover', 'annual_cooling_degree_days', 'annual_consecutive_dry_days', 'monthly_count_of_frost_days', 'annual_heating_degree_days', 'monthly_maximum_of_1_day_accumulated_precipitation', 'monthly_maximum_of_5_day_accumulated_precipitation', 'monthly_mean_of_daily_mean_wind_speed', 'monthly_mean_of_sea_ice_area_percentage', 'monthly_standardised_precipitation_index_for_6_months_cumulation_period', 'monthly_mean_of_sea_surface_temperature', 'monthly_mean_of_daily_mean_temperature', 'monthly_mean_of_daily_minimum_temperature', 'monthly_minimum_of_daily_minimum_temperature', 'monthly_mean_of_daily_maximum_temperature', 'monthly_count_of_days_with_maximum_temperature_above_35_c', 'monthly_count_of_days_with_bias_adjusted_maximum_temperature_above_35_c', 'monthly_count_of_days_with_maximum_temperature_above_40_c', 'monthly_count_of_days_with_bias_adjusted_maximum_temperature_above_40_c', 'monthly_maximum_of_daily_maximum_temperature', 'monthly_standardised_precipitation_evapotranspiration_index_for_6_months_cumulation_period'],
    )

    @Collection.wrapper
    def download(cls, domain: str, experiment: str, origin: str, period: str, variable: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): 
        """
        Parameters
        ----------
        :param domain:
        :type domain: str

        **Valid values:**
        
        - europe

        
        - euro_cordex

        
        - global

        
        - global_mosaic

        ---

        :param experiment:
        :type experiment: str

        **Valid values:**
        
        - historical

        
        - rcp_2_6

        
        - rcp_4_5

        
        - rcp_8_5

        
        - ssp1_2_6

        
        - ssp2_4_5

        
        - ssp3_7_0

        
        - ssp5_8_5

        ---

        :param origin:
        :type origin: str

        **Valid values:**
        
        - cmip5

        
        - cmip6

        
        - cordex_core

        
        - cordex_eur_11

        
        - e_obs

        
        - era5

        
        - era5_land

        
        - oras5

        ---

        :param period:
        :type period: str

        **Valid values:**
        
        - 1850-2005

        
        - 1850-2014

        
        - 1940-2022

        
        - 1950-2021

        
        - 1950-2022

        
        - 1958-2014

        
        - 1970-2005

        
        - 2006-2100

        
        - 2015-2100

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - monthly_mean_of_daily_accumulated_evaporation

        
        - monthly_mean_of_daily_accumulated_precipitation

        
        - monthly_sea_level_pressure

        
        - monthly_near_surface_specific_humidity

        
        - monthly_mean_of_daily_accumulated_runoff

        
        - monthly_mean_of_daily_accumulated_snowfall_precipitation

        
        - monthly_mean_of_daily_accumulated_soil_moisture_in_upper_soil_portion

        
        - monthly_surface_thermal_radiation_downwards

        
        - monthly_surface_solar_radiation_downwards

        
        - monthly_fraction_of_cloud_cover

        
        - annual_cooling_degree_days

        
        - annual_consecutive_dry_days

        
        - monthly_count_of_frost_days

        
        - annual_heating_degree_days

        
        - monthly_maximum_of_1_day_accumulated_precipitation

        
        - monthly_maximum_of_5_day_accumulated_precipitation

        
        - monthly_mean_of_daily_mean_wind_speed

        
        - monthly_mean_of_sea_ice_area_percentage

        
        - monthly_standardised_precipitation_index_for_6_months_cumulation_period

        
        - monthly_mean_of_sea_surface_temperature

        
        - monthly_mean_of_daily_mean_temperature

        
        - monthly_mean_of_daily_minimum_temperature

        
        - monthly_minimum_of_daily_minimum_temperature

        
        - monthly_mean_of_daily_maximum_temperature

        
        - monthly_count_of_days_with_maximum_temperature_above_35_c

        
        - monthly_count_of_days_with_bias_adjusted_maximum_temperature_above_35_c

        
        - monthly_count_of_days_with_maximum_temperature_above_40_c

        
        - monthly_count_of_days_with_bias_adjusted_maximum_temperature_above_40_c

        
        - monthly_maximum_of_daily_maximum_temperature

        
        - monthly_standardised_precipitation_evapotranspiration_index_for_6_months_cumulation_period

        ---

        :param area_group:
        :type area_group: str

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_multi_origin_c3s_atlas(domain: str, experiment: str, origin: str, period: str, variable: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
    return Collection_multi_origin_c3s_atlas.download(domain=domain, experiment=experiment, origin=origin, period=period, variable=variable, area_group=area_group)

