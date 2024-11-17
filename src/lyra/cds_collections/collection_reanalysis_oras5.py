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

class Collection_reanalysis_oras5(Collection):
    collection_name = 'reanalysis-oras5'
    valid_values = dict(
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        product_type = ['consolidated', 'operational'],
        variable = ['depth_of_14_c_isotherm', 'depth_of_17_c_isotherm', 'depth_of_20_c_isotherm', 'depth_of_26_c_isotherm', 'depth_of_28_c_isotherm', 'meridional_velocity', 'meridional_wind_stress', 'mixed_layer_depth_0_01', 'mixed_layer_depth_0_03', 'net_downward_heat_flux', 'net_upward_water_flux', 'ocean_heat_content_for_the_total_water_column', 'ocean_heat_content_for_the_upper_300m', 'ocean_heat_content_for_the_upper_700m', 'potential_temperature', 'rotated_meridional_velocity', 'rotated_zonal_velocity', 'salinity', 'sea_ice_concentration', 'sea_ice_meridional_velocity', 'sea_ice_thickness', 'sea_ice_zonal_velocity', 'sea_surface_height', 'sea_surface_salinity', 'sea_surface_temperature', 'zonal_velocity', 'zonal_wind_stress'],
        vertical_resolution = ['single_level', 'all_levels'],
        year = ['1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
    )

    @Collection.wrapper
    def download(cls, month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], vertical_resolution: str, year: OneOrMore[str]): 
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

        :param product_type:
        :type product_type: str

        **Valid values:**
        
        - consolidated

        
        - operational

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - depth_of_14_c_isotherm

        
        - depth_of_17_c_isotherm

        
        - depth_of_20_c_isotherm

        
        - depth_of_26_c_isotherm

        
        - depth_of_28_c_isotherm

        
        - meridional_velocity

        
        - meridional_wind_stress

        
        - mixed_layer_depth_0_01

        
        - mixed_layer_depth_0_03

        
        - net_downward_heat_flux

        
        - net_upward_water_flux

        
        - ocean_heat_content_for_the_total_water_column

        
        - ocean_heat_content_for_the_upper_300m

        
        - ocean_heat_content_for_the_upper_700m

        
        - potential_temperature

        
        - rotated_meridional_velocity

        
        - rotated_zonal_velocity

        
        - salinity

        
        - sea_ice_concentration

        
        - sea_ice_meridional_velocity

        
        - sea_ice_thickness

        
        - sea_ice_zonal_velocity

        
        - sea_surface_height

        
        - sea_surface_salinity

        
        - sea_surface_temperature

        
        - zonal_velocity

        
        - zonal_wind_stress

        ---

        :param vertical_resolution:
        :type vertical_resolution: str

        **Valid values:**
        
        - single_level

        
        - all_levels

        ---

        :param year:
        :type year: str

        **Valid values:**
        
        - 1958

        
        - 1959

        
        - 1960

        
        - 1961

        
        - 1962

        
        - 1963

        
        - 1964

        
        - 1965

        
        - 1966

        
        - 1967

        
        - 1968

        
        - 1969

        
        - 1970

        
        - 1971

        
        - 1972

        
        - 1973

        
        - 1974

        
        - 1975

        
        - 1976

        
        - 1977

        
        - 1978

        
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

def download_reanalysis_oras5(month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], vertical_resolution: str, year: OneOrMore[str]):
    return Collection_reanalysis_oras5.download(month=month, product_type=product_type, variable=variable, vertical_resolution=vertical_resolution, year=year)

