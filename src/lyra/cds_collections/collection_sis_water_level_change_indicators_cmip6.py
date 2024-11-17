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

class Collection_sis_water_level_change_indicators_cmip6(Collection):
    collection_name = 'sis-water-level-change-indicators-cmip6'
    valid_values = dict(
        confidence_interval = ['best_fit', 'low_bound_confidence_interval', 'high_bound_confidence_interval'],
        derived_variable = ['absolute_change', 'absolute_value', 'percentage_change'],
        experiment = ['historical', 'future'],
        model = ['cmcc_cm2_vhr4', 'ec_earth3p_hr', 'hadgem3_gc31_hm', 'hadgem3_gc31_hm_sst'],
        multi_model_ensemble_statistic = ['ensemble_mean', 'ensemble_median', 'ensemble_range', 'ensemble_standard_deviation', 'negative_ensemble_counts', 'positive_ensemble_counts'],
        period = ['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '1951_1980', '1985_2014', '2021_2050'],
        product_type = ['single_model', 'multi_model_ensemble', 'reanalysis'],
        statistic = ['1_year', '10_year', '100_year', '2_year', '25_year', '5_year', '50_year', '75_year', '10th', '25th', '5th', '50th', '75th', '90th', '95th'],
        variable = ['surge_level', 'total_water_level', 'mean_sea_level', 'tidal_range', 'highest_astronomical_tide', 'lowest_astronomical_tide', 'annual_mean_of_highest_high_water', 'annual_mean_of_lowest_low_water'],
    )

    @Collection.wrapper
    def download(cls, confidence_interval: OneOrMore[str], derived_variable: OneOrMore[str], experiment: OneOrMore[str], model: OneOrMore[str], multi_model_ensemble_statistic: OneOrMore[str], period: OneOrMore[str], product_type: OneOrMore[str], statistic: OneOrMore[str], variable: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param confidence_interval:
        :type confidence_interval: str

        **Valid values:**
        
        - best_fit

        
        - low_bound_confidence_interval

        
        - high_bound_confidence_interval

        ---

        :param derived_variable:
        :type derived_variable: str

        **Valid values:**
        
        - absolute_change

        
        - absolute_value

        
        - percentage_change

        ---

        :param experiment:
        :type experiment: str

        **Valid values:**
        
        - historical

        
        - future

        ---

        :param model:
        :type model: str

        **Valid values:**
        
        - cmcc_cm2_vhr4

        
        - ec_earth3p_hr

        
        - hadgem3_gc31_hm

        
        - hadgem3_gc31_hm_sst

        ---

        :param multi_model_ensemble_statistic:
        :type multi_model_ensemble_statistic: str

        **Valid values:**
        
        - ensemble_mean

        
        - ensemble_median

        
        - ensemble_range

        
        - ensemble_standard_deviation

        
        - negative_ensemble_counts

        
        - positive_ensemble_counts

        ---

        :param period:
        :type period: str

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

        
        - 1951_1980

        
        - 1985_2014

        
        - 2021_2050

        ---

        :param product_type:
        :type product_type: str

        **Valid values:**
        
        - single_model

        
        - multi_model_ensemble

        
        - reanalysis

        ---

        :param statistic:
        :type statistic: str

        **Valid values:**
        
        - 1_year

        
        - 10_year

        
        - 100_year

        
        - 2_year

        
        - 25_year

        
        - 5_year

        
        - 50_year

        
        - 75_year

        
        - 10th

        
        - 25th

        
        - 5th

        
        - 50th

        
        - 75th

        
        - 90th

        
        - 95th

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - surge_level

        
        - total_water_level

        
        - mean_sea_level

        
        - tidal_range

        
        - highest_astronomical_tide

        
        - lowest_astronomical_tide

        
        - annual_mean_of_highest_high_water

        
        - annual_mean_of_lowest_low_water

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_water_level_change_indicators_cmip6(confidence_interval: OneOrMore[str], derived_variable: OneOrMore[str], experiment: OneOrMore[str], model: OneOrMore[str], multi_model_ensemble_statistic: OneOrMore[str], period: OneOrMore[str], product_type: OneOrMore[str], statistic: OneOrMore[str], variable: OneOrMore[str]):
    return Collection_sis_water_level_change_indicators_cmip6.download(confidence_interval=confidence_interval, derived_variable=derived_variable, experiment=experiment, model=model, multi_model_ensemble_statistic=multi_model_ensemble_statistic, period=period, product_type=product_type, statistic=statistic, variable=variable)

