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

class Collection_seasonal_postprocessed_pressure_levels(Collection):
    collection_name = 'seasonal-postprocessed-pressure-levels'
    valid_values = dict(
        leadtime_month = ['1', '2', '3', '4', '5', '6'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        originating_centre = ['ecmwf', 'ukmo', 'meteo_france', 'dwd', 'cmcc', 'ncep', 'jma', 'eccc'],
        pressure_level = ['10', '30', '50', '100', '200', '300', '400', '500', '700', '850', '925', '1000'],
        product_type = ['ensemble_mean', 'monthly_mean'],
        system = ['1', '2', '3', '4', '5', '6', '7', '8', '12', '13', '14', '15', '21', '35', '51', '600', '601', '602', '603'],
        variable = ['geopotential_anomaly', 'specific_humidity_anomaly', 'temperature_anomaly', 'u_component_of_wind_anomaly', 'v_component_of_wind_anomaly'],
        year = ['2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        data_format = ['grib', 'netcdf'],
    )

    @Collection.wrapper
    def download(cls, leadtime_month: OneOrMore[str], month: OneOrMore[str], originating_centre: str, pressure_level: OneOrMore[str], product_type: OneOrMore[str], system: str, variable: OneOrMore[str], year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global', data_format: str = 'grib'): 
        """
        Parameters
        ----------
        :param leadtime_month:
        :type leadtime_month: str

        **Valid values:**
        
        - 1

        
        - 2

        
        - 3

        
        - 4

        
        - 5

        
        - 6

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

        
        - ncep

        
        - jma

        
        - eccc

        ---

        :param pressure_level:
        :type pressure_level: str

        **Valid values:**
        
        - 10

        
        - 30

        
        - 50

        
        - 100

        
        - 200

        
        - 300

        
        - 400

        
        - 500

        
        - 700

        
        - 850

        
        - 925

        
        - 1000

        ---

        :param product_type:
        :type product_type: str

        **Valid values:**
        
        - ensemble_mean

        
        - monthly_mean

        ---

        :param system:
        :type system: str

        **Valid values:**
        
        - 1

        
        - 2

        
        - 3

        
        - 4

        
        - 5

        
        - 6

        
        - 7

        
        - 8

        
        - 12

        
        - 13

        
        - 14

        
        - 15

        
        - 21

        
        - 35

        
        - 51

        
        - 600

        
        - 601

        
        - 602

        
        - 603

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - geopotential_anomaly

        
        - specific_humidity_anomaly

        
        - temperature_anomaly

        
        - u_component_of_wind_anomaly

        
        - v_component_of_wind_anomaly

        ---

        :param year:
        :type year: str

        **Valid values:**
        
        - 2017

        
        - 2018

        
        - 2019

        
        - 2020

        
        - 2021

        
        - 2022

        
        - 2023

        
        - 2024

        ---

        :param area_group:
        :type area_group: str

        ---

        :param data_format:
        :type data_format: str

        **Valid values:**
        
        - grib

        
        - netcdf

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_seasonal_postprocessed_pressure_levels(leadtime_month: OneOrMore[str], month: OneOrMore[str], originating_centre: str, pressure_level: OneOrMore[str], product_type: OneOrMore[str], system: str, variable: OneOrMore[str], year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global', data_format: str = 'grib'):
    return Collection_seasonal_postprocessed_pressure_levels.download(leadtime_month=leadtime_month, month=month, originating_centre=originating_centre, pressure_level=pressure_level, product_type=product_type, system=system, variable=variable, year=year, area_group=area_group, data_format=data_format)

