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

class Collection_sis_european_wind_storm_indicators(Collection):
    collection_name = 'sis-european-wind-storm-indicators'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        month = ['01', '02', '03', '10', '11', '12'],
        product = ['windstorm_tracks', 'windstorm_footprints', 'summary_indicators', 'risk_indicators', 'loss_indicators'],
        spatial_aggregation = ['austria', 'belgium', 'switzerland', 'czech_republic', 'germany', 'denmark', 'estonia', 'spain', 'finland', 'france', 'ireland', 'italy', 'lithuania', 'luxemburg', 'latvia', 'netherlands', 'norway', 'poland', 'portugal', 'sweden', 'united_kingdom', 'agriculture', 'transport', 'residential', 'other', 'industry', 'europe', 'european_nuts1_region', 'european_nuts3_region'],
        time_aggregation = ['annual', 'decadal'],
        year = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2005', '2006', '2007', '2008', '2009', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2020', '2021'],
        variable = ['all'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], month: OneOrMore[str], product: OneOrMore[str], spatial_aggregation: OneOrMore[str], time_aggregation: OneOrMore[str], year: OneOrMore[str], variable: str = 'all'): 
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

        
        - 10

        
        - 11

        
        - 12

        ---

        :param product:
        :type product: str

        **Valid values:**
        
        - windstorm_tracks

        
        - windstorm_footprints

        
        - summary_indicators

        
        - risk_indicators

        
        - loss_indicators

        ---

        :param spatial_aggregation:
        :type spatial_aggregation: str

        **Valid values:**
        
        - austria

        
        - belgium

        
        - switzerland

        
        - czech_republic

        
        - germany

        
        - denmark

        
        - estonia

        
        - spain

        
        - finland

        
        - france

        
        - ireland

        
        - italy

        
        - lithuania

        
        - luxemburg

        
        - latvia

        
        - netherlands

        
        - norway

        
        - poland

        
        - portugal

        
        - sweden

        
        - united_kingdom

        
        - agriculture

        
        - transport

        
        - residential

        
        - other

        
        - industry

        
        - europe

        
        - european_nuts1_region

        
        - european_nuts3_region

        ---

        :param time_aggregation:
        :type time_aggregation: str

        **Valid values:**
        
        - annual

        
        - decadal

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

        
        - 2005

        
        - 2006

        
        - 2007

        
        - 2008

        
        - 2009

        
        - 2011

        
        - 2012

        
        - 2013

        
        - 2014

        
        - 2015

        
        - 2016

        
        - 2017

        
        - 2020

        
        - 2021

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - all

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_european_wind_storm_indicators(day: OneOrMore[str], month: OneOrMore[str], product: OneOrMore[str], spatial_aggregation: OneOrMore[str], time_aggregation: OneOrMore[str], year: OneOrMore[str], variable: str = 'all'):
    return Collection_sis_european_wind_storm_indicators.download(day=day, month=month, product=product, spatial_aggregation=spatial_aggregation, time_aggregation=time_aggregation, year=year, variable=variable)

