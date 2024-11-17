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

class Collection_seasonal_monthly_single_levels(Collection):
    collection_name = 'seasonal-monthly-single-levels'
    valid_values = dict(
        leadtime_month = ['1', '2', '3', '4', '5', '6'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        originating_centre = ['ecmwf', 'ukmo', 'meteo_france', 'dwd', 'cmcc', 'ncep', 'jma', 'eccc'],
        product_type = ['ensemble_mean', 'hindcast_climate_mean', 'monthly_mean', 'monthly_minimum', 'monthly_maximum', 'monthly_standard_deviation'],
        system = ['1', '2', '3', '4', '5', '6', '7', '8', '12', '13', '14', '15', '21', '35', '51', '600', '601', '602', '603'],
        variable = ['10m_u_component_of_wind', '10m_v_component_of_wind', '10m_wind_gust_since_previous_post_processing', '10m_wind_speed', '2m_dewpoint_temperature', '2m_temperature', 'east_west_surface_stress_rate_of_accumulation', 'evaporation', 'maximum_2m_temperature_in_the_last_24_hours', 'mean_sea_level_pressure', 'mean_sub_surface_runoff_rate', 'mean_surface_runoff_rate', 'minimum_2m_temperature_in_the_last_24_hours', 'north_south_surface_stress_rate_of_accumulation', 'runoff', 'sea_surface_temperature', 'sea_ice_cover', 'snow_density', 'snow_depth', 'snowfall', 'soil_temperature_level_1', 'solar_insolation_rate_of_accumulation', 'surface_latent_heat_flux', 'surface_sensible_heat_flux', 'surface_solar_radiation', 'surface_solar_radiation_downwards', 'surface_thermal_radiation', 'surface_thermal_radiation_downwards', 'top_solar_radiation', 'top_thermal_radiation', 'total_cloud_cover', 'total_column_cloud_ice_water', 'total_column_cloud_liquid_water', 'total_column_water_vapour', 'total_precipitation'],
        year = ['1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
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

        
        - hindcast_climate_mean

        
        - monthly_mean

        
        - monthly_minimum

        
        - monthly_maximum

        
        - monthly_standard_deviation

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
        
        - 10m_u_component_of_wind

        
        - 10m_v_component_of_wind

        
        - 10m_wind_gust_since_previous_post_processing

        
        - 10m_wind_speed

        
        - 2m_dewpoint_temperature

        
        - 2m_temperature

        
        - east_west_surface_stress_rate_of_accumulation

        
        - evaporation

        
        - maximum_2m_temperature_in_the_last_24_hours

        
        - mean_sea_level_pressure

        
        - mean_sub_surface_runoff_rate

        
        - mean_surface_runoff_rate

        
        - minimum_2m_temperature_in_the_last_24_hours

        
        - north_south_surface_stress_rate_of_accumulation

        
        - runoff

        
        - sea_surface_temperature

        
        - sea_ice_cover

        
        - snow_density

        
        - snow_depth

        
        - snowfall

        
        - soil_temperature_level_1

        
        - solar_insolation_rate_of_accumulation

        
        - surface_latent_heat_flux

        
        - surface_sensible_heat_flux

        
        - surface_solar_radiation

        
        - surface_solar_radiation_downwards

        
        - surface_thermal_radiation

        
        - surface_thermal_radiation_downwards

        
        - top_solar_radiation

        
        - top_thermal_radiation

        
        - total_cloud_cover

        
        - total_column_cloud_ice_water

        
        - total_column_cloud_liquid_water

        
        - total_column_water_vapour

        
        - total_precipitation

        ---

        :param year:
        :type year: str

        **Valid values:**
        
        - 1981

        
        - 1982

        
        - 1983

        
        - 1984

        
        - 1985

        
        - 1986

        
        - 1987

        
        - 1988

        
        - 1989

        
        - 1990

        
        - 1991

        
        - 1992

        
        - 1993

        
        - 1994

        
        - 1995

        
        - 1996

        
        - 1997

        
        - 1998

        
        - 1999

        
        - 2000

        
        - 2001

        
        - 2002

        
        - 2003

        
        - 2004

        
        - 2005

        
        - 2006

        
        - 2007

        
        - 2008

        
        - 2009

        
        - 2010

        
        - 2011

        
        - 2012

        
        - 2013

        
        - 2014

        
        - 2015

        
        - 2016

        
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

def download_seasonal_monthly_single_levels(leadtime_month: OneOrMore[str], month: OneOrMore[str], originating_centre: str, product_type: OneOrMore[str], system: str, variable: OneOrMore[str], year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global', data_format: str = 'grib'):
    return Collection_seasonal_monthly_single_levels.download(leadtime_month=leadtime_month, month=month, originating_centre=originating_centre, product_type=product_type, system=system, variable=variable, year=year, area_group=area_group, data_format=data_format)

