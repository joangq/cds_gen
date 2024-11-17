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

class Collection_satellite_fire_radiative_power(Collection):
    collection_name = 'satellite-fire-radiative-power'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        horizontal_aggregation = ['0_1_degree_x_0_1_degree', '0_25_degree_x_0_25_degree'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        observation_time = ['night', 'day'],
        product_type = ['gridded', 'table_summary'],
        satellite = ['sentinel_3a', 'sentinel_3b'],
        time_aggregation = ['day', '27_days', 'month'],
        version = ['1_0', '1_2'],
        year = ['2020', '2021', '2022', '2023', '2024'],
        variable = ['all'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], horizontal_aggregation: str, month: OneOrMore[str], observation_time: OneOrMore[str], product_type: str, satellite: OneOrMore[str], time_aggregation: str, version: OneOrMore[str], year: str, variable: str = 'all'): 
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
        
        - 0_1_degree_x_0_1_degree

        
        - 0_25_degree_x_0_25_degree

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

        :param observation_time:
        :type observation_time: str

        **Valid values:**
        
        - night

        
        - day

        ---

        :param product_type:
        :type product_type: str

        **Valid values:**
        
        - gridded

        
        - table_summary

        ---

        :param satellite:
        :type satellite: str

        **Valid values:**
        
        - sentinel_3a

        
        - sentinel_3b

        ---

        :param time_aggregation:
        :type time_aggregation: str

        **Valid values:**
        
        - day

        
        - 27_days

        
        - month

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - 1_0

        
        - 1_2

        ---

        :param year:
        :type year: str

        **Valid values:**
        
        - 2020

        
        - 2021

        
        - 2022

        
        - 2023

        
        - 2024

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

def download_satellite_fire_radiative_power(day: OneOrMore[str], horizontal_aggregation: str, month: OneOrMore[str], observation_time: OneOrMore[str], product_type: str, satellite: OneOrMore[str], time_aggregation: str, version: OneOrMore[str], year: str, variable: str = 'all'):
    return Collection_satellite_fire_radiative_power.download(day=day, horizontal_aggregation=horizontal_aggregation, month=month, observation_time=observation_time, product_type=product_type, satellite=satellite, time_aggregation=time_aggregation, version=version, year=year, variable=variable)

