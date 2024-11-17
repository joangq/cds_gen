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

class Collection_sis_biodiversity_era5_regional(Collection):
    collection_name = 'sis-biodiversity-era5-regional'
    valid_values = dict(
        derived_variable = ['annual_maximum', 'annual_maximum_of_daily_mean', 'annual_mean', 'annual_mean_of_daily_maximum', 'annual_mean_of_daily_minimum', 'annual_minimum', 'annual_sum', 'coldest_quarter', 'driest_quarter', 'end_of_season', 'length_of_season', 'maximum_length', 'mean_intensity', 'mean_length_with_minimum_5_days', 'monthly_mean', 'monthly_mean_of_daily_maximum', 'monthly_mean_of_daily_minimum', 'monthly_sum', 'number_of_occurrences', 'start_of_season', 'warmest_quarter', 'wettest_quarter'],
        origin = ['era5', 'era5_land'],
        region = ['central_africa', 'northern_brazil', 'europe'],
        statistic = ['mean', 'median', '25th_quartile', '75th_quartile'],
        variable = ['annual_mean_temperature', 'mean_diurnal_range', 'isothermality', 'temperature_seasonality', 'maximum_temperature_of_warmest_month', 'minimum_temperature_of_coldest_month', 'temperature_annual_range', 'mean_temperature_of_wettest_quarter', 'mean_temperature_of_driest_quarter', 'mean_temperature_of_warmest_quarter', 'mean_temperature_of_coldest_quarter', 'annual_precipitation', 'precipitation_of_wettest_month', 'precipitation_of_driest_month', 'precipitation_seasonality', 'precipitation_of_wettest_quarter', 'precipitation_of_driest_quarter', 'precipitation_of_warmest_quarter', 'precipitation_of_coldest_quarter', 'aridity', 'dry_spells', 'dry_days', 'summer_days', 'surface_latent_heat_flux', 'surface_sensible_heat_flux', 'evaporative_fraction', 'frost_days', 'growing_season', 'growing_degree_days', 'growing_degree_days_during_growing_season_length', 'koeppen_geiger_class', 'potential_evaporation', '2m_temperature', 'precipitation', 'water_vapor_pressure', 'cloud_cover', 'volumetric_soil_water', 'wind_speed', 'zonal_wind_speed', 'meridional_wind_speed'],
        version = ['1_0'],
    )

    @Collection.wrapper
    def download(cls, derived_variable: OneOrMore[str], origin: str, region: OneOrMore[str], statistic: OneOrMore[str], variable: OneOrMore[str], version: OneOrMore[str] = '1.0'): 
        """
        Parameters
        ----------
        :param derived_variable:
        :type derived_variable: str

        **Valid values:**
        
        - annual_maximum

        
        - annual_maximum_of_daily_mean

        
        - annual_mean

        
        - annual_mean_of_daily_maximum

        
        - annual_mean_of_daily_minimum

        
        - annual_minimum

        
        - annual_sum

        
        - coldest_quarter

        
        - driest_quarter

        
        - end_of_season

        
        - length_of_season

        
        - maximum_length

        
        - mean_intensity

        
        - mean_length_with_minimum_5_days

        
        - monthly_mean

        
        - monthly_mean_of_daily_maximum

        
        - monthly_mean_of_daily_minimum

        
        - monthly_sum

        
        - number_of_occurrences

        
        - start_of_season

        
        - warmest_quarter

        
        - wettest_quarter

        ---

        :param origin:
        :type origin: str

        **Valid values:**
        
        - era5

        
        - era5_land

        ---

        :param region:
        :type region: str

        **Valid values:**
        
        - central_africa

        
        - northern_brazil

        
        - europe

        ---

        :param statistic:
        :type statistic: str

        **Valid values:**
        
        - mean

        
        - median

        
        - 25th_quartile

        
        - 75th_quartile

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - annual_mean_temperature

        
        - mean_diurnal_range

        
        - isothermality

        
        - temperature_seasonality

        
        - maximum_temperature_of_warmest_month

        
        - minimum_temperature_of_coldest_month

        
        - temperature_annual_range

        
        - mean_temperature_of_wettest_quarter

        
        - mean_temperature_of_driest_quarter

        
        - mean_temperature_of_warmest_quarter

        
        - mean_temperature_of_coldest_quarter

        
        - annual_precipitation

        
        - precipitation_of_wettest_month

        
        - precipitation_of_driest_month

        
        - precipitation_seasonality

        
        - precipitation_of_wettest_quarter

        
        - precipitation_of_driest_quarter

        
        - precipitation_of_warmest_quarter

        
        - precipitation_of_coldest_quarter

        
        - aridity

        
        - dry_spells

        
        - dry_days

        
        - summer_days

        
        - surface_latent_heat_flux

        
        - surface_sensible_heat_flux

        
        - evaporative_fraction

        
        - frost_days

        
        - growing_season

        
        - growing_degree_days

        
        - growing_degree_days_during_growing_season_length

        
        - koeppen_geiger_class

        
        - potential_evaporation

        
        - 2m_temperature

        
        - precipitation

        
        - water_vapor_pressure

        
        - cloud_cover

        
        - volumetric_soil_water

        
        - wind_speed

        
        - zonal_wind_speed

        
        - meridional_wind_speed

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - 1_0

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_biodiversity_era5_regional(derived_variable: OneOrMore[str], origin: str, region: OneOrMore[str], statistic: OneOrMore[str], variable: OneOrMore[str], version: OneOrMore[str] = '1.0'):
    return Collection_sis_biodiversity_era5_regional.download(derived_variable=derived_variable, origin=origin, region=region, statistic=statistic, variable=variable, version=version)

