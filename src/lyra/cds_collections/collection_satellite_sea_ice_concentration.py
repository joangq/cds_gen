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

class Collection_satellite_sea_ice_concentration(Collection):
    collection_name = 'satellite-sea-ice-concentration'
    valid_values = dict(
        cdr_type = ['cdr', 'icdr'],
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        origin = ['esa_cci', 'eumetsat_osi_saf'],
        region = ['northern_hemisphere', 'southern_hemisphere'],
        sensor = ['ssmis', 'amsr'],
        temporal_aggregation = ['daily', 'monthly'],
        version = ['v2', 'v3'],
        year = ['1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        variable = ['all'],
    )

    @Collection.wrapper
    def download(cls, cdr_type: OneOrMore[str], day: OneOrMore[str], month: OneOrMore[str], origin: str, region: OneOrMore[str], sensor: str, temporal_aggregation: str, version: str, year: OneOrMore[str], variable: str = 'all'): 
        """
        Parameters
        ----------
        :param cdr_type:
        :type cdr_type: str

        **Valid values:**
        
        - cdr

        
        - icdr

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

        :param origin:
        :type origin: str

        **Valid values:**
        
        - esa_cci

        
        - eumetsat_osi_saf

        ---

        :param region:
        :type region: str

        **Valid values:**
        
        - northern_hemisphere

        
        - southern_hemisphere

        ---

        :param sensor:
        :type sensor: str

        **Valid values:**
        
        - ssmis

        
        - amsr

        ---

        :param temporal_aggregation:
        :type temporal_aggregation: str

        **Valid values:**
        
        - daily

        
        - monthly

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - v2

        
        - v3

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

        
        - 2024

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

def download_satellite_sea_ice_concentration(cdr_type: OneOrMore[str], day: OneOrMore[str], month: OneOrMore[str], origin: str, region: OneOrMore[str], sensor: str, temporal_aggregation: str, version: str, year: OneOrMore[str], variable: str = 'all'):
    return Collection_satellite_sea_ice_concentration.download(cdr_type=cdr_type, day=day, month=month, origin=origin, region=region, sensor=sensor, temporal_aggregation=temporal_aggregation, version=version, year=year, variable=variable)

