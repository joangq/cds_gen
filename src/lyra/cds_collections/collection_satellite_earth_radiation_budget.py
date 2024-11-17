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

class Collection_satellite_earth_radiation_budget(Collection):
    collection_name = 'satellite-earth-radiation-budget'
    valid_values = dict(
        climate_data_record_type = ['interim_climate_data_record', 'thematic_climate_data_record'],
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        origin = ['nasa', 'noaa_ncei', 'eumetsat', 'esa', 'c3s', 'rmib'],
        product_family = ['ceres_ebaf', 'hirs', 'clara_a3', 'cci', 'tsi'],
        sensor_on_satellite = ['aatsr', 'atsr2', 'slstr_on_sentinel_3a', 'slstr_on_sentinel_3b', 'slstr_on_sentinel_3a_3b'],
        time_aggregation = ['daily_mean', 'monthly_mean'],
        variable = ['incoming_shortwave_radiation', 'outgoing_longwave_radiation', 'outgoing_shortwave_radiation', 'total_solar_irradiance', 'all_variables'],
        version = ['1_2_reprocessed', '2_7_reprocessed'],
        year = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
    )

    @Collection.wrapper
    def download(cls, climate_data_record_type: str, day: OneOrMore[str], month: OneOrMore[str], origin: str, product_family: str, sensor_on_satellite: OneOrMore[str], time_aggregation: str, variable: OneOrMore[str], version: OneOrMore[str], year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): 
        """
        Parameters
        ----------
        :param climate_data_record_type:
        :type climate_data_record_type: str

        **Valid values:**
        
        - interim_climate_data_record

        
        - thematic_climate_data_record

        ---

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

        :param origin:
        :type origin: str

        **Valid values:**
        
        - nasa

        
        - noaa_ncei

        
        - eumetsat

        
        - esa

        
        - c3s

        
        - rmib

        ---

        :param product_family:
        :type product_family: str

        **Valid values:**
        
        - ceres_ebaf

        
        - hirs

        
        - clara_a3

        
        - cci

        
        - tsi

        ---

        :param sensor_on_satellite:
        :type sensor_on_satellite: str

        **Valid values:**
        
        - aatsr

        
        - atsr2

        
        - slstr_on_sentinel_3a

        
        - slstr_on_sentinel_3b

        
        - slstr_on_sentinel_3a_3b

        ---

        :param time_aggregation:
        :type time_aggregation: str

        **Valid values:**
        
        - daily_mean

        
        - monthly_mean

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - incoming_shortwave_radiation

        
        - outgoing_longwave_radiation

        
        - outgoing_shortwave_radiation

        
        - total_solar_irradiance

        
        - all_variables

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - 1_2_reprocessed

        
        - 2_7_reprocessed

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

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_satellite_earth_radiation_budget(climate_data_record_type: str, day: OneOrMore[str], month: OneOrMore[str], origin: str, product_family: str, sensor_on_satellite: OneOrMore[str], time_aggregation: str, variable: OneOrMore[str], version: OneOrMore[str], year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
    return Collection_satellite_earth_radiation_budget.download(climate_data_record_type=climate_data_record_type, day=day, month=month, origin=origin, product_family=product_family, sensor_on_satellite=sensor_on_satellite, time_aggregation=time_aggregation, variable=variable, version=version, year=year, area_group=area_group)

