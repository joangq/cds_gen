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

class Collection_reanalysis_era5_land(Collection):
    collection_name = 'reanalysis-era5-land'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        time = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'],
        variable = ['2m_dewpoint_temperature', '2m_temperature', 'skin_temperature', 'soil_temperature_level_1', 'soil_temperature_level_2', 'soil_temperature_level_3', 'soil_temperature_level_4', 'lake_bottom_temperature', 'lake_ice_depth', 'lake_ice_temperature', 'lake_mix_layer_depth', 'lake_mix_layer_temperature', 'lake_shape_factor', 'lake_total_layer_temperature', 'snow_albedo', 'snow_cover', 'snow_density', 'snow_depth', 'snow_depth_water_equivalent', 'snowfall', 'snowmelt', 'temperature_of_snow_layer', 'skin_reservoir_content', 'volumetric_soil_water_layer_1', 'volumetric_soil_water_layer_2', 'volumetric_soil_water_layer_3', 'volumetric_soil_water_layer_4', 'forecast_albedo', 'surface_latent_heat_flux', 'surface_net_solar_radiation', 'surface_net_thermal_radiation', 'surface_sensible_heat_flux', 'surface_solar_radiation_downwards', 'surface_thermal_radiation_downwards', 'evaporation_from_bare_soil', 'evaporation_from_open_water_surfaces_excluding_oceans', 'evaporation_from_the_top_of_canopy', 'evaporation_from_vegetation_transpiration', 'potential_evaporation', 'runoff', 'snow_evaporation', 'sub_surface_runoff', 'surface_runoff', 'total_evaporation', '10m_u_component_of_wind', '10m_v_component_of_wind', 'surface_pressure', 'total_precipitation', 'leaf_area_index_high_vegetation', 'leaf_area_index_low_vegetation'],
        year = ['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        data_format = ['grib', 'netcdf'],
        download_format = ['unarchived', 'zip'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], month: str, time: OneOrMore[str], variable: OneOrMore[str], year: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global', data_format: str = 'grib', download_format: str = 'unarchived'): 
        """
        Parameters
        ----------
        :param day:
        :type day: str

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

        
        - 13

        
        - 14

        
        - 15

        
        - 16

        
        - 17

        
        - 18

        
        - 19

        
        - 20

        
        - 21

        
        - 22

        
        - 23

        
        - 24

        
        - 25

        
        - 26

        
        - 27

        
        - 28

        
        - 29

        
        - 30

        
        - 31

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

        :param time:
        :type time: str

        **Valid values:**
        
        - 00:00

        
        - 01:00

        
        - 02:00

        
        - 03:00

        
        - 04:00

        
        - 05:00

        
        - 06:00

        
        - 07:00

        
        - 08:00

        
        - 09:00

        
        - 10:00

        
        - 11:00

        
        - 12:00

        
        - 13:00

        
        - 14:00

        
        - 15:00

        
        - 16:00

        
        - 17:00

        
        - 18:00

        
        - 19:00

        
        - 20:00

        
        - 21:00

        
        - 22:00

        
        - 23:00

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - 2m_dewpoint_temperature

        
        - 2m_temperature

        
        - skin_temperature

        
        - soil_temperature_level_1

        
        - soil_temperature_level_2

        
        - soil_temperature_level_3

        
        - soil_temperature_level_4

        
        - lake_bottom_temperature

        
        - lake_ice_depth

        
        - lake_ice_temperature

        
        - lake_mix_layer_depth

        
        - lake_mix_layer_temperature

        
        - lake_shape_factor

        
        - lake_total_layer_temperature

        
        - snow_albedo

        
        - snow_cover

        
        - snow_density

        
        - snow_depth

        
        - snow_depth_water_equivalent

        
        - snowfall

        
        - snowmelt

        
        - temperature_of_snow_layer

        
        - skin_reservoir_content

        
        - volumetric_soil_water_layer_1

        
        - volumetric_soil_water_layer_2

        
        - volumetric_soil_water_layer_3

        
        - volumetric_soil_water_layer_4

        
        - forecast_albedo

        
        - surface_latent_heat_flux

        
        - surface_net_solar_radiation

        
        - surface_net_thermal_radiation

        
        - surface_sensible_heat_flux

        
        - surface_solar_radiation_downwards

        
        - surface_thermal_radiation_downwards

        
        - evaporation_from_bare_soil

        
        - evaporation_from_open_water_surfaces_excluding_oceans

        
        - evaporation_from_the_top_of_canopy

        
        - evaporation_from_vegetation_transpiration

        
        - potential_evaporation

        
        - runoff

        
        - snow_evaporation

        
        - sub_surface_runoff

        
        - surface_runoff

        
        - total_evaporation

        
        - 10m_u_component_of_wind

        
        - 10m_v_component_of_wind

        
        - surface_pressure

        
        - total_precipitation

        
        - leaf_area_index_high_vegetation

        
        - leaf_area_index_low_vegetation

        ---

        :param year:
        :type year: str

        **Valid values:**
        
        - 1950

        
        - 1951

        
        - 1952

        
        - 1953

        
        - 1954

        
        - 1955

        
        - 1956

        
        - 1957

        
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

        :param area_group:
        :type area_group: str

        ---

        :param data_format:
        :type data_format: str

        **Valid values:**
        
        - grib

        
        - netcdf

        ---

        :param download_format:
        :type download_format: str

        **Valid values:**
        
        - unarchived

        
        - zip

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_reanalysis_era5_land(day: OneOrMore[str], month: str, time: OneOrMore[str], variable: OneOrMore[str], year: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global', data_format: str = 'grib', download_format: str = 'unarchived'):
    return Collection_reanalysis_era5_land.download(day=day, month=month, time=time, variable=variable, year=year, area_group=area_group, data_format=data_format, download_format=download_format)

