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

class Collection_reanalysis_cerra_height_levels(Collection):
    collection_name = 'reanalysis-cerra-height-levels'
    valid_values = dict(
        data_type = ['ensemble_members', 'reanalysis'],
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        height_level = ['15_m', '30_m', '50_m', '75_m', '100_m', '150_m', '200_m', '250_m', '300_m', '400_m', '500_m'],
        leadtime_hour = ['1', '2', '3', '4', '5', '6', '9', '12', '15', '18', '21', '24', '27', '30'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        product_type = ['analysis', 'forecast'],
        time = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00'],
        variable = ['pressure', 'relative_humidity', 'specific_cloud_ice_water_content', 'specific_cloud_liquid_water_content', 'specific_rain_water_content', 'specific_snow_water_content', 'temperature', 'turbulent_kinetic_energy', 'wind_direction', 'wind_speed'],
        year = ['1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021'],
        data_format = ['grib', 'netcdf'],
    )

    @Collection.wrapper
    def download(cls, data_type: OneOrMore[str], day: OneOrMore[str], height_level: OneOrMore[str], leadtime_hour: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], time: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], data_format: str = 'grib'): 
        """
        Parameters
        ----------
        :param data_type:
        :type data_type: str

        **Valid values:**
        
        - ensemble_members

        
        - reanalysis

        ---

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

        :param height_level:
        :type height_level: str

        **Valid values:**
        
        - 15_m

        
        - 30_m

        
        - 50_m

        
        - 75_m

        
        - 100_m

        
        - 150_m

        
        - 200_m

        
        - 250_m

        
        - 300_m

        
        - 400_m

        
        - 500_m

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
        
        - pressure

        
        - relative_humidity

        
        - specific_cloud_ice_water_content

        
        - specific_cloud_liquid_water_content

        
        - specific_rain_water_content

        
        - specific_snow_water_content

        
        - temperature

        
        - turbulent_kinetic_energy

        
        - wind_direction

        
        - wind_speed

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

def download_reanalysis_cerra_height_levels(data_type: OneOrMore[str], day: OneOrMore[str], height_level: OneOrMore[str], leadtime_hour: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], time: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], data_format: str = 'grib'):
    return Collection_reanalysis_cerra_height_levels.download(data_type=data_type, day=day, height_level=height_level, leadtime_hour=leadtime_hour, month=month, product_type=product_type, time=time, variable=variable, year=year, data_format=data_format)

