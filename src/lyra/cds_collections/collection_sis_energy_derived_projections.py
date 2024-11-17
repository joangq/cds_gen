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

class Collection_sis_energy_derived_projections(Collection):
    collection_name = 'sis-energy-derived-projections'
    valid_values = dict(
        energy_product_type = ['capacity_factor_ratio', 'energy', 'power'],
        ensemble_member = ['r12i1p1', 'r1i1p1', 'r3i1p1'],
        experiment = ['rcp_2_6', 'rcp_4_5', 'rcp_8_5'],
        gcm = ['cnrm_cm5', 'ec_earth', 'ipsl_cm5a_mr', 'hadgem2_es', 'mpi_esm_lr', 'noresm1_m'],
        rcm = ['aladin63', 'cclm4_8_17', 'hirham5', 'racmo22e', 'regcm4', 'rca4', 'wrf381p'],
        spatial_aggregation = ['country_level', 'sub_country_level', 'maritime_country_level', 'maritime_sub_country_level', 'original_grid'],
        temporal_aggregation = ['3_hourly', 'daily', 'monthly', 'seasonal', 'annual'],
        variable = ['wind_speed_at_100m', 'wind_speed_at_10m', 'surface_downwelling_shortwave_radiation', '2m_air_temperature', 'total_precipitation', 'electricity_demand', 'hydro_power_generation_reservoirs', 'hydro_power_generation_rivers', 'solar_photovoltaic_power_generation', 'wind_power_generation_offshore', 'wind_power_generation_onshore'],
    )

    @Collection.wrapper
    def download(cls, energy_product_type: OneOrMore[str], ensemble_member: OneOrMore[str], experiment: OneOrMore[str], gcm: OneOrMore[str], rcm: str, spatial_aggregation: str, temporal_aggregation: str, variable: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param energy_product_type:
        :type energy_product_type: str

        **Valid values:**
        
        - capacity_factor_ratio

        
        - energy

        
        - power

        ---

        :param ensemble_member:
        :type ensemble_member: str

        **Valid values:**
        
        - r12i1p1

        
        - r1i1p1

        
        - r3i1p1

        ---

        :param experiment:
        :type experiment: str

        **Valid values:**
        
        - rcp_2_6

        
        - rcp_4_5

        
        - rcp_8_5

        ---

        :param gcm:
        :type gcm: str

        **Valid values:**
        
        - cnrm_cm5

        
        - ec_earth

        
        - ipsl_cm5a_mr

        
        - hadgem2_es

        
        - mpi_esm_lr

        
        - noresm1_m

        ---

        :param rcm:
        :type rcm: str

        **Valid values:**
        
        - aladin63

        
        - cclm4_8_17

        
        - hirham5

        
        - racmo22e

        
        - regcm4

        
        - rca4

        
        - wrf381p

        ---

        :param spatial_aggregation:
        :type spatial_aggregation: str

        **Valid values:**
        
        - country_level

        
        - sub_country_level

        
        - maritime_country_level

        
        - maritime_sub_country_level

        
        - original_grid

        ---

        :param temporal_aggregation:
        :type temporal_aggregation: str

        **Valid values:**
        
        - 3_hourly

        
        - daily

        
        - monthly

        
        - seasonal

        
        - annual

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - wind_speed_at_100m

        
        - wind_speed_at_10m

        
        - surface_downwelling_shortwave_radiation

        
        - 2m_air_temperature

        
        - total_precipitation

        
        - electricity_demand

        
        - hydro_power_generation_reservoirs

        
        - hydro_power_generation_rivers

        
        - solar_photovoltaic_power_generation

        
        - wind_power_generation_offshore

        
        - wind_power_generation_onshore

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_energy_derived_projections(energy_product_type: OneOrMore[str], ensemble_member: OneOrMore[str], experiment: OneOrMore[str], gcm: OneOrMore[str], rcm: str, spatial_aggregation: str, temporal_aggregation: str, variable: OneOrMore[str]):
    return Collection_sis_energy_derived_projections.download(energy_product_type=energy_product_type, ensemble_member=ensemble_member, experiment=experiment, gcm=gcm, rcm=rcm, spatial_aggregation=spatial_aggregation, temporal_aggregation=temporal_aggregation, variable=variable)

