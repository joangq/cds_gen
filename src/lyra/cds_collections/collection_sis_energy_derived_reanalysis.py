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

class Collection_sis_energy_derived_reanalysis(Collection):
    collection_name = 'sis-energy-derived-reanalysis'
    valid_values = dict(
        energy_product_type = ['capacity_factor_ratio', 'energy', 'power'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        spatial_aggregation = ['original_grid', 'country_level', 'sub_country_level', 'maritime_country_level', 'maritime_sub_country_level'],
        temporal_aggregation = ['hourly', 'daily', 'monthly', 'seasonal', 'annual'],
        variable = ['wind_speed_at_100m', 'wind_speed_at_10m', 'surface_downwelling_shortwave_radiation', 'pressure_at_sea_level', '2m_air_temperature', 'total_precipitation', 'electricity_demand', 'hydro_power_generation_reservoirs', 'hydro_power_generation_rivers', 'solar_photovoltaic_power_generation', 'wind_power_generation_offshore', 'wind_power_generation_onshore'],
        year = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
    )

    @Collection.wrapper
    def download(cls, energy_product_type: OneOrMore[str], month: OneOrMore[str], spatial_aggregation: OneOrMore[str], temporal_aggregation: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param energy_product_type:
        :type energy_product_type: str

        **Valid values:**
        
        - capacity_factor_ratio

        
        - energy

        
        - power

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

        :param spatial_aggregation:
        :type spatial_aggregation: str

        **Valid values:**
        
        - original_grid

        
        - country_level

        
        - sub_country_level

        
        - maritime_country_level

        
        - maritime_sub_country_level

        ---

        :param temporal_aggregation:
        :type temporal_aggregation: str

        **Valid values:**
        
        - hourly

        
        - daily

        
        - monthly

        
        - seasonal

        
        - annual

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - wind_speed_at_100m

        
        - wind_speed_at_10m

        
        - surface_downwelling_shortwave_radiation

        
        - pressure_at_sea_level

        
        - 2m_air_temperature

        
        - total_precipitation

        
        - electricity_demand

        
        - hydro_power_generation_reservoirs

        
        - hydro_power_generation_rivers

        
        - solar_photovoltaic_power_generation

        
        - wind_power_generation_offshore

        
        - wind_power_generation_onshore

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

def download_sis_energy_derived_reanalysis(energy_product_type: OneOrMore[str], month: OneOrMore[str], spatial_aggregation: OneOrMore[str], temporal_aggregation: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str]):
    return Collection_sis_energy_derived_reanalysis.download(energy_product_type=energy_product_type, month=month, spatial_aggregation=spatial_aggregation, temporal_aggregation=temporal_aggregation, variable=variable, year=year)

