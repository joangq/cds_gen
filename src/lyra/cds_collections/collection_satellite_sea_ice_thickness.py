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

class Collection_satellite_sea_ice_thickness(Collection):
    collection_name = 'satellite-sea-ice-thickness'
    valid_values = dict(
        cdr_type = ['cdr', 'icdr'],
        month = ['01', '02', '03', '04', '10', '11', '12'],
        satellite = ['envisat', 'cryosat_2'],
        year = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        variable = ['all'],
        version = ['1_0', '2_0', '3_0'],
    )

    @Collection.wrapper
    def download(cls, cdr_type: OneOrMore[str], month: OneOrMore[str], satellite: OneOrMore[str], year: OneOrMore[str], variable: str = 'all', version: str = '3_0'): 
        """
        Parameters
        ----------
        :param cdr_type:
        :type cdr_type: str

        **Valid values:**
        
        - cdr

        
        - icdr

        ---

        :param month:
        :type month: str

        **Valid values:**
        
        - 01

        
        - 02

        
        - 03

        
        - 04

        
        - 10

        
        - 11

        
        - 12

        ---

        :param satellite:
        :type satellite: str

        **Valid values:**
        
        - envisat

        
        - cryosat_2

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

        
        - 2023

        
        - 2024

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - all

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

def download_satellite_sea_ice_thickness(cdr_type: OneOrMore[str], month: OneOrMore[str], satellite: OneOrMore[str], year: OneOrMore[str], variable: str = 'all', version: str = '3_0'):
    return Collection_satellite_sea_ice_thickness.download(cdr_type=cdr_type, month=month, satellite=satellite, year=year, variable=variable, version=version)

