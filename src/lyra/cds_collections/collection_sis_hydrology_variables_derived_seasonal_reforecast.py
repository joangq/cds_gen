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

class Collection_sis_hydrology_variables_derived_seasonal_reforecast(Collection):
    collection_name = 'sis-hydrology-variables-derived-seasonal-reforecast'
    valid_values = dict(
        hydrological_model = ['e_hypecatch_m00', 'lisflood_efas', 'vic_wur'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        variable = ['river_discharge', 'reference_river_discharge_lower_tercile', 'reference_river_discharge_upper_tercile', 'brier_skill_score_above_normal_conditions', 'brier_skill_score_below_normal_conditions', 'continuous_ranked_probability_skill_score', 'fair_ranked_probability_skill_score'],
        version = ['1'],
        year = ['1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'],
    )

    @Collection.wrapper
    def download(cls, hydrological_model: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], version: OneOrMore[str], year: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param hydrological_model:
        :type hydrological_model: str

        **Valid values:**
        
        - e_hypecatch_m00

        
        - lisflood_efas

        
        - vic_wur

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

        :param variable:
        :type variable: str

        **Valid values:**
        
        - river_discharge

        
        - reference_river_discharge_lower_tercile

        
        - reference_river_discharge_upper_tercile

        
        - brier_skill_score_above_normal_conditions

        
        - brier_skill_score_below_normal_conditions

        
        - continuous_ranked_probability_skill_score

        
        - fair_ranked_probability_skill_score

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - 1

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_hydrology_variables_derived_seasonal_reforecast(hydrological_model: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], version: OneOrMore[str], year: OneOrMore[str]):
    return Collection_sis_hydrology_variables_derived_seasonal_reforecast.download(hydrological_model=hydrological_model, month=month, variable=variable, version=version, year=year)

