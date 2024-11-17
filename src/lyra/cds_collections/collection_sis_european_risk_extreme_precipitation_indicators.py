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

class Collection_sis_european_risk_extreme_precipitation_indicators(Collection):
    collection_name = 'sis-european-risk-extreme-precipitation-indicators'
    valid_values = dict(
        city = ['amadora', 'amersfoort', 'antwerp', 'athens', 'bilbao', 'birmingham', 'brussels', 'bucharest', 'budapest', 'frankfurt_am_main', 'koln', 'london', 'milan', 'pamplona', 'paris', 'prague', 'riga', 'rimini', 'stockholm', 'vienna'],
        percentile = ['90th', '95th', '99th'],
        period = ['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '1989_2018'],
        product_type = ['e_obs', 'eca_d', 'era5', 'era5_2km'],
        return_period = ['10-yrs', '100-yrs', '25-yrs', '5-yrs', '50-yrs'],
        spatial_coverage = ['city', 'europe'],
        temporal_aggregation = ['30_year', 'daily', 'monthly', 'yearly'],
        variable = ['maximum_1_day_precipitation', 'maximum_5_day_precipitation', 'number_of_consecutive_wet_days', 'number_of_precipitation_days_exceeding_20mm', 'number_of_precipitation_days_exceeding_fixed_percentiles', 'number_of_wet_days', 'total_precipitation', 'precipitation_at_fixed_percentiles', 'precipitation_at_fixed_return_periods', 'standardised_precipitation_exceeding_fixed_percentiles'],
    )

    @Collection.wrapper
    def download(cls, city: OneOrMore[str], percentile: OneOrMore[str], period: OneOrMore[str], product_type: OneOrMore[str], return_period: OneOrMore[str], spatial_coverage: OneOrMore[str], temporal_aggregation: OneOrMore[str], variable: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param city:
        :type city: str

        **Valid values:**
        
        - amadora

        
        - amersfoort

        
        - antwerp

        
        - athens

        
        - bilbao

        
        - birmingham

        
        - brussels

        
        - bucharest

        
        - budapest

        
        - frankfurt_am_main

        
        - koln

        
        - london

        
        - milan

        
        - pamplona

        
        - paris

        
        - prague

        
        - riga

        
        - rimini

        
        - stockholm

        
        - vienna

        ---

        :param percentile:
        :type percentile: str

        **Valid values:**
        
        - 90th

        
        - 95th

        
        - 99th

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

        
        - 1989_2018

        ---

        :param product_type:
        :type product_type: str

        **Valid values:**
        
        - e_obs

        
        - eca_d

        
        - era5

        
        - era5_2km

        ---

        :param return_period:
        :type return_period: str

        **Valid values:**
        
        - 10-yrs

        
        - 100-yrs

        
        - 25-yrs

        
        - 5-yrs

        
        - 50-yrs

        ---

        :param spatial_coverage:
        :type spatial_coverage: str

        **Valid values:**
        
        - city

        
        - europe

        ---

        :param temporal_aggregation:
        :type temporal_aggregation: str

        **Valid values:**
        
        - 30_year

        
        - daily

        
        - monthly

        
        - yearly

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - maximum_1_day_precipitation

        
        - maximum_5_day_precipitation

        
        - number_of_consecutive_wet_days

        
        - number_of_precipitation_days_exceeding_20mm

        
        - number_of_precipitation_days_exceeding_fixed_percentiles

        
        - number_of_wet_days

        
        - total_precipitation

        
        - precipitation_at_fixed_percentiles

        
        - precipitation_at_fixed_return_periods

        
        - standardised_precipitation_exceeding_fixed_percentiles

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_european_risk_extreme_precipitation_indicators(city: OneOrMore[str], percentile: OneOrMore[str], period: OneOrMore[str], product_type: OneOrMore[str], return_period: OneOrMore[str], spatial_coverage: OneOrMore[str], temporal_aggregation: OneOrMore[str], variable: OneOrMore[str]):
    return Collection_sis_european_risk_extreme_precipitation_indicators.download(city=city, percentile=percentile, period=period, product_type=product_type, return_period=return_period, spatial_coverage=spatial_coverage, temporal_aggregation=temporal_aggregation, variable=variable)

