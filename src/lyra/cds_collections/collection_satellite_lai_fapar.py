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

class Collection_satellite_lai_fapar(Collection):
    collection_name = 'satellite-lai-fapar'
    valid_values = dict(
        horizontal_resolution = ['300m', '1km', '4km'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        nominal_day = ['03', '10', '13', '20', '21', '22', '23', '24', '28', '29', '30', '31'],
        product_version = ['v0', 'v1', 'v2', 'v3', 'v4'],
        satellite = ['proba', 'spot', 'noaa_7', 'noaa_9', 'noaa_11', 'noaa_14', 'noaa_16', 'noaa_17', 'sentinel_3'],
        sensor = ['avhrr', 'vgt', 'olci_and_slstr'],
        variable = ['fapar', 'lai'],
        year = ['1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'],
    )

    @Collection.wrapper
    def download(cls, horizontal_resolution: OneOrMore[str], month: OneOrMore[str], nominal_day: OneOrMore[str], product_version: str, satellite: OneOrMore[str], sensor: str, variable: OneOrMore[str], year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): 
        """
        Parameters
        ----------
        :param horizontal_resolution:
        :type horizontal_resolution: str

        **Valid values:**
        
        - 300m

        
        - 1km

        
        - 4km

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

        :param nominal_day:
        :type nominal_day: str

        **Valid values:**
        
        - 03

        
        - 10

        
        - 13

        
        - 20

        
        - 21

        
        - 22

        
        - 23

        
        - 24

        
        - 28

        
        - 29

        
        - 30

        
        - 31

        ---

        :param product_version:
        :type product_version: str

        **Valid values:**
        
        - v0

        
        - v1

        
        - v2

        
        - v3

        
        - v4

        ---

        :param satellite:
        :type satellite: str

        **Valid values:**
        
        - proba

        
        - spot

        
        - noaa_7

        
        - noaa_9

        
        - noaa_11

        
        - noaa_14

        
        - noaa_16

        
        - noaa_17

        
        - sentinel_3

        ---

        :param sensor:
        :type sensor: str

        **Valid values:**
        
        - avhrr

        
        - vgt

        
        - olci_and_slstr

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - fapar

        
        - lai

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

        ---

        :param area_group:
        :type area_group: str

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_satellite_lai_fapar(horizontal_resolution: OneOrMore[str], month: OneOrMore[str], nominal_day: OneOrMore[str], product_version: str, satellite: OneOrMore[str], sensor: str, variable: OneOrMore[str], year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
    return Collection_satellite_lai_fapar.download(horizontal_resolution=horizontal_resolution, month=month, nominal_day=nominal_day, product_version=product_version, satellite=satellite, sensor=sensor, variable=variable, year=year, area_group=area_group)

