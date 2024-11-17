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

class Collection_satellite_soil_moisture(Collection):
    collection_name = 'satellite-soil-moisture'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        time_aggregation = ['day_average', '10_day_average', 'month_average'],
        type_of_record = ['icdr', 'cdr'],
        type_of_sensor = ['active', 'passive', 'combined_passive_and_active'],
        variable = ['surface_soil_moisture', 'volumetric_surface_soil_moisture'],
        version = ['v202212', 'v201706', 'v201812', 'deprecated_v201912', 'v201912_1', 'v202012'],
        year = ['1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], month: OneOrMore[str], time_aggregation: OneOrMore[str], type_of_record: OneOrMore[str], type_of_sensor: OneOrMore[str], variable: OneOrMore[str], version: OneOrMore[str], year: OneOrMore[str]): 
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

        :param time_aggregation:
        :type time_aggregation: str

        **Valid values:**
        
        - day_average

        
        - 10_day_average

        
        - month_average

        ---

        :param type_of_record:
        :type type_of_record: str

        **Valid values:**
        
        - icdr

        
        - cdr

        ---

        :param type_of_sensor:
        :type type_of_sensor: str

        **Valid values:**
        
        - active

        
        - passive

        
        - combined_passive_and_active

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - surface_soil_moisture

        
        - volumetric_surface_soil_moisture

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - v202212

        
        - v201706

        
        - v201812

        
        - deprecated_v201912

        
        - v201912_1

        
        - v202012

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_satellite_soil_moisture(day: OneOrMore[str], month: OneOrMore[str], time_aggregation: OneOrMore[str], type_of_record: OneOrMore[str], type_of_sensor: OneOrMore[str], variable: OneOrMore[str], version: OneOrMore[str], year: OneOrMore[str]):
    return Collection_satellite_soil_moisture.download(day=day, month=month, time_aggregation=time_aggregation, type_of_record=type_of_record, type_of_sensor=type_of_sensor, variable=variable, version=version, year=year)

