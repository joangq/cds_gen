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

class Collection_insitu_observations_gruan_reference_network(Collection):
    collection_name = 'insitu-observations-gruan-reference-network'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        format = ['netcdf', 'csv'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        variable = ['air_temperature', 'relative_humidity', 'air_relative_humidity_effective_vertical_resolution', 'eastward_wind_speed', 'northward_wind_speed', 'wind_from_direction', 'wind_speed', 'shortwave_radiation', 'altitude', 'frost_point_temperature', 'geopotential_height', 'vertical_speed_of_radiosonde', 'water_vapour_mixing_ratio'],
        year = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], format: str, month: str, variable: OneOrMore[str], year: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): 
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

        :param variable:
        :type variable: str

        **Valid values:**
        
        - air_temperature

        
        - relative_humidity

        
        - air_relative_humidity_effective_vertical_resolution

        
        - eastward_wind_speed

        
        - northward_wind_speed

        
        - wind_from_direction

        
        - wind_speed

        
        - shortwave_radiation

        
        - altitude

        
        - frost_point_temperature

        
        - geopotential_height

        
        - vertical_speed_of_radiosonde

        
        - water_vapour_mixing_ratio

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

def download_insitu_observations_gruan_reference_network(day: OneOrMore[str], format: str, month: str, variable: OneOrMore[str], year: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
    return Collection_insitu_observations_gruan_reference_network.download(day=day, format=format, month=month, variable=variable, year=year, area_group=area_group)

