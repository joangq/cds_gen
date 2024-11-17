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

class Collection_projections_climate_atlas(Collection):
    collection_name = 'projections-climate-atlas'
    valid_values = dict(
        domain = ['global', 'africa', 'antarctica', 'arctic', 'australasia', 'central_america', 'east_asia', 'europe', 'north_america', 'south_america', 'southeast_asia', 'south_asia'],
        experiment = ['historical', 'rcp_2_6', 'rcp_4_5', 'rcp_8_5', 'ssp1_2_6', 'ssp2_4_5', 'ssp3_7_0', 'ssp5_8_5'],
        origin = ['cmip5', 'cmip6', 'cordex'],
        period = ['1850-2005', '1850-2014', '1950-2005', '1950-2014', '1970-2005', '2006-2098', '2006-2100', '2015-2100'],
        variable = ['monthly_mean_of_daily_accumulated_precipitation', 'monthly_mean_of_daily_accumulated_snowfall_precipitation', 'annual_cooling_degree_days', 'annual_consecutive_dry_days', 'monthly_count_of_frost_days', 'annual_heating_degree_days', 'monthly_mean_of_acidity_of_seawater', 'monthly_maximum_of_1_day_accumulated_precipitation', 'monthly_maximum_of_5_day_accumulated_precipitation', 'monthly_mean_of_daily_mean_wind_speed', 'monthly_mean_of_sea_ice_area_percentage', 'standardized_precipitation_index_for_6_months_cumulation_period', 'monthly_mean_of_sea_surface_temperature', 'monthly_mean_of_daily_mean_temperature', 'monthly_mean_of_daily_minimum_temperature', 'monthly_minimum_of_daily_minimum_temperature', 'monthly_mean_of_daily_maximum_temperature', 'monthly_count_of_days_with_maximum_temperature_above_35_c', 'bias_adjusted_monthly_count_of_days_with_maximum_temperature_above_35_c', 'monthly_count_of_days_with_maximum_temperature_above_40_c', 'bias_adjusted_monthly_count_of_days_with_maximum_temperature_above_40_c', 'monthly_maximum_of_daily_maximum_temperature'],
    )

    @Collection.wrapper
    def download(cls, domain: str, experiment: str, origin: str, period: str, variable: str): 
        """
        Parameters
        ----------
        :param domain:
        :type domain: str

        **Valid values:**
        
        - global

        
        - africa

        
        - antarctica

        
        - arctic

        
        - australasia

        
        - central_america

        
        - east_asia

        
        - europe

        
        - north_america

        
        - south_america

        
        - southeast_asia

        
        - south_asia

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

        
        - cordex

        ---

        :param period:
        :type period: str

        **Valid values:**
        
        - 1850-2005

        
        - 1850-2014

        
        - 1950-2005

        
        - 1950-2014

        
        - 1970-2005

        
        - 2006-2098

        
        - 2006-2100

        
        - 2015-2100

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - monthly_mean_of_daily_accumulated_precipitation

        
        - monthly_mean_of_daily_accumulated_snowfall_precipitation

        
        - annual_cooling_degree_days

        
        - annual_consecutive_dry_days

        
        - monthly_count_of_frost_days

        
        - annual_heating_degree_days

        
        - monthly_mean_of_acidity_of_seawater

        
        - monthly_maximum_of_1_day_accumulated_precipitation

        
        - monthly_maximum_of_5_day_accumulated_precipitation

        
        - monthly_mean_of_daily_mean_wind_speed

        
        - monthly_mean_of_sea_ice_area_percentage

        
        - standardized_precipitation_index_for_6_months_cumulation_period

        
        - monthly_mean_of_sea_surface_temperature

        
        - monthly_mean_of_daily_mean_temperature

        
        - monthly_mean_of_daily_minimum_temperature

        
        - monthly_minimum_of_daily_minimum_temperature

        
        - monthly_mean_of_daily_maximum_temperature

        
        - monthly_count_of_days_with_maximum_temperature_above_35_c

        
        - bias_adjusted_monthly_count_of_days_with_maximum_temperature_above_35_c

        
        - monthly_count_of_days_with_maximum_temperature_above_40_c

        
        - bias_adjusted_monthly_count_of_days_with_maximum_temperature_above_40_c

        
        - monthly_maximum_of_daily_maximum_temperature

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_projections_climate_atlas(domain: str, experiment: str, origin: str, period: str, variable: str):
    return Collection_projections_climate_atlas.download(domain=domain, experiment=experiment, origin=origin, period=period, variable=variable)

