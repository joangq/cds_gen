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

class Collection_seasonal_postprocessed_single_levels(Collection):
    collection_name = 'seasonal-postprocessed-single-levels'
    valid_values = dict(
        leadtime_month = ['1', '2', '3', '4', '5', '6'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        originating_centre = ['ecmwf', 'ukmo', 'meteo_france', 'dwd', 'cmcc', 'ncep', 'jma', 'eccc'],
        product_type = ['ensemble_mean', 'monthly_mean'],
        system = ['1', '2', '3', '4', '5', '6', '7', '8', '12', '13', '14', '15', '21', '35', '51', '600', '601', '602', '603'],
        variable = ['10m_u_component_of_wind_anomaly', '10m_v_component_of_wind_anomaly', '10m_wind_gust_anomaly', '10m_wind_speed_anomaly', '2m_dewpoint_temperature_anomaly', '2m_temperature_anomaly', 'east_west_surface_stress_anomalous_rate_of_accumulation', 'evaporation_anomalous_rate_of_accumulation', 'maximum_2m_temperature_in_the_last_24_hours_anomaly', 'mean_sea_level_pressure_anomaly', 'mean_sub_surface_runoff_rate_anomaly', 'mean_surface_runoff_rate_anomaly', 'minimum_2m_temperature_in_the_last_24_hours_anomaly', 'north_south_surface_stress_anomalous_rate_of_accumulation', 'runoff_anomalous_rate_of_accumulation', 'sea_surface_temperature_anomaly', 'sea_ice_cover_anomaly', 'snow_density_anomaly', 'snow_depth_anomaly', 'snowfall_anomalous_rate_of_accumulation', 'soil_temperature_anomaly_level_1', 'solar_insolation_anomalous_rate_of_accumulation', 'surface_latent_heat_flux_anomalous_rate_of_accumulation', 'surface_sensible_heat_flux_anomalous_rate_of_accumulation', 'surface_solar_radiation_anomalous_rate_of_accumulation', 'surface_solar_radiation_downwards_anomalous_rate_of_accumulation', 'surface_thermal_radiation_anomalous_rate_of_accumulation', 'surface_thermal_radiation_downwards_anomalous_rate_of_accumulation', 'top_solar_radiation_anomalous_rate_of_accumulation', 'top_thermal_radiation_anomalous_rate_of_accumulation', 'total_cloud_cover_anomaly', 'total_column_ice_water_anomaly', 'total_column_liquid_water_anomaly', 'total_column_water_vapour_anomaly', 'total_precipitation_anomalous_rate_of_accumulation'],
        year = ['2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        data_format = ['grib', 'netcdf'],
    )

    @Collection.wrapper
    def download(cls, leadtime_month: OneOrMore[str], month: OneOrMore[str], originating_centre: str, product_type: OneOrMore[str], system: str, variable: OneOrMore[str], year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global', data_format: str = 'grib'): 
        """
        Parameters
        ----------
        :param leadtime_month:
        :type leadtime_month: str

        **Valid values:**
        
        - 1

        
        - 2

        
        - 3

        
        - 4

        
        - 5

        
        - 6

        ---

        :param month:
        :type month: str

        **Valid values:**
        
        - 01

        
        - 02

        
        - 03

        
        - 04

        
        - 05

        
        - 06

        
        - 07

        
        - 08

        
        - 09

        
        - 10

        
        - 11

        
        - 12

        ---

        :param originating_centre:
        :type originating_centre: str

        **Valid values:**
        
        - ecmwf

        
        - ukmo

        
        - meteo_france

        
        - dwd

        
        - cmcc

        
        - ncep

        
        - jma

        
        - eccc

        ---

        :param product_type:
        :type product_type: str

        **Valid values:**
        
        - ensemble_mean

        
        - monthly_mean

        ---

        :param system:
        :type system: str

        **Valid values:**
        
        - 1

        
        - 2

        
        - 3

        
        - 4

        
        - 5

        
        - 6

        
        - 7

        
        - 8

        
        - 12

        
        - 13

        
        - 14

        
        - 15

        
        - 21

        
        - 35

        
        - 51

        
        - 600

        
        - 601

        
        - 602

        
        - 603

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - 10m_u_component_of_wind_anomaly

        
        - 10m_v_component_of_wind_anomaly

        
        - 10m_wind_gust_anomaly

        
        - 10m_wind_speed_anomaly

        
        - 2m_dewpoint_temperature_anomaly

        
        - 2m_temperature_anomaly

        
        - east_west_surface_stress_anomalous_rate_of_accumulation

        
        - evaporation_anomalous_rate_of_accumulation

        
        - maximum_2m_temperature_in_the_last_24_hours_anomaly

        
        - mean_sea_level_pressure_anomaly

        
        - mean_sub_surface_runoff_rate_anomaly

        
        - mean_surface_runoff_rate_anomaly

        
        - minimum_2m_temperature_in_the_last_24_hours_anomaly

        
        - north_south_surface_stress_anomalous_rate_of_accumulation

        
        - runoff_anomalous_rate_of_accumulation

        
        - sea_surface_temperature_anomaly

        
        - sea_ice_cover_anomaly

        
        - snow_density_anomaly

        
        - snow_depth_anomaly

        
        - snowfall_anomalous_rate_of_accumulation

        
        - soil_temperature_anomaly_level_1

        
        - solar_insolation_anomalous_rate_of_accumulation

        
        - surface_latent_heat_flux_anomalous_rate_of_accumulation

        
        - surface_sensible_heat_flux_anomalous_rate_of_accumulation

        
        - surface_solar_radiation_anomalous_rate_of_accumulation

        
        - surface_solar_radiation_downwards_anomalous_rate_of_accumulation

        
        - surface_thermal_radiation_anomalous_rate_of_accumulation

        
        - surface_thermal_radiation_downwards_anomalous_rate_of_accumulation

        
        - top_solar_radiation_anomalous_rate_of_accumulation

        
        - top_thermal_radiation_anomalous_rate_of_accumulation

        
        - total_cloud_cover_anomaly

        
        - total_column_ice_water_anomaly

        
        - total_column_liquid_water_anomaly

        
        - total_column_water_vapour_anomaly

        
        - total_precipitation_anomalous_rate_of_accumulation

        ---

        :param year:
        :type year: str

        **Valid values:**
        
        - 2017

        
        - 2018

        
        - 2019

        
        - 2020

        
        - 2021

        
        - 2022

        
        - 2023

        
        - 2024

        ---

        :param area_group:
        :type area_group: str

        ---

        :param data_format:
        :type data_format: str

        **Valid values:**
        
        - grib

        
        - netcdf

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_seasonal_postprocessed_single_levels(leadtime_month: OneOrMore[str], month: OneOrMore[str], originating_centre: str, product_type: OneOrMore[str], system: str, variable: OneOrMore[str], year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global', data_format: str = 'grib'):
    return Collection_seasonal_postprocessed_single_levels.download(leadtime_month=leadtime_month, month=month, originating_centre=originating_centre, product_type=product_type, system=system, variable=variable, year=year, area_group=area_group, data_format=data_format)

