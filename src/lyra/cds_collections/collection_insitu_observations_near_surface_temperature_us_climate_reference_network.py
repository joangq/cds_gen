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

class Collection_insitu_observations_near_surface_temperature_us_climate_reference_network(Collection):
    collection_name = 'insitu-observations-near-surface-temperature-us-climate-reference-network'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        format = ['netcdf', 'csv'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        time_aggregation = ['daily', 'hourly', 'monthly', 'sub_hourly'],
        variable = ['air_temperature', 'daily_maximum_air_temperature', 'daily_minimum_air_temperature', 'relative_humidity', 'daily_maximum_relative_humidity', 'daily_minimum_relative_humidity', 'downward_shortwave_irradiance_at_earth_surface', 'hourly_maximum_downward_shortwave_irradiance_at_earth_surface', 'hourly_minimum_downward_shortwave_irradiance_at_earth_surface', 'hourly_maximum_soil_temperature', 'hourly_minimum_soil_temperature', 'monthly_maximum_soil_temperature', 'monthly_minimum_soil_temperature', 'soil_temperature', 'soil_temperature_100cm_from_earth_surface', 'soil_temperature_10cm_from_earth_surface', 'soil_temperature_20cm_from_earth_surface', 'soil_temperature_50cm_from_earth_surface', 'soil_temperature_5cm_from_earth_surface', 'soil_moisture_100cm_from_earth_surface', 'soil_moisture_10cm_from_earth_surface', 'soil_moisture_20cm_from_earth_surface', 'soil_moisture_50cm_from_earth_surface', 'soil_moisture_5cm_from_earth_surface', 'accumulated_precipitation', 'wind_speed_2_meters_from_earth_surface'],
        year = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], format: str, month: OneOrMore[str], time_aggregation: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): 
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

        :param format:
        :type format: str

        **Valid values:**
        
        - netcdf

        
        - csv

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

        :param time_aggregation:
        :type time_aggregation: str

        **Valid values:**
        
        - daily

        
        - hourly

        
        - monthly

        
        - sub_hourly

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - air_temperature

        
        - daily_maximum_air_temperature

        
        - daily_minimum_air_temperature

        
        - relative_humidity

        
        - daily_maximum_relative_humidity

        
        - daily_minimum_relative_humidity

        
        - downward_shortwave_irradiance_at_earth_surface

        
        - hourly_maximum_downward_shortwave_irradiance_at_earth_surface

        
        - hourly_minimum_downward_shortwave_irradiance_at_earth_surface

        
        - hourly_maximum_soil_temperature

        
        - hourly_minimum_soil_temperature

        
        - monthly_maximum_soil_temperature

        
        - monthly_minimum_soil_temperature

        
        - soil_temperature

        
        - soil_temperature_100cm_from_earth_surface

        
        - soil_temperature_10cm_from_earth_surface

        
        - soil_temperature_20cm_from_earth_surface

        
        - soil_temperature_50cm_from_earth_surface

        
        - soil_temperature_5cm_from_earth_surface

        
        - soil_moisture_100cm_from_earth_surface

        
        - soil_moisture_10cm_from_earth_surface

        
        - soil_moisture_20cm_from_earth_surface

        
        - soil_moisture_50cm_from_earth_surface

        
        - soil_moisture_5cm_from_earth_surface

        
        - accumulated_precipitation

        
        - wind_speed_2_meters_from_earth_surface

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

def download_insitu_observations_near_surface_temperature_us_climate_reference_network(day: OneOrMore[str], format: str, month: OneOrMore[str], time_aggregation: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
    return Collection_insitu_observations_near_surface_temperature_us_climate_reference_network.download(day=day, format=format, month=month, time_aggregation=time_aggregation, variable=variable, year=year, area_group=area_group)

