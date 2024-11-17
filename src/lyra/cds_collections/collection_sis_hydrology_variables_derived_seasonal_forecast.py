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

class Collection_sis_hydrology_variables_derived_seasonal_forecast(Collection):
    collection_name = 'sis-hydrology-variables-derived-seasonal-forecast'
    valid_values = dict(
        hydrological_model = ['e_hypecatch_m00', 'e_hypecatch_m01', 'e_hypecatch_m02', 'e_hypecatch_m05', 'e_hypecatch_m06', 'e_hypecatch_m07', 'e_hypecatch_m08', 'e_hypecatch_m09', 'e_hypegrid', 'lisflood_efas', 'vic_wur'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        variable = ['river_discharge', 'reference_river_discharge_lower_tercile', 'reference_river_discharge_upper_tercile', 'brier_skill_score_above_normal_conditions', 'brier_skill_score_below_normal_conditions', 'continuous_ranked_probability_skill_score', 'fair_ranked_probability_skill_score'],
        year = ['2020', '2021', '2022', '2023', '2024'],
        version = ['1'],
    )

    @Collection.wrapper
    def download(cls, hydrological_model: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], version: OneOrMore[str] = 1): 
        """
        Parameters
        ----------
        :param hydrological_model:
        :type hydrological_model: str

        **Valid values:**
        
        - e_hypecatch_m00

        
        - e_hypecatch_m01

        
        - e_hypecatch_m02

        
        - e_hypecatch_m05

        
        - e_hypecatch_m06

        
        - e_hypecatch_m07

        
        - e_hypecatch_m08

        
        - e_hypecatch_m09

        
        - e_hypegrid

        
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

        :param year:
        :type year: str

        **Valid values:**
        
        - 2020

        
        - 2021

        
        - 2022

        
        - 2023

        
        - 2024

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - 1

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_hydrology_variables_derived_seasonal_forecast(hydrological_model: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], version: OneOrMore[str] = 1):
    return Collection_sis_hydrology_variables_derived_seasonal_forecast.download(hydrological_model=hydrological_model, month=month, variable=variable, year=year, version=version)

