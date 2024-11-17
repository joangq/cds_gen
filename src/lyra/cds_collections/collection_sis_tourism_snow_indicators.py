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

class Collection_sis_tourism_snow_indicators(Collection):
    collection_name = 'sis-tourism-snow-indicators'
    valid_values = dict(
        experiment = ['historical', 'rcp2_6', 'rcp4_5', 'rcp8_5', 'uerra_reanalysis'],
        gcm = ['mpi_esm_lr', 'cnrm_cm5', 'cm5a_mr', 'hadgem2_es', 'ec_earth'],
        period = ['1961_1990', '1986_2005', '1990_2015', '2021_2040', '2041_2060', '2081_2100'],
        rcm = ['cclm4_8_17', 'aladin53', 'wrf331f', 'remo2009', 'rca4'],
        statistic = ['10th_percentile', '20th_percentile', '50th_percentile', '80th_percentile', '90th_percentile', 'mean', 'standard_deviation'],
        time_aggregation = ['climatology', 'annual_data'],
        variable = ['start_of_the_longest_period_with_groomed_snow', 'start_of_the_longest_period_with_managed_snow', 'start_of_the_longest_period_with_natural_snow', 'end_of_the_longest_period_with_groomed_snow', 'end_of_the_longest_period_with_managed_snow', 'end_of_the_longest_period_with_natural_snow', 'annual_amount_of_machine_made_snow_produced', 'total_precipitation_from_november_to_april', 'total_snow_precipitation_from_november_to_april', 'period_with_medium_height_of_groomed_snow', 'period_with_medium_height_of_managed_snow', 'period_with_medium_height_of_natural_snow', 'period_with_low_height_of_groomed_snow', 'period_with_low_height_of_managed_snow', 'period_with_low_height_of_natural_snow', 'period_with_high_height_of_groomed_snow', 'period_with_high_height_of_managed_snow', 'period_with_high_height_of_natural_snow', 'period_with_medium_height_of_groomed_snow_between_fourth_and_tenth_december', 'period_with_medium_height_of_managed_snow_between_fourth_and_tenth_december', 'period_with_medium_height_of_natural_snow_between_fourth_and_tenth_december', 'period_with_medium_height_of_groomed_snow_between_twenty_second_december_and_fourth_january', 'period_with_medium_height_of_managed_snow_between_twenty_second_december_and_fourth_january', 'period_with_medium_height_of_natural_snow_between_twenty_second_december_and_fourth_january', 'period_with_medium_amount_of_groomed_snow', 'period_with_medium_amount_of_managed_snow', 'period_with_medium_amount_of_natural_snow', 'period_with_high_amount_of_groomed_snow', 'period_with_high_amount_of_managed_snow', 'period_with_high_amount_of_natural_snow', 'mean_winter_air_temperature', 'monthly_mean_air_temperature_for_november', 'monthly_mean_air_temperature_for_december', 'monthly_mean_air_temperature_for_january', 'monthly_mean_air_temperature_for_february', 'monthly_mean_air_temperature_for_march', 'monthly_mean_air_temperature_for_april', 'snow_making_hours_for_WBT_lower_than_negative_2_degc', 'snow_making_hours_for_WBT_lower_than_negative_5_degc'],
        version = ['1_0', '1_1'],
        year = ['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057', '2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065', '2066', '2067', '2068', '2069', '2070', '2071', '2072', '2073', '2074', '2075', '2076', '2077', '2078', '2079', '2080', '2081', '2082', '2083', '2084', '2085', '2086', '2087', '2088', '2089', '2090', '2091', '2092', '2093', '2094', '2095', '2096', '2097', '2098', '2099', '2100'],
    )

    @Collection.wrapper
    def download(cls, experiment: str, gcm: OneOrMore[str], period: OneOrMore[str], rcm: str, statistic: OneOrMore[str], time_aggregation: str, variable: OneOrMore[str], version: OneOrMore[str], year: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param experiment:
        :type experiment: str

        **Valid values:**
        
        - historical

        
        - rcp2_6

        
        - rcp4_5

        
        - rcp8_5

        
        - uerra_reanalysis

        ---

        :param gcm:
        :type gcm: str

        **Valid values:**
        
        - mpi_esm_lr

        
        - cnrm_cm5

        
        - cm5a_mr

        
        - hadgem2_es

        
        - ec_earth

        ---

        :param period:
        :type period: str

        **Valid values:**
        
        - 1961_1990

        
        - 1986_2005

        
        - 1990_2015

        
        - 2021_2040

        
        - 2041_2060

        
        - 2081_2100

        ---

        :param rcm:
        :type rcm: str

        **Valid values:**
        
        - cclm4_8_17

        
        - aladin53

        
        - wrf331f

        
        - remo2009

        
        - rca4

        ---

        :param statistic:
        :type statistic: str

        **Valid values:**
        
        - 10th_percentile

        
        - 20th_percentile

        
        - 50th_percentile

        
        - 80th_percentile

        
        - 90th_percentile

        
        - mean

        
        - standard_deviation

        ---

        :param time_aggregation:
        :type time_aggregation: str

        **Valid values:**
        
        - climatology

        
        - annual_data

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - start_of_the_longest_period_with_groomed_snow

        
        - start_of_the_longest_period_with_managed_snow

        
        - start_of_the_longest_period_with_natural_snow

        
        - end_of_the_longest_period_with_groomed_snow

        
        - end_of_the_longest_period_with_managed_snow

        
        - end_of_the_longest_period_with_natural_snow

        
        - annual_amount_of_machine_made_snow_produced

        
        - total_precipitation_from_november_to_april

        
        - total_snow_precipitation_from_november_to_april

        
        - period_with_medium_height_of_groomed_snow

        
        - period_with_medium_height_of_managed_snow

        
        - period_with_medium_height_of_natural_snow

        
        - period_with_low_height_of_groomed_snow

        
        - period_with_low_height_of_managed_snow

        
        - period_with_low_height_of_natural_snow

        
        - period_with_high_height_of_groomed_snow

        
        - period_with_high_height_of_managed_snow

        
        - period_with_high_height_of_natural_snow

        
        - period_with_medium_height_of_groomed_snow_between_fourth_and_tenth_december

        
        - period_with_medium_height_of_managed_snow_between_fourth_and_tenth_december

        
        - period_with_medium_height_of_natural_snow_between_fourth_and_tenth_december

        
        - period_with_medium_height_of_groomed_snow_between_twenty_second_december_and_fourth_january

        
        - period_with_medium_height_of_managed_snow_between_twenty_second_december_and_fourth_january

        
        - period_with_medium_height_of_natural_snow_between_twenty_second_december_and_fourth_january

        
        - period_with_medium_amount_of_groomed_snow

        
        - period_with_medium_amount_of_managed_snow

        
        - period_with_medium_amount_of_natural_snow

        
        - period_with_high_amount_of_groomed_snow

        
        - period_with_high_amount_of_managed_snow

        
        - period_with_high_amount_of_natural_snow

        
        - mean_winter_air_temperature

        
        - monthly_mean_air_temperature_for_november

        
        - monthly_mean_air_temperature_for_december

        
        - monthly_mean_air_temperature_for_january

        
        - monthly_mean_air_temperature_for_february

        
        - monthly_mean_air_temperature_for_march

        
        - monthly_mean_air_temperature_for_april

        
        - snow_making_hours_for_WBT_lower_than_negative_2_degc

        
        - snow_making_hours_for_WBT_lower_than_negative_5_degc

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - 1_0

        
        - 1_1

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

        
        - 2066

        
        - 2067

        
        - 2068

        
        - 2069

        
        - 2070

        
        - 2071

        
        - 2072

        
        - 2073

        
        - 2074

        
        - 2075

        
        - 2076

        
        - 2077

        
        - 2078

        
        - 2079

        
        - 2080

        
        - 2081

        
        - 2082

        
        - 2083

        
        - 2084

        
        - 2085

        
        - 2086

        
        - 2087

        
        - 2088

        
        - 2089

        
        - 2090

        
        - 2091

        
        - 2092

        
        - 2093

        
        - 2094

        
        - 2095

        
        - 2096

        
        - 2097

        
        - 2098

        
        - 2099

        
        - 2100

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_tourism_snow_indicators(experiment: str, gcm: OneOrMore[str], period: OneOrMore[str], rcm: str, statistic: OneOrMore[str], time_aggregation: str, variable: OneOrMore[str], version: OneOrMore[str], year: OneOrMore[str]):
    return Collection_sis_tourism_snow_indicators.download(experiment=experiment, gcm=gcm, period=period, rcm=rcm, statistic=statistic, time_aggregation=time_aggregation, variable=variable, version=version, year=year)

