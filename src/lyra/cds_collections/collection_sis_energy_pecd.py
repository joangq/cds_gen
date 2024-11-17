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

class Collection_sis_energy_pecd(Collection):
    collection_name = 'sis-energy-pecd'
    valid_values = dict(
        emissions = ['ssp2_4_5'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        origin = ['era5_reanalysis', 'cmcc_cm2_sr5', 'ec_earth3', 'mpi_esm1_2_hr'],
        spatial_resolution = ['0_25_degree', 'nuts_0', 'nuts_2', 'peof', 'peon', 'szof', 'szon'],
        technology = ['20', '21', '22', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43'],
        temporal_period = ['historical', 'future_projections'],
        variable = ['100m_wind_speed', '10m_wind_speed', '2m_temperature', 'population_weighted_temperature', 'surface_solar_radiation_downwards', 'total_precipitation', 'latitude_weights', 'nuts_0_regions_mask', 'nuts_2_regions_mask', 'peof_regions_mask', 'peon_regions_mask', 'population_density_mask', 'power_law_coefficients', 'solar_pv_mask', 'szof_regions_mask', 'szon_regions_mask', 'wind_power_regions_mask'],
        year = ['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057', '2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065'],
        pecd_version = ['pecd4_1'],
    )

    @Collection.wrapper
    def download(cls, emissions: OneOrMore[str], month: OneOrMore[str], origin: OneOrMore[str], spatial_resolution: OneOrMore[str], technology: OneOrMore[str], temporal_period: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], area: Optional[str] = None, area_group: Union[GeographicExtentType, FreeEditionType] = 'global', pecd_version: str = 'pecd4_1'): 
        """
        Parameters
        ----------
        :param emissions:
        :type emissions: str

        **Valid values:**
        
        - ssp2_4_5

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
        
        - era5_reanalysis

        
        - cmcc_cm2_sr5

        
        - ec_earth3

        
        - mpi_esm1_2_hr

        ---

        :param spatial_resolution:
        :type spatial_resolution: str

        **Valid values:**
        
        - 0_25_degree

        
        - nuts_0

        
        - nuts_2

        
        - peof

        
        - peon

        
        - szof

        
        - szon

        ---

        :param technology:
        :type technology: str

        **Valid values:**
        
        - 20

        
        - 21

        
        - 22

        
        - 30

        
        - 31

        
        - 32

        
        - 33

        
        - 34

        
        - 35

        
        - 36

        
        - 37

        
        - 38

        
        - 39

        
        - 40

        
        - 41

        
        - 42

        
        - 43

        ---

        :param temporal_period:
        :type temporal_period: str

        **Valid values:**
        
        - historical

        
        - future_projections

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - 100m_wind_speed

        
        - 10m_wind_speed

        
        - 2m_temperature

        
        - population_weighted_temperature

        
        - surface_solar_radiation_downwards

        
        - total_precipitation

        
        - latitude_weights

        
        - nuts_0_regions_mask

        
        - nuts_2_regions_mask

        
        - peof_regions_mask

        
        - peon_regions_mask

        
        - population_density_mask

        
        - power_law_coefficients

        
        - solar_pv_mask

        
        - szof_regions_mask

        
        - szon_regions_mask

        
        - wind_power_regions_mask

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

        
        - 2025

        
        - 2026

        
        - 2027

        
        - 2028

        
        - 2029

        
        - 2030

        
        - 2031

        
        - 2032

        
        - 2033

        
        - 2034

        
        - 2035

        
        - 2036

        
        - 2037

        
        - 2038

        
        - 2039

        
        - 2040

        
        - 2041

        
        - 2042

        
        - 2043

        
        - 2044

        
        - 2045

        
        - 2046

        
        - 2047

        
        - 2048

        
        - 2049

        
        - 2050

        
        - 2051

        
        - 2052

        
        - 2053

        
        - 2054

        
        - 2055

        
        - 2056

        
        - 2057

        
        - 2058

        
        - 2059

        
        - 2060

        
        - 2061

        
        - 2062

        
        - 2063

        
        - 2064

        
        - 2065

        ---

        :param area:
        :type area: str

        ---

        :param area_group:
        :type area_group: str

        ---

        :param pecd_version:
        :type pecd_version: str

        **Valid values:**
        
        - pecd4_1

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_energy_pecd(emissions: OneOrMore[str], month: OneOrMore[str], origin: OneOrMore[str], spatial_resolution: OneOrMore[str], technology: OneOrMore[str], temporal_period: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], area: Optional[str] = None, area_group: Union[GeographicExtentType, FreeEditionType] = 'global', pecd_version: str = 'pecd4_1'):
    return Collection_sis_energy_pecd.download(emissions=emissions, month=month, origin=origin, spatial_resolution=spatial_resolution, technology=technology, temporal_period=temporal_period, variable=variable, year=year, area=area, area_group=area_group, pecd_version=pecd_version)

