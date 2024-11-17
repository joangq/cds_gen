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

class Collection_sis_tourism_fire_danger_indicators(Collection):
    collection_name = 'sis-tourism-fire-danger-indicators'
    valid_values = dict(
        experiment = ['historical', 'rcp2_6', 'rcp4_5', 'rcp8_5'],
        gcm_model = ['cnrm_cm5', 'ec_earth', 'ipsl_cm5a_mr', 'hadgem2_es', 'mpi_esm_lr', 'noresm1_m'],
        period = ['1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057', '2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065', '2066', '2067', '2068', '2069', '2070', '2071', '2072', '2073', '2074', '2075', '2076', '2077', '2078', '2079', '2080', '2081', '2082', '2083', '2084', '2085', '2086', '2087', '2088', '2089', '2090', '2091', '2092', '2093', '2094', '2095', '2096', '2097', '2098', '1971_1975', '1976_1980', '1981_1982', '1981_1985', '1981_2000', '1981_2005', '1986_1990', '1991_1995', '1996_2000', '2001_2005', '2006_2010', '2011_2015', '2016_2020', '2021_2025', '2021_2040', '2026_2030', '2031_2035', '2036_2040', '2041_2045', '2041_2060', '2046_2050', '2051_2055', '2056_2060', '2061_2065', '2066_2070', '2071_2075', '2076_2080', '2078_2097', '2079_2098', '2081_2085', '2086_2090', '2091_2095', '2096_2098'],
        product_type = ['single_model', 'multi_model_mean_case', 'multi_model_best_case', 'multi_model_worst_case'],
        time_aggregation = ['daily_indicators', 'seasonal_indicators', 'annual_indicators'],
        variable = ['daily_fire_weather_index', 'seasonal_fire_weather_index', 'number_of_days_with_moderate_fire_danger', 'number_of_days_with_high_fire_danger', 'number_of_days_with_very_high_fire_danger'],
        version = ['v1_0', 'v2_0'],
    )

    @Collection.wrapper
    def download(cls, experiment: str, gcm_model: OneOrMore[str], period: OneOrMore[str], product_type: str, time_aggregation: str, variable: OneOrMore[str], version: str): 
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

        ---

        :param gcm_model:
        :type gcm_model: str

        **Valid values:**
        
        - cnrm_cm5

        
        - ec_earth

        
        - ipsl_cm5a_mr

        
        - hadgem2_es

        
        - mpi_esm_lr

        
        - noresm1_m

        ---

        :param period:
        :type period: str

        **Valid values:**
        
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

        
        - 1971_1975

        
        - 1976_1980

        
        - 1981_1982

        
        - 1981_1985

        
        - 1981_2000

        
        - 1981_2005

        
        - 1986_1990

        
        - 1991_1995

        
        - 1996_2000

        
        - 2001_2005

        
        - 2006_2010

        
        - 2011_2015

        
        - 2016_2020

        
        - 2021_2025

        
        - 2021_2040

        
        - 2026_2030

        
        - 2031_2035

        
        - 2036_2040

        
        - 2041_2045

        
        - 2041_2060

        
        - 2046_2050

        
        - 2051_2055

        
        - 2056_2060

        
        - 2061_2065

        
        - 2066_2070

        
        - 2071_2075

        
        - 2076_2080

        
        - 2078_2097

        
        - 2079_2098

        
        - 2081_2085

        
        - 2086_2090

        
        - 2091_2095

        
        - 2096_2098

        ---

        :param product_type:
        :type product_type: str

        **Valid values:**
        
        - single_model

        
        - multi_model_mean_case

        
        - multi_model_best_case

        
        - multi_model_worst_case

        ---

        :param time_aggregation:
        :type time_aggregation: str

        **Valid values:**
        
        - daily_indicators

        
        - seasonal_indicators

        
        - annual_indicators

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - daily_fire_weather_index

        
        - seasonal_fire_weather_index

        
        - number_of_days_with_moderate_fire_danger

        
        - number_of_days_with_high_fire_danger

        
        - number_of_days_with_very_high_fire_danger

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - v1_0

        
        - v2_0

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_tourism_fire_danger_indicators(experiment: str, gcm_model: OneOrMore[str], period: OneOrMore[str], product_type: str, time_aggregation: str, variable: OneOrMore[str], version: str):
    return Collection_sis_tourism_fire_danger_indicators.download(experiment=experiment, gcm_model=gcm_model, period=period, product_type=product_type, time_aggregation=time_aggregation, variable=variable, version=version)

