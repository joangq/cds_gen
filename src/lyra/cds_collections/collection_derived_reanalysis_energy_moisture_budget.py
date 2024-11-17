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

class Collection_derived_reanalysis_energy_moisture_budget(Collection):
    collection_name = 'derived-reanalysis-energy-moisture-budget'
    valid_values = dict(
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        variable = ['divergence_of_vertical_integral_of_latent_heat_flux', 'divergence_of_vertical_integral_of_total_energy_flux', 'divergence_of_vertical_integral_of_water_vapour_flux', 'vertical_integral_of_eastward_latent_heat_flux', 'vertical_integral_of_eastward_total_energy_flux', 'vertical_integral_of_eastward_water_vapour_flux', 'vertical_integral_of_northward_latent_heat_flux', 'vertical_integral_of_northward_total_energy_flux', 'vertical_integral_of_northward_water_vapour_flux', 'tendency_of_vertical_integral_of_latent_heat', 'tendency_of_vertical_integral_of_water_vapour', 'tendency_of_vertical_integral_of_total_energy'],
        year = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'],
    )

    @Collection.wrapper
    def download(cls, month: OneOrMore[str], variable: str, year: OneOrMore[str], area_group: Optional[Union[LabelType, GeographicExtentMapType]] = None): 
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

        :param variable:
        :type variable: str

        **Valid values:**
        
        - divergence_of_vertical_integral_of_latent_heat_flux

        
        - divergence_of_vertical_integral_of_total_energy_flux

        
        - divergence_of_vertical_integral_of_water_vapour_flux

        
        - vertical_integral_of_eastward_latent_heat_flux

        
        - vertical_integral_of_eastward_total_energy_flux

        
        - vertical_integral_of_eastward_water_vapour_flux

        
        - vertical_integral_of_northward_latent_heat_flux

        
        - vertical_integral_of_northward_total_energy_flux

        
        - vertical_integral_of_northward_water_vapour_flux

        
        - tendency_of_vertical_integral_of_latent_heat

        
        - tendency_of_vertical_integral_of_water_vapour

        
        - tendency_of_vertical_integral_of_total_energy

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

def download_derived_reanalysis_energy_moisture_budget(month: OneOrMore[str], variable: str, year: OneOrMore[str], area_group: Optional[Union[LabelType, GeographicExtentMapType]] = None):
    return Collection_derived_reanalysis_energy_moisture_budget.download(month=month, variable=variable, year=year, area_group=area_group)

