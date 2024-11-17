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

class Collection_satellite_ozone_v1(Collection):
    collection_name = 'satellite-ozone-v1'
    valid_values = dict(
        algorithm = ['ubr', 'usask'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        processing_level = ['level_3', 'level_4'],
        sensor = ['msr', 'merged_uv', 'merged_np', 'allg', 'cllg', 'amzm', 'cmzm', 'ace', 'gome', 'gome2_a', 'gome2_b', 'gome2_c', 'gomos', 'haloe', 'iasi_a_day_time', 'iasi_a_night_time', 'iasi_b_day_time', 'iasi_b_night_time', 'iasi_c_day_time', 'iasi_c_night_time', 'mipas', 'mls', 'omi', 'omps', 'osiris', 'saber', 'sage_2', 'sage_3', 'sciamachy', 'smr', 'tropomi'],
        variable = ['mole_concentration_of_ozone_in_air', 'mole_fraction_of_ozone_in_air', 'anomaly_of_mole_concentration_of_ozone_in_air', 'mole_content_of_ozone_in_atmosphere_layer', 'atmosphere_mole_content_of_ozone'],
        version = ['v0001', 'v0002', 'v0003', 'v0004', 'v0005', 'v0006', 'v0007', 'v0008', 'v0009', 'v0020', 'v0021', 'v0022', 'v0023', 'v0024', 'v0025', 'v0100', 'v0101', 'v0200', 'v0300', 'v0400', 'v0500', 'v0600', 'v0700', 'v0800', 'v0900', 'v1000', 'v1100', 'v2000'],
        vertical_aggregation = ['total_column', 'tropospheric_column_0_6_km', 'vertical_profiles_from_limb_sensors', 'vertical_profiles_from_nadir_sensors'],
        year = ['1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    )

    @Collection.wrapper
    def download(cls, algorithm: str, month: OneOrMore[str], processing_level: str, sensor: OneOrMore[str], variable: str, version: OneOrMore[str], vertical_aggregation: str, year: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param algorithm:
        :type algorithm: str

        **Valid values:**
        
        - ubr

        
        - usask

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
        
        - level_3

        
        - level_4

        ---

        :param sensor:
        :type sensor: str

        **Valid values:**
        
        - msr

        
        - merged_uv

        
        - merged_np

        
        - allg

        
        - cllg

        
        - amzm

        
        - cmzm

        
        - ace

        
        - gome

        
        - gome2_a

        
        - gome2_b

        
        - gome2_c

        
        - gomos

        
        - haloe

        
        - iasi_a_day_time

        
        - iasi_a_night_time

        
        - iasi_b_day_time

        
        - iasi_b_night_time

        
        - iasi_c_day_time

        
        - iasi_c_night_time

        
        - mipas

        
        - mls

        
        - omi

        
        - omps

        
        - osiris

        
        - saber

        
        - sage_2

        
        - sage_3

        
        - sciamachy

        
        - smr

        
        - tropomi

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - mole_concentration_of_ozone_in_air

        
        - mole_fraction_of_ozone_in_air

        
        - anomaly_of_mole_concentration_of_ozone_in_air

        
        - mole_content_of_ozone_in_atmosphere_layer

        
        - atmosphere_mole_content_of_ozone

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - v0001

        
        - v0002

        
        - v0003

        
        - v0004

        
        - v0005

        
        - v0006

        
        - v0007

        
        - v0008

        
        - v0009

        
        - v0020

        
        - v0021

        
        - v0022

        
        - v0023

        
        - v0024

        
        - v0025

        
        - v0100

        
        - v0101

        
        - v0200

        
        - v0300

        
        - v0400

        
        - v0500

        
        - v0600

        
        - v0700

        
        - v0800

        
        - v0900

        
        - v1000

        
        - v1100

        
        - v2000

        ---

        :param vertical_aggregation:
        :type vertical_aggregation: str

        **Valid values:**
        
        - total_column

        
        - tropospheric_column_0_6_km

        
        - vertical_profiles_from_limb_sensors

        
        - vertical_profiles_from_nadir_sensors

        ---

        :param year:
        :type year: str

        **Valid values:**
        
        - 1970

        
        - 1971

        
        - 1972

        
        - 1973

        
        - 1974

        
        - 1975

        
        - 1976

        
        - 1977

        
        - 1978

        
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

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_satellite_ozone_v1(algorithm: str, month: OneOrMore[str], processing_level: str, sensor: OneOrMore[str], variable: str, version: OneOrMore[str], vertical_aggregation: str, year: OneOrMore[str]):
    return Collection_satellite_ozone_v1.download(algorithm=algorithm, month=month, processing_level=processing_level, sensor=sensor, variable=variable, version=version, vertical_aggregation=vertical_aggregation, year=year)

