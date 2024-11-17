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

class Collection_seasonal_monthly_ocean(Collection):
    collection_name = 'seasonal-monthly-ocean'
    valid_values = dict(
        forecast_type = ['forecast', 'hindcast'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        originating_centre = ['ecmwf', 'ukmo', 'meteo_france', 'dwd', 'cmcc'],
        system = ['8', '21', '35', '51', '602', '603'],
        variable = ['mixed_layer_depth_0_01', 'sea_ice_thickness', 'depth_average_salinity_of_upper_300m', 'depth_average_potential_temperature_of_upper_300m', 'mixed_layer_depth_0_03', 'sea_surface_salinity', 'depth_of_14_c_isotherm', 'depth_of_17_c_isotherm', 'depth_of_20_c_isotherm', 'depth_of_26_c_isotherm', 'depth_of_28_c_isotherm', 'sea_surface_height_above_geoid'],
        year = ['1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2023', '2024'],
    )

    @Collection.wrapper
    def download(cls, forecast_type: OneOrMore[str], month: OneOrMore[str], originating_centre: str, system: str, variable: OneOrMore[str], year: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param forecast_type:
        :type forecast_type: str

        **Valid values:**
        
        - forecast

        
        - hindcast

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

        :param originating_centre:
        :type originating_centre: str

        **Valid values:**
        
        - ecmwf

        
        - ukmo

        
        - meteo_france

        
        - dwd

        
        - cmcc

        ---

        :param system:
        :type system: str

        **Valid values:**
        
        - 8

        
        - 21

        
        - 35

        
        - 51

        
        - 602

        
        - 603

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - mixed_layer_depth_0_01

        
        - sea_ice_thickness

        
        - depth_average_salinity_of_upper_300m

        
        - depth_average_potential_temperature_of_upper_300m

        
        - mixed_layer_depth_0_03

        
        - sea_surface_salinity

        
        - depth_of_14_c_isotherm

        
        - depth_of_17_c_isotherm

        
        - depth_of_20_c_isotherm

        
        - depth_of_26_c_isotherm

        
        - depth_of_28_c_isotherm

        
        - sea_surface_height_above_geoid

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

        
        - 2023

        
        - 2024

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_seasonal_monthly_ocean(forecast_type: OneOrMore[str], month: OneOrMore[str], originating_centre: str, system: str, variable: OneOrMore[str], year: OneOrMore[str]):
    return Collection_seasonal_monthly_ocean.download(forecast_type=forecast_type, month=month, originating_centre=originating_centre, system=system, variable=variable, year=year)

