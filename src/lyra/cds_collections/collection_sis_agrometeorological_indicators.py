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

class Collection_sis_agrometeorological_indicators(Collection):
    collection_name = 'sis-agrometeorological-indicators'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        statistic = ['24_hour_maximum', '24_hour_mean', '24_hour_minimum', 'day_time_maximum', 'day_time_mean', 'night_time_mean', 'night_time_minimum'],
        time = ['06_00', '09_00', '12_00', '15_00', '18_00'],
        variable = ['cloud_cover', 'precipitation_flux', 'liquid_precipitation_duration_fraction', 'solid_precipitation_duration_fraction', 'snow_thickness_lwe', 'snow_thickness', 'solar_radiation_flux', 'vapour_pressure', '2m_temperature', '10m_wind_speed', '2m_dewpoint_temperature', '2m_relative_humidity'],
        year = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        version = ['1_0', '1_1'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], month: OneOrMore[str], statistic: OneOrMore[str], time: OneOrMore[str], variable: str, year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global', version: str = '1_1'): 
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

        :param statistic:
        :type statistic: str

        **Valid values:**
        
        - 24_hour_maximum

        
        - 24_hour_mean

        
        - 24_hour_minimum

        
        - day_time_maximum

        
        - day_time_mean

        
        - night_time_mean

        
        - night_time_minimum

        ---

        :param time:
        :type time: str

        **Valid values:**
        
        - 06_00

        
        - 09_00

        
        - 12_00

        
        - 15_00

        
        - 18_00

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - cloud_cover

        
        - precipitation_flux

        
        - liquid_precipitation_duration_fraction

        
        - solid_precipitation_duration_fraction

        
        - snow_thickness_lwe

        
        - snow_thickness

        
        - solar_radiation_flux

        
        - vapour_pressure

        
        - 2m_temperature

        
        - 10m_wind_speed

        
        - 2m_dewpoint_temperature

        
        - 2m_relative_humidity

        ---

        :param year:
        :type year: str

        **Valid values:**
        
        - 1979

        
        - 1980

        
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

        :param version:
        :type version: str

        **Valid values:**
        
        - 1_0

        
        - 1_1

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_agrometeorological_indicators(day: OneOrMore[str], month: OneOrMore[str], statistic: OneOrMore[str], time: OneOrMore[str], variable: str, year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global', version: str = '1_1'):
    return Collection_sis_agrometeorological_indicators.download(day=day, month=month, statistic=statistic, time=time, variable=variable, year=year, area_group=area_group, version=version)

