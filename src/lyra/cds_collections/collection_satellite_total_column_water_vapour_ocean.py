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

class Collection_satellite_total_column_water_vapour_ocean(Collection):
    collection_name = 'satellite-total-column-water-vapour-ocean'
    valid_values = dict(
        climate_data_record_type = ['icdr', 'tcdr'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        origin = ['c3s', 'eumetsat'],
        temporal_aggregation = ['monthly', '6_hourly'],
        year = ['1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'],
        variable = ['all'],
    )

    @Collection.wrapper
    def download(cls, climate_data_record_type: str, month: OneOrMore[str], origin: str, temporal_aggregation: str, year: OneOrMore[str], variable: str = 'all'): 
        """
        Parameters
        ----------
        :param climate_data_record_type:
        :type climate_data_record_type: str

        **Valid values:**
        
        - icdr

        
        - tcdr

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
        
        - c3s

        
        - eumetsat

        ---

        :param temporal_aggregation:
        :type temporal_aggregation: str

        **Valid values:**
        
        - monthly

        
        - 6_hourly

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

def download_satellite_total_column_water_vapour_ocean(climate_data_record_type: str, month: OneOrMore[str], origin: str, temporal_aggregation: str, year: OneOrMore[str], variable: str = 'all'):
    return Collection_satellite_total_column_water_vapour_ocean.download(climate_data_record_type=climate_data_record_type, month=month, origin=origin, temporal_aggregation=temporal_aggregation, year=year, variable=variable)

