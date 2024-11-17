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

class Collection_sis_water_level_change_timeseries_cmip6(Collection):
    collection_name = 'sis-water-level-change-timeseries-cmip6'
    valid_values = dict(
        experiment = ['future', 'historical', 'reanalysis'],
        model = ['cmcc_cm2_vhr4', 'ec_earth3p_hr', 'gfdl_cm4c192_sst', 'hadgem3_gc31_hm', 'hadgem3_gc31_hm_sst'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        temporal_aggregation = ['10_min', 'daily_maximum', 'hourly', 'annual'],
        variable = ['mean_sea_level', 'storm_surge_residual', 'tidal_elevation', 'total_water_level'],
        year = ['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050'],
    )

    @Collection.wrapper
    def download(cls, experiment: str, model: OneOrMore[str], month: OneOrMore[str], temporal_aggregation: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param experiment:
        :type experiment: str

        **Valid values:**
        
        - future

        
        - historical

        
        - reanalysis

        ---

        :param model:
        :type model: str

        **Valid values:**
        
        - cmcc_cm2_vhr4

        
        - ec_earth3p_hr

        
        - gfdl_cm4c192_sst

        
        - hadgem3_gc31_hm

        
        - hadgem3_gc31_hm_sst

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

        :param temporal_aggregation:
        :type temporal_aggregation: str

        **Valid values:**
        
        - 10_min

        
        - daily_maximum

        
        - hourly

        
        - annual

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - mean_sea_level

        
        - storm_surge_residual

        
        - tidal_elevation

        
        - total_water_level

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

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_water_level_change_timeseries_cmip6(experiment: str, model: OneOrMore[str], month: OneOrMore[str], temporal_aggregation: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str]):
    return Collection_sis_water_level_change_timeseries_cmip6.download(experiment=experiment, model=model, month=month, temporal_aggregation=temporal_aggregation, variable=variable, year=year)

