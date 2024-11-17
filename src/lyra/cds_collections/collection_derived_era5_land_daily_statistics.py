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

class Collection_derived_era5_land_daily_statistics(Collection):
    collection_name = 'derived-era5-land-daily-statistics'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        variable = ['2m_dewpoint_temperature', '2m_temperature', 'skin_temperature', 'soil_temperature_level_1', 'soil_temperature_level_2', 'soil_temperature_level_3', 'soil_temperature_level_4', 'lake_bottom_temperature', 'lake_ice_depth', 'lake_ice_temperature', 'lake_mix_layer_depth', 'lake_mix_layer_temperature', 'lake_shape_factor', 'lake_total_layer_temperature', 'snow_albedo', 'snow_cover', 'snow_density', 'snow_depth', 'snow_depth_water_equivalent', 'temperature_of_snow_layer', 'skin_reservoir_content', 'volumetric_soil_water_layer_1', 'volumetric_soil_water_layer_2', 'volumetric_soil_water_layer_3', 'volumetric_soil_water_layer_4', '10m_u_component_of_wind', '10m_v_component_of_wind', 'surface_pressure', 'leaf_area_index_high_vegetation', 'leaf_area_index_low_vegetation', 'forecast_albedo'],
        year = ['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        daily_statistic = ['daily_mean', 'daily_minimum', 'daily_maximum'],
        frequency = ['1_hourly', '3_hourly', '6_hourly'],
        time_zone = ['utc-12:00', 'utc-11:00', 'utc-10:00', 'utc-09:00', 'utc-08:00', 'utc-07:00', 'utc-06:00', 'utc-05:00', 'utc-04:00', 'utc-03:00', 'utc-02:00', 'utc-01:00', 'utc+00:00', 'utc+01:00', 'utc+02:00', 'utc+03:00', 'utc+04:00', 'utc+05:00', 'utc+06:00', 'utc+07:00', 'utc+08:00', 'utc+09:00', 'utc+10:00', 'utc+11:00', 'utc+12:00', 'utc+13:00', 'utc+14:00'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], month: str, variable: OneOrMore[str], year: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global', daily_statistic: str = 'daily_mean', frequency: str = '1_hourly', time_zone: str = 'utc+00:00'): 
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

        
        - temperature_of_snow_layer

        
        - skin_reservoir_content

        
        - volumetric_soil_water_layer_1

        
        - volumetric_soil_water_layer_2

        
        - volumetric_soil_water_layer_3

        
        - volumetric_soil_water_layer_4

        
        - 10m_u_component_of_wind

        
        - 10m_v_component_of_wind

        
        - surface_pressure

        
        - leaf_area_index_high_vegetation

        
        - leaf_area_index_low_vegetation

        
        - forecast_albedo

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

        :param daily_statistic:
        :type daily_statistic: str

        **Valid values:**
        
        - daily_mean

        
        - daily_minimum

        
        - daily_maximum

        ---

        :param frequency:
        :type frequency: str

        **Valid values:**
        
        - 1_hourly

        
        - 3_hourly

        
        - 6_hourly

        ---

        :param time_zone:
        :type time_zone: str

        **Valid values:**
        
        - utc-12:00

        
        - utc-11:00

        
        - utc-10:00

        
        - utc-09:00

        
        - utc-08:00

        
        - utc-07:00

        
        - utc-06:00

        
        - utc-05:00

        
        - utc-04:00

        
        - utc-03:00

        
        - utc-02:00

        
        - utc-01:00

        
        - utc+00:00

        
        - utc+01:00

        
        - utc+02:00

        
        - utc+03:00

        
        - utc+04:00

        
        - utc+05:00

        
        - utc+06:00

        
        - utc+07:00

        
        - utc+08:00

        
        - utc+09:00

        
        - utc+10:00

        
        - utc+11:00

        
        - utc+12:00

        
        - utc+13:00

        
        - utc+14:00

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_derived_era5_land_daily_statistics(day: OneOrMore[str], month: str, variable: OneOrMore[str], year: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global', daily_statistic: str = 'daily_mean', frequency: str = '1_hourly', time_zone: str = 'utc+00:00'):
    return Collection_derived_era5_land_daily_statistics.download(day=day, month=month, variable=variable, year=year, area_group=area_group, daily_statistic=daily_statistic, frequency=frequency, time_zone=time_zone)

