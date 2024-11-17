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

class Collection_satellite_fire_burned_area(Collection):
    collection_name = 'satellite-fire-burned-area'
    valid_values = dict(
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        nominal_day = ['01', '07', '22'],
        origin = ['c3s', 'esa_cci'],
        region = ['north_america', 'south_america', 'europe', 'asia', 'africa', 'australia'],
        sensor = ['modis', 'olci'],
        variable = ['grid_variables', 'pixel_variables'],
        version = ['5_1_1cds', '1_0', '1_1', '5_0cds', '5_1cds'],
        year = ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'],
    )

    @Collection.wrapper
    def download(cls, month: OneOrMore[str], nominal_day: OneOrMore[str], origin: str, region: OneOrMore[str], sensor: str, variable: str, version: str, year: OneOrMore[str]): 
        """
        Parameters
        ----------
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
        
        - 01

        
        - 07

        
        - 22

        ---

        :param origin:
        :type origin: str

        **Valid values:**
        
        - c3s

        
        - esa_cci

        ---

        :param region:
        :type region: str

        **Valid values:**
        
        - north_america

        
        - south_america

        
        - europe

        
        - asia

        
        - africa

        
        - australia

        ---

        :param sensor:
        :type sensor: str

        **Valid values:**
        
        - modis

        
        - olci

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - grid_variables

        
        - pixel_variables

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - 5_1_1cds

        
        - 1_0

        
        - 1_1

        
        - 5_0cds

        
        - 5_1cds

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_satellite_fire_burned_area(month: OneOrMore[str], nominal_day: OneOrMore[str], origin: str, region: OneOrMore[str], sensor: str, variable: str, version: str, year: OneOrMore[str]):
    return Collection_satellite_fire_burned_area.download(month=month, nominal_day=nominal_day, origin=origin, region=region, sensor=sensor, variable=variable, version=version, year=year)

