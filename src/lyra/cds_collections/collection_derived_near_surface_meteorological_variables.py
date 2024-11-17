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

class Collection_derived_near_surface_meteorological_variables(Collection):
    collection_name = 'derived-near-surface-meteorological-variables'
    valid_values = dict(
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        reference_dataset = ['cru', 'cru_and_gpcc'],
        variable = ['grid_point_altitude', 'near_surface_wind_speed', 'near_surface_air_temperature', 'surface_air_pressure', 'near_surface_specific_humidity', 'surface_downwelling_shortwave_radiation', 'surface_downwelling_longwave_radiation', 'rainfall_flux', 'snowfall_flux'],
        year = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'],
        version = ['deprecated (1.0)', '1_1', '2_0', '2_1'],
    )

    @Collection.wrapper
    def download(cls, month: OneOrMore[str], reference_dataset: str, variable: OneOrMore[str], year: OneOrMore[str], version: OneOrMore[str] = '2.1'): 
        """
        Parameters
        ----------
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

        :param reference_dataset:
        :type reference_dataset: str

        **Valid values:**
        
        - cru

        
        - cru_and_gpcc

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - grid_point_altitude

        
        - near_surface_wind_speed

        
        - near_surface_air_temperature

        
        - surface_air_pressure

        
        - near_surface_specific_humidity

        
        - surface_downwelling_shortwave_radiation

        
        - surface_downwelling_longwave_radiation

        
        - rainfall_flux

        
        - snowfall_flux

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

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - deprecated (1.0)

        
        - 1_1

        
        - 2_0

        
        - 2_1

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_derived_near_surface_meteorological_variables(month: OneOrMore[str], reference_dataset: str, variable: OneOrMore[str], year: OneOrMore[str], version: OneOrMore[str] = '2.1'):
    return Collection_derived_near_surface_meteorological_variables.download(month=month, reference_dataset=reference_dataset, variable=variable, year=year, version=version)

