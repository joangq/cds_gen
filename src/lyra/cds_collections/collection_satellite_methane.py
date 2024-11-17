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

class Collection_satellite_methane(Collection):
    collection_name = 'satellite-methane'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        processing_level = ['level_2', 'level_3'],
        sensor_and_algorithm = ['iasi_metop_a_nlis', 'iasi_metop_b_nlis', 'iasi_metop_c_nlis', 'sciamachy_imap', 'sciamachy_wfmd', 'tanso_fts_ocfp', 'tanso_fts_ocpr', 'tanso_fts_srfp', 'tanso_fts_srpr', 'tanso2_fts_srfp', 'tanso2_fts_srpr', 'merged_emma', 'merged_obs4mips'],
        variable = ['ch4', 'xch4'],
        version = ['4_3', '4_5', '7_2', '7_3', '9_0', '9_1', '10_2', '2_0_1', '2_3_8', '2_3_9', '3', '3_0', '3_1', '4_0', '4_1', '4_2', '4_4', '4_5', '7_0', '7_1', '7_2', '7_3', '8_1', '8_4', '9_0', '9_1', '10_2', '2_0_0', '2_0_1', '2_3_8', '2_3_9'],
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
        
        - iasi_metop_a_nlis

        
        - iasi_metop_b_nlis

        
        - iasi_metop_c_nlis

        
        - sciamachy_imap

        
        - sciamachy_wfmd

        
        - tanso_fts_ocfp

        
        - tanso_fts_ocpr

        
        - tanso_fts_srfp

        
        - tanso_fts_srpr

        
        - tanso2_fts_srfp

        
        - tanso2_fts_srpr

        
        - merged_emma

        
        - merged_obs4mips

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - ch4

        
        - xch4

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - 4_3

        
        - 4_5

        
        - 7_2

        
        - 7_3

        
        - 9_0

        
        - 9_1

        
        - 10_2

        
        - 2_0_1

        
        - 2_3_8

        
        - 2_3_9

        
        - 3

        
        - 3_0

        
        - 3_1

        
        - 4_0

        
        - 4_1

        
        - 4_2

        
        - 4_4

        
        - 4_5

        
        - 7_0

        
        - 7_1

        
        - 7_2

        
        - 7_3

        
        - 8_1

        
        - 8_4

        
        - 9_0

        
        - 9_1

        
        - 10_2

        
        - 2_0_0

        
        - 2_0_1

        
        - 2_3_8

        
        - 2_3_9

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

def download_satellite_methane(day: OneOrMore[str], month: OneOrMore[str], processing_level: OneOrMore[str], sensor_and_algorithm: str, variable: str, version: OneOrMore[str], year: OneOrMore[str]):
    return Collection_satellite_methane.download(day=day, month=month, processing_level=processing_level, sensor_and_algorithm=sensor_and_algorithm, variable=variable, version=version, year=year)

