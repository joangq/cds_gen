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

class Collection_reanalysis_uerra_europe_pressure_levels(Collection):
    collection_name = 'reanalysis-uerra-europe-pressure-levels'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        pressure_level = ['10', '20', '30', '50', '70', '100', '150', '200', '250', '300', '400', '500', '600', '700', '750', '800', '825', '850', '875', '900', '925', '950', '975', '1000'],
        time = ['00:00', '06:00', '12:00', '18:00'],
        variable = ['geopotential', 'geopotential_height', 'relative_humidity', 'temperature', 'u_component_of_wind', 'v_component_of_wind'],
        year = ['1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'],
        data_format = ['grib', 'netcdf'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], month: OneOrMore[str], pressure_level: OneOrMore[str], time: OneOrMore[str], variable: str, year: OneOrMore[str], data_format: str = 'grib'): 
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

        :param pressure_level:
        :type pressure_level: str

        **Valid values:**
        
        - 10

        
        - 20

        
        - 30

        
        - 50

        
        - 70

        
        - 100

        
        - 150

        
        - 200

        
        - 250

        
        - 300

        
        - 400

        
        - 500

        
        - 600

        
        - 700

        
        - 750

        
        - 800

        
        - 825

        
        - 850

        
        - 875

        
        - 900

        
        - 925

        
        - 950

        
        - 975

        
        - 1000

        ---

        :param time:
        :type time: str

        **Valid values:**
        
        - 00:00

        
        - 06:00

        
        - 12:00

        
        - 18:00

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - geopotential

        
        - geopotential_height

        
        - relative_humidity

        
        - temperature

        
        - u_component_of_wind

        
        - v_component_of_wind

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

        ---

        :param data_format:
        :type data_format: str

        **Valid values:**
        
        - grib

        
        - netcdf

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_reanalysis_uerra_europe_pressure_levels(day: OneOrMore[str], month: OneOrMore[str], pressure_level: OneOrMore[str], time: OneOrMore[str], variable: str, year: OneOrMore[str], data_format: str = 'grib'):
    return Collection_reanalysis_uerra_europe_pressure_levels.download(day=day, month=month, pressure_level=pressure_level, time=time, variable=variable, year=year, data_format=data_format)

