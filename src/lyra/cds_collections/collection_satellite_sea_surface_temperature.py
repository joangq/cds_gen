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

class Collection_satellite_sea_surface_temperature(Collection):
    collection_name = 'satellite-sea-surface-temperature'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        processinglevel = ['level_3c', 'level_4'],
        sensor_on_satellite = ['avhrr_on_noaa_07', 'avhrr_on_noaa_15', 'avhrr_on_metop_a', 'aatsr_on_envisat', 'avhrr_on_noaa_09', 'avhrr_on_noaa_16', 'avhrr_on_metop_b', 'slstr_on_sentinel_3a', 'avhrr_on_noaa_11', 'avhrr_on_noaa_17', 'atsr1_on_ers_1', 'slstr_on_sentinel_3b', 'avhrr_on_noaa_12', 'avhrr_on_noaa_18', 'atsr2_on_ers_2', 'combined_product', 'avhrr_on_noaa_14', 'avhrr_on_noaa_19'],
        year = ['1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'],
        variable = ['all'],
        version = ['2_1', '2_0', '1_1'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], month: OneOrMore[str], processinglevel: str, sensor_on_satellite: str, year: OneOrMore[str], variable: str = 'all', version: str = '2_1'): 
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

        :param processinglevel:
        :type processinglevel: str

        **Valid values:**
        
        - level_3c

        
        - level_4

        ---

        :param sensor_on_satellite:
        :type sensor_on_satellite: str

        **Valid values:**
        
        - avhrr_on_noaa_07

        
        - avhrr_on_noaa_15

        
        - avhrr_on_metop_a

        
        - aatsr_on_envisat

        
        - avhrr_on_noaa_09

        
        - avhrr_on_noaa_16

        
        - avhrr_on_metop_b

        
        - slstr_on_sentinel_3a

        
        - avhrr_on_noaa_11

        
        - avhrr_on_noaa_17

        
        - atsr1_on_ers_1

        
        - slstr_on_sentinel_3b

        
        - avhrr_on_noaa_12

        
        - avhrr_on_noaa_18

        
        - atsr2_on_ers_2

        
        - combined_product

        
        - avhrr_on_noaa_14

        
        - avhrr_on_noaa_19

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

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - all

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - 2_1

        
        - 2_0

        
        - 1_1

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_satellite_sea_surface_temperature(day: OneOrMore[str], month: OneOrMore[str], processinglevel: str, sensor_on_satellite: str, year: OneOrMore[str], variable: str = 'all', version: str = '2_1'):
    return Collection_satellite_sea_surface_temperature.download(day=day, month=month, processinglevel=processinglevel, sensor_on_satellite=sensor_on_satellite, year=year, variable=variable, version=version)

