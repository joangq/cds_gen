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

class Collection_satellite_upper_troposphere_humidity(Collection):
    collection_name = 'satellite-upper-troposphere-humidity'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        sensor_on_satellite = ['mhs_on_metop_a', 'mhs_on_metop_b', 'mhs_on_metop_c', 'amsu_b_on_noaa_15', 'amsu_b_on_noaa_16', 'amsu_b_on_noaa_17', 'mhs_on_noaa_18', 'mhs_on_noaa_19'],
        year = ['1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021'],
        variable = ['all'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], month: OneOrMore[str], sensor_on_satellite: str, year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global', variable: str = 'all'): 
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

        :param sensor_on_satellite:
        :type sensor_on_satellite: str

        **Valid values:**
        
        - mhs_on_metop_a

        
        - mhs_on_metop_b

        
        - mhs_on_metop_c

        
        - amsu_b_on_noaa_15

        
        - amsu_b_on_noaa_16

        
        - amsu_b_on_noaa_17

        
        - mhs_on_noaa_18

        
        - mhs_on_noaa_19

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

        ---

        :param area_group:
        :type area_group: str

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - all

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_satellite_upper_troposphere_humidity(day: OneOrMore[str], month: OneOrMore[str], sensor_on_satellite: str, year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global', variable: str = 'all'):
    return Collection_satellite_upper_troposphere_humidity.download(day=day, month=month, sensor_on_satellite=sensor_on_satellite, year=year, area_group=area_group, variable=variable)

