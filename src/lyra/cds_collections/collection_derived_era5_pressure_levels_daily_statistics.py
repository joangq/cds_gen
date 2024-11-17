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

class Collection_derived_era5_pressure_levels_daily_statistics(Collection):
    collection_name = 'derived-era5-pressure-levels-daily-statistics'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        pressure_level = ['1', '2', '3', '5', '7', '10', '20', '30', '50', '70', '100', '125', '150', '175', '200', '225', '250', '300', '350', '400', '450', '500', '550', '600', '650', '700', '750', '775', '800', '825', '850', '875', '900', '925', '950', '975', '1000'],
        variable = ['divergence', 'fraction_of_cloud_cover', 'geopotential', 'ozone_mass_mixing_ratio', 'potential_vorticity', 'relative_humidity', 'specific_cloud_ice_water_content', 'specific_cloud_liquid_water_content', 'specific_humidity', 'specific_rain_water_content', 'specific_snow_water_content', 'temperature', 'u_component_of_wind', 'v_component_of_wind', 'vertical_velocity', 'vorticity'],
        year = ['1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        daily_statistic = ['daily_mean', 'daily_minimum', 'daily_maximum'],
        frequency = ['1_hourly', '3_hourly', '6_hourly'],
        product_type = ['reanalysis', 'ensemble_members', 'ensemble_mean'],
        time_zone = ['utc-12:00', 'utc-11:00', 'utc-10:00', 'utc-09:00', 'utc-08:00', 'utc-07:00', 'utc-06:00', 'utc-05:00', 'utc-04:00', 'utc-03:00', 'utc-02:00', 'utc-01:00', 'utc+00:00', 'utc+01:00', 'utc+02:00', 'utc+03:00', 'utc+04:00', 'utc+05:00', 'utc+06:00', 'utc+07:00', 'utc+08:00', 'utc+09:00', 'utc+10:00', 'utc+11:00', 'utc+12:00', 'utc+13:00', 'utc+14:00'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], month: OneOrMore[str], pressure_level: OneOrMore[str], variable: OneOrMore[str], year: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global', daily_statistic: str = 'daily_mean', frequency: str = '1_hourly', product_type: str = 'reanalysis', time_zone: str = 'utc+00:00'): 
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

        :param pressure_level:
        :type pressure_level: str

        **Valid values:**
        
        - 1

        
        - 2

        
        - 3

        
        - 5

        
        - 7

        
        - 10

        
        - 20

        
        - 30

        
        - 50

        
        - 70

        
        - 100

        
        - 125

        
        - 150

        
        - 175

        
        - 200

        
        - 225

        
        - 250

        
        - 300

        
        - 350

        
        - 400

        
        - 450

        
        - 500

        
        - 550

        
        - 600

        
        - 650

        
        - 700

        
        - 750

        
        - 775

        
        - 800

        
        - 825

        
        - 850

        
        - 875

        
        - 900

        
        - 925

        
        - 950

        
        - 975

        
        - 1000

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - divergence

        
        - fraction_of_cloud_cover

        
        - geopotential

        
        - ozone_mass_mixing_ratio

        
        - potential_vorticity

        
        - relative_humidity

        
        - specific_cloud_ice_water_content

        
        - specific_cloud_liquid_water_content

        
        - specific_humidity

        
        - specific_rain_water_content

        
        - specific_snow_water_content

        
        - temperature

        
        - u_component_of_wind

        
        - v_component_of_wind

        
        - vertical_velocity

        
        - vorticity

        ---

        :param year:
        :type year: str

        **Valid values:**
        
        - 1940

        
        - 1941

        
        - 1942

        
        - 1943

        
        - 1944

        
        - 1945

        
        - 1946

        
        - 1947

        
        - 1948

        
        - 1949

        
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

        :param product_type:
        :type product_type: str

        **Valid values:**
        
        - reanalysis

        
        - ensemble_members

        
        - ensemble_mean

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

def download_derived_era5_pressure_levels_daily_statistics(day: OneOrMore[str], month: OneOrMore[str], pressure_level: OneOrMore[str], variable: OneOrMore[str], year: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global', daily_statistic: str = 'daily_mean', frequency: str = '1_hourly', product_type: str = 'reanalysis', time_zone: str = 'utc+00:00'):
    return Collection_derived_era5_pressure_levels_daily_statistics.download(day=day, month=month, pressure_level=pressure_level, variable=variable, year=year, area_group=area_group, daily_statistic=daily_statistic, frequency=frequency, product_type=product_type, time_zone=time_zone)

