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

class Collection_satellite_total_column_water_vapour_land_ocean(Collection):
    collection_name = 'satellite-total-column-water-vapour-land-ocean'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        horizontal_aggregation = ['0_05_x_0_05', '0_5_x_0_5'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        product = ['c3s_meris_and_ssm_i', 'near_infrared_hoaps_combined'],
        temporal_aggregation = ['monthly', 'daily'],
        year = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
        variable = ['all'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], horizontal_aggregation: OneOrMore[str], month: OneOrMore[str], product: str, temporal_aggregation: str, year: OneOrMore[str], variable: str = 'all'): 
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

        :param horizontal_aggregation:
        :type horizontal_aggregation: str

        **Valid values:**
        
        - 0_05_x_0_05

        
        - 0_5_x_0_5

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

        :param product:
        :type product: str

        **Valid values:**
        
        - c3s_meris_and_ssm_i

        
        - near_infrared_hoaps_combined

        ---

        :param temporal_aggregation:
        :type temporal_aggregation: str

        **Valid values:**
        
        - monthly

        
        - daily

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

def download_satellite_total_column_water_vapour_land_ocean(day: OneOrMore[str], horizontal_aggregation: OneOrMore[str], month: OneOrMore[str], product: str, temporal_aggregation: str, year: OneOrMore[str], variable: str = 'all'):
    return Collection_satellite_total_column_water_vapour_land_ocean.download(day=day, horizontal_aggregation=horizontal_aggregation, month=month, product=product, temporal_aggregation=temporal_aggregation, year=year, variable=variable)

