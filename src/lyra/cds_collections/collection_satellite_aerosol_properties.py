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

class Collection_satellite_aerosol_properties(Collection):
    collection_name = 'satellite-aerosol-properties'
    valid_values = dict(
        algorithm = ['aergom', 'adv', 'ens', 'grasp', 'imars', 'lmd', 'mapir', 'orac', 'sdv', 'swansea', 's4m', 's4o', 'ulb', 'xbaer'],
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        orbit = ['ascending', 'descending', 'ascending_and_descending'],
        sensor_on_satellite = ['aatsr_on_envisat', 'atsr2_on_ers2', 'slstr_on_sentinel_3a', 'slstr_on_sentinel_3b', 'polder_on_parasol', 'meris_on_envisat', 'iasi_on_metopa', 'iasi_on_metopb', 'iasi_on_metopc', 'olci_on_sentinel_3a', 'gomos_on_envisat'],
        time_aggregation = ['daily_average', 'monthly_average', '5_daily_composite'],
        variable = ['aerosol_optical_depth', 'fine_mode_aerosol_optical_depth', 'dust_aerosol_optical_depth', 'single_scattering_albedo', 'aerosol_layer_height', 'dust_aerosol_layer_height', 'aerosol_extinction_coefficient'],
        version = ['deprecated (v4.32)', 'v2_30', 'v2_6', 'v2_9', 'v3_0', 'v3_11', 'v4_0', 'v4_01', 'v4_02', 'v4_1', 'v4_3', 'v4_32_latest', 'v4_33', 'deprecated (v1.11)', 'v1_00', 'v1_10', 'v1_12', 'v2_00', 'v2_10', 'v2_20', 'v2_30', 'v0_08', 'v2_01', 'v2_10', 'v2_20', 'v1_0', 'v2_1', 'v2_3', 'v4_8a', 'v7_0a', 'v1_0', 'v1_1', 'v1_2', 'v1_3', 'v1_4', 'v2_1', 'v2_2', 'v3_51', 'v3_7', 'v4_0', 'v4_1', 'v5_0', 'v5_1', 'v5_2', 'v6_0', 'v7_0', 'v7_1', 'v8', 'v9', 'v1_0', 'v1_1', 'v2_0', 'deprecated (v5.00)', 'v3_00', 'v4_00', 'v4_01s', 'deprecated (v5.00)', 'v1_0', 'v1_1', 'v1_2', 'v1_3', 'v1_4', 'v2_1', 'v2_2', 'v2_3', 'v2_6', 'v2_9', 'v3_0', 'v3_1'],
        year = ['1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    )

    @Collection.wrapper
    def download(cls, algorithm: str, day: OneOrMore[str], month: OneOrMore[str], orbit: OneOrMore[str], sensor_on_satellite: str, time_aggregation: str, variable: OneOrMore[str], version: OneOrMore[str], year: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param algorithm:
        :type algorithm: str

        **Valid values:**
        
        - aergom

        
        - adv

        
        - ens

        
        - grasp

        
        - imars

        
        - lmd

        
        - mapir

        
        - orac

        
        - sdv

        
        - swansea

        
        - s4m

        
        - s4o

        
        - ulb

        
        - xbaer

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

        :param orbit:
        :type orbit: str

        **Valid values:**
        
        - ascending

        
        - descending

        
        - ascending_and_descending

        ---

        :param sensor_on_satellite:
        :type sensor_on_satellite: str

        **Valid values:**
        
        - aatsr_on_envisat

        
        - atsr2_on_ers2

        
        - slstr_on_sentinel_3a

        
        - slstr_on_sentinel_3b

        
        - polder_on_parasol

        
        - meris_on_envisat

        
        - iasi_on_metopa

        
        - iasi_on_metopb

        
        - iasi_on_metopc

        
        - olci_on_sentinel_3a

        
        - gomos_on_envisat

        ---

        :param time_aggregation:
        :type time_aggregation: str

        **Valid values:**
        
        - daily_average

        
        - monthly_average

        
        - 5_daily_composite

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - aerosol_optical_depth

        
        - fine_mode_aerosol_optical_depth

        
        - dust_aerosol_optical_depth

        
        - single_scattering_albedo

        
        - aerosol_layer_height

        
        - dust_aerosol_layer_height

        
        - aerosol_extinction_coefficient

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - deprecated (v4.32)

        
        - v2_30

        
        - v2_6

        
        - v2_9

        
        - v3_0

        
        - v3_11

        
        - v4_0

        
        - v4_01

        
        - v4_02

        
        - v4_1

        
        - v4_3

        
        - v4_32_latest

        
        - v4_33

        
        - deprecated (v1.11)

        
        - v1_00

        
        - v1_10

        
        - v1_12

        
        - v2_00

        
        - v2_10

        
        - v2_20

        
        - v2_30

        
        - v0_08

        
        - v2_01

        
        - v2_10

        
        - v2_20

        
        - v1_0

        
        - v2_1

        
        - v2_3

        
        - v4_8a

        
        - v7_0a

        
        - v1_0

        
        - v1_1

        
        - v1_2

        
        - v1_3

        
        - v1_4

        
        - v2_1

        
        - v2_2

        
        - v3_51

        
        - v3_7

        
        - v4_0

        
        - v4_1

        
        - v5_0

        
        - v5_1

        
        - v5_2

        
        - v6_0

        
        - v7_0

        
        - v7_1

        
        - v8

        
        - v9

        
        - v1_0

        
        - v1_1

        
        - v2_0

        
        - deprecated (v5.00)

        
        - v3_00

        
        - v4_00

        
        - v4_01s

        
        - deprecated (v5.00)

        
        - v1_0

        
        - v1_1

        
        - v1_2

        
        - v1_3

        
        - v1_4

        
        - v2_1

        
        - v2_2

        
        - v2_3

        
        - v2_6

        
        - v2_9

        
        - v3_0

        
        - v3_1

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_satellite_aerosol_properties(algorithm: str, day: OneOrMore[str], month: OneOrMore[str], orbit: OneOrMore[str], sensor_on_satellite: str, time_aggregation: str, variable: OneOrMore[str], version: OneOrMore[str], year: OneOrMore[str]):
    return Collection_satellite_aerosol_properties.download(algorithm=algorithm, day=day, month=month, orbit=orbit, sensor_on_satellite=sensor_on_satellite, time_aggregation=time_aggregation, variable=variable, version=version, year=year)

