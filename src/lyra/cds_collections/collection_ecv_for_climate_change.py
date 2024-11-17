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

class Collection_ecv_for_climate_change(Collection):
    collection_name = 'ecv-for-climate-change'
    valid_values = dict(
        climate_reference_period = ['1981_2010', '1991_2020'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        origin = ['era5', 'era5_land', 'era_interim'],
        product_type = ['anomaly', 'climatology', 'monthly_mean'],
        time_aggregation = ['1_month_mean', '12_month_running_mean'],
        variable = ['surface_air_temperature', 'surface_air_relative_humidity', '0_7cm_volumetric_soil_moisture', 'precipitation', 'sea_ice_cover'],
        year = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
    )

    @Collection.wrapper
    def download(cls, climate_reference_period: OneOrMore[str], month: OneOrMore[str], origin: OneOrMore[str], product_type: OneOrMore[str], time_aggregation: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param climate_reference_period:
        :type climate_reference_period: str

        **Valid values:**
        
        - 1981_2010

        
        - 1991_2020

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
        
        - era5

        
        - era5_land

        
        - era_interim

        ---

        :param product_type:
        :type product_type: str

        **Valid values:**
        
        - anomaly

        
        - climatology

        
        - monthly_mean

        ---

        :param time_aggregation:
        :type time_aggregation: str

        **Valid values:**
        
        - 1_month_mean

        
        - 12_month_running_mean

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - surface_air_temperature

        
        - surface_air_relative_humidity

        
        - 0_7cm_volumetric_soil_moisture

        
        - precipitation

        
        - sea_ice_cover

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_ecv_for_climate_change(climate_reference_period: OneOrMore[str], month: OneOrMore[str], origin: OneOrMore[str], product_type: OneOrMore[str], time_aggregation: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str]):
    return Collection_ecv_for_climate_change.download(climate_reference_period=climate_reference_period, month=month, origin=origin, product_type=product_type, time_aggregation=time_aggregation, variable=variable, year=year)

