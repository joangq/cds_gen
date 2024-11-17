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

class Collection_sis_extreme_indices_cmip6(Collection):
    collection_name = 'sis-extreme-indices-cmip6'
    valid_values = dict(
        ensemble_member = ['r10i1p1f1', 'r10i1p2f1', 'r11i1p1f1', 'r11i1p2f1', 'r12i1p1f1', 'r12i1p2f1', 'r13i1p1f1', 'r13i1p2f1', 'r14i1p1f1', 'r14i1p2f1', 'r15i1p1f1', 'r15i1p2f1', 'r16i1p1f1', 'r16i1p2f1', 'r17i1p1f1', 'r17i1p2f1', 'r18i1p1f1', 'r18i1p2f1', 'r19i1p1f1', 'r19i1p2f1', 'r1i1p1f1', 'r1i1p1f2', 'r1i1p1f3', 'r1i1p2f1', 'r20i1p1f1', 'r20i1p2f1', 'r21i1p1f1', 'r21i1p2f1', 'r22i1p1f1', 'r22i1p2f1', 'r23i1p1f1', 'r23i1p2f1', 'r24i1p1f1', 'r24i1p2f1', 'r25i1p1f1', 'r25i1p2f1', 'r26i1p1f1', 'r27i1p1f1', 'r28i1p1f1', 'r29i1p1f1', 'r2i1p1f1', 'r2i1p2f1', 'r30i1p1f1', 'r31i1p1f1', 'r32i1p1f1', 'r33i1p1f1', 'r34i1p1f1', 'r35i1p1f1', 'r36i1p1f1', 'r37i1p1f1', 'r38i1p1f1', 'r39i1p1f1', 'r3i1p1f1', 'r3i1p2f1', 'r40i1p1f1', 'r41i1p1f1', 'r42i1p1f1', 'r43i1p1f1', 'r44i1p1f1', 'r45i1p1f1', 'r46i1p1f1', 'r47i1p1f1', 'r48i1p1f1', 'r49i1p1f1', 'r4i1p1f1', 'r4i1p2f1', 'r50i1p1f1', 'r5i1p1f1', 'r5i1p2f1', 'r6i1p1f1', 'r6i1p2f1', 'r7i1p1f1', 'r7i1p2f1', 'r8i1p1f1', 'r8i1p2f1', 'r9i1p1f1', 'r9i1p2f1'],
        experiment = ['historical', 'ssp1_2_6', 'ssp2_4_5', 'ssp3_7_0', 'ssp5_8_5'],
        model = ['access_cm2', 'access_esm1_5', 'bcc_csm2_mr', 'cnrm_cm6_1', 'cnrm_cm6_1_hr', 'cnrm_esm2_1', 'canesm5', 'ec_earth3', 'ec_earth3_veg', 'fgoals_g3', 'gfdl_cm4', 'gfdl_esm4', 'hadgem3_gc31_ll', 'hadgem3_gc31_mm', 'inm_cm4_8', 'inm_cm5_0', 'kace_1_0_g', 'kiost_esm', 'miroc_es2l', 'miroc6', 'mpi_esm1_2_hr', 'mpi_esm1_2_lr', 'mri_esm2_0', 'nesm3', 'noresm2_lm', 'noresm2_mm', 'ukesm1_0_ll'],
        period = ['19510101_20101230', '19510101_20101231', '19510101_20141230', '19510101_20141231', '20110101_21001230', '20110101_21001231', '20150101_21001230', '20150101_21001231', '184901_201412', '185001_201412', '185001_201612', '195101_201412', '201501_203912', '201501_210012', '201501_218012', '201501_230012', '1849_2014', '1850_2014', '1850_2016', '1951_2014', '2015_2039', '2015_2100', '2015_2180', '2015_2300'],
        product_type = ['base_period_1961_1990', 'base_period_1981_2010', 'base_independent', 'bias_adjusted', 'non_bias_adjusted'],
        temporal_aggregation = ['yearly', 'monthly', 'daily'],
        variable = ['cold_days', 'cold_nights', 'cold_spell_duration_index', 'consecutive_dry_days', 'consecutive_wet_days', 'diurnal_temperature_range', 'extremely_wet_day_precipitation', 'frost_days', 'growing_season_length', 'heavy_precipitation_days', 'ice_days', 'maximum_1_day_precipitation', 'maximum_5_day_precipitation', 'maximum_value_of_daily_maximum_temperature', 'minimum_value_of_daily_maximum_temperature', 'maximum_value_of_daily_minimum_temperature', 'minimum_value_of_daily_minimum_temperature', 'number_of_wet_days', 'simple_daily_intensity_index', 'summer_days', 'total_wet_day_precipitation', 'tropical_nights', 'very_heavy_precipitation_days', 'very_wet_day_precipitation', 'warm_days', 'warm_nights', 'warm_spell_duration_index', 'heat_index', 'humidex', 'universal_thermal_climate_index', 'wet_bulb_temperature_index', 'wet_bulb_globe_temperature_index'],
        version = ['1_0', '2_0'],
    )

    @Collection.wrapper
    def download(cls, ensemble_member: OneOrMore[str], experiment: OneOrMore[str], model: OneOrMore[str], period: OneOrMore[str], product_type: OneOrMore[str], temporal_aggregation: OneOrMore[str], variable: OneOrMore[str], version: OneOrMore[str] = '2_0'): 
        """
        Parameters
        ----------
        :param ensemble_member:
        :type ensemble_member: str

        **Valid values:**
        
        - r10i1p1f1

        
        - r10i1p2f1

        
        - r11i1p1f1

        
        - r11i1p2f1

        
        - r12i1p1f1

        
        - r12i1p2f1

        
        - r13i1p1f1

        
        - r13i1p2f1

        
        - r14i1p1f1

        
        - r14i1p2f1

        
        - r15i1p1f1

        
        - r15i1p2f1

        
        - r16i1p1f1

        
        - r16i1p2f1

        
        - r17i1p1f1

        
        - r17i1p2f1

        
        - r18i1p1f1

        
        - r18i1p2f1

        
        - r19i1p1f1

        
        - r19i1p2f1

        
        - r1i1p1f1

        
        - r1i1p1f2

        
        - r1i1p1f3

        
        - r1i1p2f1

        
        - r20i1p1f1

        
        - r20i1p2f1

        
        - r21i1p1f1

        
        - r21i1p2f1

        
        - r22i1p1f1

        
        - r22i1p2f1

        
        - r23i1p1f1

        
        - r23i1p2f1

        
        - r24i1p1f1

        
        - r24i1p2f1

        
        - r25i1p1f1

        
        - r25i1p2f1

        
        - r26i1p1f1

        
        - r27i1p1f1

        
        - r28i1p1f1

        
        - r29i1p1f1

        
        - r2i1p1f1

        
        - r2i1p2f1

        
        - r30i1p1f1

        
        - r31i1p1f1

        
        - r32i1p1f1

        
        - r33i1p1f1

        
        - r34i1p1f1

        
        - r35i1p1f1

        
        - r36i1p1f1

        
        - r37i1p1f1

        
        - r38i1p1f1

        
        - r39i1p1f1

        
        - r3i1p1f1

        
        - r3i1p2f1

        
        - r40i1p1f1

        
        - r41i1p1f1

        
        - r42i1p1f1

        
        - r43i1p1f1

        
        - r44i1p1f1

        
        - r45i1p1f1

        
        - r46i1p1f1

        
        - r47i1p1f1

        
        - r48i1p1f1

        
        - r49i1p1f1

        
        - r4i1p1f1

        
        - r4i1p2f1

        
        - r50i1p1f1

        
        - r5i1p1f1

        
        - r5i1p2f1

        
        - r6i1p1f1

        
        - r6i1p2f1

        
        - r7i1p1f1

        
        - r7i1p2f1

        
        - r8i1p1f1

        
        - r8i1p2f1

        
        - r9i1p1f1

        
        - r9i1p2f1

        ---

        :param experiment:
        :type experiment: str

        **Valid values:**
        
        - historical

        
        - ssp1_2_6

        
        - ssp2_4_5

        
        - ssp3_7_0

        
        - ssp5_8_5

        ---

        :param model:
        :type model: str

        **Valid values:**
        
        - access_cm2

        
        - access_esm1_5

        
        - bcc_csm2_mr

        
        - cnrm_cm6_1

        
        - cnrm_cm6_1_hr

        
        - cnrm_esm2_1

        
        - canesm5

        
        - ec_earth3

        
        - ec_earth3_veg

        
        - fgoals_g3

        
        - gfdl_cm4

        
        - gfdl_esm4

        
        - hadgem3_gc31_ll

        
        - hadgem3_gc31_mm

        
        - inm_cm4_8

        
        - inm_cm5_0

        
        - kace_1_0_g

        
        - kiost_esm

        
        - miroc_es2l

        
        - miroc6

        
        - mpi_esm1_2_hr

        
        - mpi_esm1_2_lr

        
        - mri_esm2_0

        
        - nesm3

        
        - noresm2_lm

        
        - noresm2_mm

        
        - ukesm1_0_ll

        ---

        :param period:
        :type period: str

        **Valid values:**
        
        - 19510101_20101230

        
        - 19510101_20101231

        
        - 19510101_20141230

        
        - 19510101_20141231

        
        - 20110101_21001230

        
        - 20110101_21001231

        
        - 20150101_21001230

        
        - 20150101_21001231

        
        - 184901_201412

        
        - 185001_201412

        
        - 185001_201612

        
        - 195101_201412

        
        - 201501_203912

        
        - 201501_210012

        
        - 201501_218012

        
        - 201501_230012

        
        - 1849_2014

        
        - 1850_2014

        
        - 1850_2016

        
        - 1951_2014

        
        - 2015_2039

        
        - 2015_2100

        
        - 2015_2180

        
        - 2015_2300

        ---

        :param product_type:
        :type product_type: str

        **Valid values:**
        
        - base_period_1961_1990

        
        - base_period_1981_2010

        
        - base_independent

        
        - bias_adjusted

        
        - non_bias_adjusted

        ---

        :param temporal_aggregation:
        :type temporal_aggregation: str

        **Valid values:**
        
        - yearly

        
        - monthly

        
        - daily

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - cold_days

        
        - cold_nights

        
        - cold_spell_duration_index

        
        - consecutive_dry_days

        
        - consecutive_wet_days

        
        - diurnal_temperature_range

        
        - extremely_wet_day_precipitation

        
        - frost_days

        
        - growing_season_length

        
        - heavy_precipitation_days

        
        - ice_days

        
        - maximum_1_day_precipitation

        
        - maximum_5_day_precipitation

        
        - maximum_value_of_daily_maximum_temperature

        
        - minimum_value_of_daily_maximum_temperature

        
        - maximum_value_of_daily_minimum_temperature

        
        - minimum_value_of_daily_minimum_temperature

        
        - number_of_wet_days

        
        - simple_daily_intensity_index

        
        - summer_days

        
        - total_wet_day_precipitation

        
        - tropical_nights

        
        - very_heavy_precipitation_days

        
        - very_wet_day_precipitation

        
        - warm_days

        
        - warm_nights

        
        - warm_spell_duration_index

        
        - heat_index

        
        - humidex

        
        - universal_thermal_climate_index

        
        - wet_bulb_temperature_index

        
        - wet_bulb_globe_temperature_index

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - 1_0

        
        - 2_0

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_extreme_indices_cmip6(ensemble_member: OneOrMore[str], experiment: OneOrMore[str], model: OneOrMore[str], period: OneOrMore[str], product_type: OneOrMore[str], temporal_aggregation: OneOrMore[str], variable: OneOrMore[str], version: OneOrMore[str] = '2_0'):
    return Collection_sis_extreme_indices_cmip6.download(ensemble_member=ensemble_member, experiment=experiment, model=model, period=period, product_type=product_type, temporal_aggregation=temporal_aggregation, variable=variable, version=version)

