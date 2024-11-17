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

class Collection_satellite_sea_ice_edge_type(Collection):
    collection_name = 'satellite-sea-ice-edge-type'
    valid_values = dict(
        cdr_type = ['cdr', 'icdr'],
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        region = ['northern_hemisphere', 'southern_hemisphere'],
        variable = ['sea_ice_edge', 'sea_ice_type'],
        year = ['1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        version = ['1_0', '2_0', '3_0'],
    )

    @Collection.wrapper
    def download(cls, cdr_type: str, day: OneOrMore[str], month: OneOrMore[str], region: str, variable: OneOrMore[str], year: OneOrMore[str], version: str = '3_0'): 
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

        :param region:
        :type region: str

        **Valid values:**
        
        - northern_hemisphere

        
        - southern_hemisphere

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - sea_ice_edge

        
        - sea_ice_type

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

        :param version:
        :type version: str

        **Valid values:**
        
        - 1_0

        
        - 2_0

        
        - 3_0

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_satellite_sea_ice_edge_type(cdr_type: str, day: OneOrMore[str], month: OneOrMore[str], region: str, variable: OneOrMore[str], year: OneOrMore[str], version: str = '3_0'):
    return Collection_satellite_sea_ice_edge_type.download(cdr_type=cdr_type, day=day, month=month, region=region, variable=variable, year=year, version=version)

