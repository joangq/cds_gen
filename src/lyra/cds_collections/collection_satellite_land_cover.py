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

class Collection_satellite_land_cover(Collection):
    collection_name = 'satellite-land-cover'
    valid_values = dict(
        version = ['v2_0_7cds', 'v2_1_1'],
        year = ['1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'],
        variable = ['all'],
    )

    @Collection.wrapper
    def download(cls, version: OneOrMore[str], year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global', variable: str = 'all'): 
        """
        Parameters
        ----------
        :param version:
        :type version: str

        **Valid values:**
        
        - v2_0_7cds

        
        - v2_1_1

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

        :param area_group:
        :type area_group: str

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

def download_satellite_land_cover(version: OneOrMore[str], year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global', variable: str = 'all'):
    return Collection_satellite_land_cover.download(version=version, year=year, area_group=area_group, variable=variable)

