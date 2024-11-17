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

class Collection_projections_cmip6_decadal_prototype(Collection):
    collection_name = 'projections-cmip6-decadal-prototype'
    valid_values = dict(
        base_year = ['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021'],
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        model = ['cmcc_cm2_sr5', 'ec_earth3', 'hadgem3_gc31_mm', 'mpi_esm1_2_hr', 'mpi_esm1_2_lr'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        temporal_resolution = ['monthly', 'daily'],
        variable = ['near_surface_air_temperature', 'daily_maximum_near_surface_air_temperature', 'precipitation', 'sea_level_pressure', 'daily_minimum_near_surface_air_temperature', '500_hpa_geopotential_height'],
        year = ['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031'],
    )

    @Collection.wrapper
    def download(cls, base_year: str, day: OneOrMore[str], model: str, month: OneOrMore[str], temporal_resolution: str, variable: str, year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): 
        """
        Parameters
        ----------
        :param base_year:
        :type base_year: str

        **Valid values:**
        
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

        :param model:
        :type model: str

        **Valid values:**
        
        - cmcc_cm2_sr5

        
        - ec_earth3

        
        - hadgem3_gc31_mm

        
        - mpi_esm1_2_hr

        
        - mpi_esm1_2_lr

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

        :param temporal_resolution:
        :type temporal_resolution: str

        **Valid values:**
        
        - monthly

        
        - daily

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - near_surface_air_temperature

        
        - daily_maximum_near_surface_air_temperature

        
        - precipitation

        
        - sea_level_pressure

        
        - daily_minimum_near_surface_air_temperature

        
        - 500_hpa_geopotential_height

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

def download_projections_cmip6_decadal_prototype(base_year: str, day: OneOrMore[str], model: str, month: OneOrMore[str], temporal_resolution: str, variable: str, year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
    return Collection_projections_cmip6_decadal_prototype.download(base_year=base_year, day=day, model=model, month=month, temporal_resolution=temporal_resolution, variable=variable, year=year, area_group=area_group)

