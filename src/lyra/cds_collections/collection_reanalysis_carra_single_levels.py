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

class Collection_reanalysis_carra_single_levels(Collection):
    collection_name = 'reanalysis-carra-single-levels'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        domain = ['east_domain', 'west_domain'],
        leadtime_hour = ['1', '2', '3', '4', '5', '6', '9', '12', '15', '18', '21', '24', '27', '30'],
        level_type = ['surface_or_atmosphere', 'soil_level'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        product_type = ['analysis', 'forecast'],
        soil_level = ['soil_surface', 'root_depth'],
        time = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00'],
        variable = ['10m_eastward_wind_gust_since_previous_post_processing', '10m_northward_wind_gust_since_previous_post_processing', '10m_u_component_of_wind', '10m_v_component_of_wind', '10m_wind_direction', '10m_wind_gust_since_previous_post_processing', '10m_wind_speed', '2m_relative_humidity', '2m_specific_humidity', '2m_temperature', 'albedo', 'cloud_base', 'cloud_top', 'direct_solar_radiation', 'evaporation', 'fog', 'fraction_of_snow_cover', 'high_cloud_cover', 'land_sea_mask', 'low_cloud_cover', 'maximum_2m_temperature_since_previous_post_processing', 'mean_sea_level_pressure', 'medium_cloud_cover', 'minimum_2m_temperature_since_previous_post_processing', 'orography', 'percolation', 'precipitation_type', 'sea_ice_area_fraction', 'sea_ice_surface_temperature', 'sea_ice_thickness', 'sea_surface_temperature', 'skin_temperature', 'snow_albedo', 'snow_density', 'snow_depth_water_equivalent', 'snow_on_ice_total_depth', 'surface_latent_heat_flux', 'surface_net_solar_radiation', 'surface_net_solar_radiation,_clear_sky', 'surface_net_thermal_radiation', 'surface_net_thermal_radiation,_clear_sky', 'surface_pressure', 'surface_roughness', 'surface_roughness_length_for_heat', 'surface_runoff', 'surface_sensible_heat_flux', 'surface_solar_radiation_downwards', 'thermal_surface_radiation_downwards', 'time_integral_of_rain_flux', 'time_integral_of_snow_evaporation_flux', 'time_integral_of_surface_eastward_momentum_flux', 'time_integral_of_surface_latent_heat_evaporation_flux', 'time_integral_of_surface_latent_heat_sublimation_flux', 'time_integral_of_surface_northward_momentum_flux', 'time_integral_of_total_solid_precipitation_flux', 'time_integrated_surface_direct_short_wave_radiation_flux', 'top_net_solar_radiation', 'top_net_thermal_radiation', 'total_cloud_cover', 'total_column_cloud_ice_water', 'total_column_cloud_liquid_water', 'total_column_graupel', 'total_column_integrated_water_vapour', 'total_precipitation', 'visibility', 'volumetric_soil_ice', 'volumetric_soil_moisture'],
        year = ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        data_format = ['grib', 'netcdf'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], domain: str, leadtime_hour: OneOrMore[str], level_type: str, month: OneOrMore[str], product_type: str, soil_level: OneOrMore[str], time: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], data_format: str = 'grib'): 
        """
        Parameters
        ----------
        :param day:
        :type day: str

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

        
        - 13

        
        - 14

        
        - 15

        
        - 16

        
        - 17

        
        - 18

        
        - 19

        
        - 20

        
        - 21

        
        - 22

        
        - 23

        
        - 24

        
        - 25

        
        - 26

        
        - 27

        
        - 28

        
        - 29

        
        - 30

        
        - 31

        ---

        :param domain:
        :type domain: str

        **Valid values:**
        
        - east_domain

        
        - west_domain

        ---

        :param leadtime_hour:
        :type leadtime_hour: str

        **Valid values:**
        
        - 1

        
        - 2

        
        - 3

        
        - 4

        
        - 5

        
        - 6

        
        - 9

        
        - 12

        
        - 15

        
        - 18

        
        - 21

        
        - 24

        
        - 27

        
        - 30

        ---

        :param level_type:
        :type level_type: str

        **Valid values:**
        
        - surface_or_atmosphere

        
        - soil_level

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

        :param product_type:
        :type product_type: str

        **Valid values:**
        
        - analysis

        
        - forecast

        ---

        :param soil_level:
        :type soil_level: str

        **Valid values:**
        
        - soil_surface

        
        - root_depth

        ---

        :param time:
        :type time: str

        **Valid values:**
        
        - 00:00

        
        - 03:00

        
        - 06:00

        
        - 09:00

        
        - 12:00

        
        - 15:00

        
        - 18:00

        
        - 21:00

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - 10m_eastward_wind_gust_since_previous_post_processing

        
        - 10m_northward_wind_gust_since_previous_post_processing

        
        - 10m_u_component_of_wind

        
        - 10m_v_component_of_wind

        
        - 10m_wind_direction

        
        - 10m_wind_gust_since_previous_post_processing

        
        - 10m_wind_speed

        
        - 2m_relative_humidity

        
        - 2m_specific_humidity

        
        - 2m_temperature

        
        - albedo

        
        - cloud_base

        
        - cloud_top

        
        - direct_solar_radiation

        
        - evaporation

        
        - fog

        
        - fraction_of_snow_cover

        
        - high_cloud_cover

        
        - land_sea_mask

        
        - low_cloud_cover

        
        - maximum_2m_temperature_since_previous_post_processing

        
        - mean_sea_level_pressure

        
        - medium_cloud_cover

        
        - minimum_2m_temperature_since_previous_post_processing

        
        - orography

        
        - percolation

        
        - precipitation_type

        
        - sea_ice_area_fraction

        
        - sea_ice_surface_temperature

        
        - sea_ice_thickness

        
        - sea_surface_temperature

        
        - skin_temperature

        
        - snow_albedo

        
        - snow_density

        
        - snow_depth_water_equivalent

        
        - snow_on_ice_total_depth

        
        - surface_latent_heat_flux

        
        - surface_net_solar_radiation

        
        - surface_net_solar_radiation,_clear_sky

        
        - surface_net_thermal_radiation

        
        - surface_net_thermal_radiation,_clear_sky

        
        - surface_pressure

        
        - surface_roughness

        
        - surface_roughness_length_for_heat

        
        - surface_runoff

        
        - surface_sensible_heat_flux

        
        - surface_solar_radiation_downwards

        
        - thermal_surface_radiation_downwards

        
        - time_integral_of_rain_flux

        
        - time_integral_of_snow_evaporation_flux

        
        - time_integral_of_surface_eastward_momentum_flux

        
        - time_integral_of_surface_latent_heat_evaporation_flux

        
        - time_integral_of_surface_latent_heat_sublimation_flux

        
        - time_integral_of_surface_northward_momentum_flux

        
        - time_integral_of_total_solid_precipitation_flux

        
        - time_integrated_surface_direct_short_wave_radiation_flux

        
        - top_net_solar_radiation

        
        - top_net_thermal_radiation

        
        - total_cloud_cover

        
        - total_column_cloud_ice_water

        
        - total_column_cloud_liquid_water

        
        - total_column_graupel

        
        - total_column_integrated_water_vapour

        
        - total_precipitation

        
        - visibility

        
        - volumetric_soil_ice

        
        - volumetric_soil_moisture

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

def download_reanalysis_carra_single_levels(day: OneOrMore[str], domain: str, leadtime_hour: OneOrMore[str], level_type: str, month: OneOrMore[str], product_type: str, soil_level: OneOrMore[str], time: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], data_format: str = 'grib'):
    return Collection_reanalysis_carra_single_levels.download(day=day, domain=domain, leadtime_hour=leadtime_hour, level_type=level_type, month=month, product_type=product_type, soil_level=soil_level, time=time, variable=variable, year=year, data_format=data_format)

