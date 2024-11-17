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

class Collection_satellite_carbon_dioxide(Collection):
    collection_name = 'satellite-carbon-dioxide'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        processing_level = ['level_2', 'level_3'],
        sensor_and_algorithm = ['airs_nlis', 'iasi_metop_a_nlis', 'iasi_metop_b_nlis', 'iasi_metop_c_nlis', 'sciamachy_wfmd', 'sciamachy_besd', 'tanso_fts_ocfp', 'tanso_fts_srfp', 'tanso2_fts_srfp', 'merged_emma', 'merged_obs4mips'],
        variable = ['co2', 'xco2'],
        version = ['3_0', '4_5', '7_3', '10_1', '2_0_0', '2_3_8', '02_01_02', '3', '3_0', '3_1', '4_0', '4_1', '4_2', '4_3', '4_4', '4_5', '7_1', '7_2', '7_3', '8_0', '9_1', '10_1', '2_0_0', '2_3_8', '02_01_02'],
        year = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], month: OneOrMore[str], processing_level: OneOrMore[str], sensor_and_algorithm: str, variable: str, version: OneOrMore[str], year: OneOrMore[str]): 
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

        :param processing_level:
        :type processing_level: str

        **Valid values:**
        
        - level_2

        
        - level_3

        ---

        :param sensor_and_algorithm:
        :type sensor_and_algorithm: str

        **Valid values:**
        
        - airs_nlis

        
        - iasi_metop_a_nlis

        
        - iasi_metop_b_nlis

        
        - iasi_metop_c_nlis

        
        - sciamachy_wfmd

        
        - sciamachy_besd

        
        - tanso_fts_ocfp

        
        - tanso_fts_srfp

        
        - tanso2_fts_srfp

        
        - merged_emma

        
        - merged_obs4mips

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - co2

        
        - xco2

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - 3_0

        
        - 4_5

        
        - 7_3

        
        - 10_1

        
        - 2_0_0

        
        - 2_3_8

        
        - 02_01_02

        
        - 3

        
        - 3_0

        
        - 3_1

        
        - 4_0

        
        - 4_1

        
        - 4_2

        
        - 4_3

        
        - 4_4

        
        - 4_5

        
        - 7_1

        
        - 7_2

        
        - 7_3

        
        - 8_0

        
        - 9_1

        
        - 10_1

        
        - 2_0_0

        
        - 2_3_8

        
        - 02_01_02

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_satellite_carbon_dioxide(day: OneOrMore[str], month: OneOrMore[str], processing_level: OneOrMore[str], sensor_and_algorithm: str, variable: str, version: OneOrMore[str], year: OneOrMore[str]):
    return Collection_satellite_carbon_dioxide.download(day=day, month=month, processing_level=processing_level, sensor_and_algorithm=sensor_and_algorithm, variable=variable, version=version, year=year)

