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

class Collection_sis_hydrology_variables_derived_projections(Collection):
    collection_name = 'sis-hydrology-variables-derived-projections'
    valid_values = dict(
        ensemble_member = ['r1i1p1', 'r12i1p1', 'r2i1p1'],
        experiment = ['historical', 'rcp_2_6', 'rcp_4_5', 'rcp_8_5', 'degree_scenario'],
        gcm = ['hadgem2_es', 'mpi_esm_lr', 'ec_earth'],
        hydrological_model = ['e_hypecatch_m00', 'e_hypecatch_m01', 'e_hypecatch_m02', 'e_hypecatch_m03', 'e_hypecatch_m04', 'e_hypecatch_m05', 'e_hypecatch_m06', 'e_hypecatch_m07', 'e_hypegrid', 'vic_wur'],
        period = ['1971_2000', '2011_2040', '2041_2070', '2071_2100', '1971_1980', '1981_1990', '1991_2000', '2001_2005', '2006_2010', '2011_2020', '2021_2030', '2031_2040', '2041_2050', '2051_2060', '2061_2070', '2071_2080', '2081_2090', '2091_2100', '1_5_c', '2_0_c', '3_0_c', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057', '2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065', '2066', '2067', '2068', '2069', '2070', '2071', '2072', '2073', '2074', '2075', '2076', '2077', '2078', '2079', '2080', '2081', '2082', '2083', '2084', '2085', '2086', '2087', '2088', '2089', '2090', '2091', '2092', '2093', '2094', '2095', '2096', '2097', '2098', '2099', '2100'],
        product_type = ['climate_impact_indicators', 'essential_climate_variables'],
        rcm = ['cclm4_8_17', 'racmo22e', 'csc_remo2009', 'rca4'],
        time_aggregation = ['daily', 'monthly_mean', 'annual_mean'],
        variable = ['river_discharge', 'mean_runoff', 'flood_recurrence_2_years_return_period', 'flood_recurrence_5_years_return_period', 'flood_recurrence_10_years_return_period', 'flood_recurrence_50_years_return_period', 'maximum_river_discharge', 'minimum_river_discharge', 'mean_soil_moisture', 'wetness_actual', 'wetness_potential', 'water_temperature_in_catchments', 'water_temperature_in_local_streams', 'aridity_potential', 'aridity_actual', 'total_nitrogen_concentration_in_catchments', 'total_nitrogen_load_in_catchments', 'total_nitrogen_concentration_in_local_streams', 'total_phosphorus_concentration_in_catchments', 'total_phosphorus_load_in_catchments', 'total_phosphorus_concentration_in_local_streams'],
        variable_type = ['relative_change_from_reference_period', 'absolute_change_from_reference_period', 'absolute_values'],
    )

    @Collection.wrapper
    def download(cls, ensemble_member: OneOrMore[str], experiment: OneOrMore[str], gcm: str, hydrological_model: OneOrMore[str], period: OneOrMore[str], product_type: str, rcm: str, time_aggregation: str, variable: OneOrMore[str], variable_type: str): 
        """
        Parameters
        ----------
        :param ensemble_member:
        :type ensemble_member: str

        **Valid values:**
        
        - r1i1p1

        
        - r12i1p1

        
        - r2i1p1

        ---

        :param experiment:
        :type experiment: str

        **Valid values:**
        
        - historical

        
        - rcp_2_6

        
        - rcp_4_5

        
        - rcp_8_5

        
        - degree_scenario

        ---

        :param gcm:
        :type gcm: str

        **Valid values:**
        
        - hadgem2_es

        
        - mpi_esm_lr

        
        - ec_earth

        ---

        :param hydrological_model:
        :type hydrological_model: str

        **Valid values:**
        
        - e_hypecatch_m00

        
        - e_hypecatch_m01

        
        - e_hypecatch_m02

        
        - e_hypecatch_m03

        
        - e_hypecatch_m04

        
        - e_hypecatch_m05

        
        - e_hypecatch_m06

        
        - e_hypecatch_m07

        
        - e_hypegrid

        
        - vic_wur

        ---

        :param period:
        :type period: str

        **Valid values:**
        
        - 1971_2000

        
        - 2011_2040

        
        - 2041_2070

        
        - 2071_2100

        
        - 1971_1980

        
        - 1981_1990

        
        - 1991_2000

        
        - 2001_2005

        
        - 2006_2010

        
        - 2011_2020

        
        - 2021_2030

        
        - 2031_2040

        
        - 2041_2050

        
        - 2051_2060

        
        - 2061_2070

        
        - 2071_2080

        
        - 2081_2090

        
        - 2091_2100

        
        - 1_5_c

        
        - 2_0_c

        
        - 3_0_c

        
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

        
        - 2032

        
        - 2033

        
        - 2034

        
        - 2035

        
        - 2036

        
        - 2037

        
        - 2038

        
        - 2039

        
        - 2040

        
        - 2041

        
        - 2042

        
        - 2043

        
        - 2044

        
        - 2045

        
        - 2046

        
        - 2047

        
        - 2048

        
        - 2049

        
        - 2050

        
        - 2051

        
        - 2052

        
        - 2053

        
        - 2054

        
        - 2055

        
        - 2056

        
        - 2057

        
        - 2058

        
        - 2059

        
        - 2060

        
        - 2061

        
        - 2062

        
        - 2063

        
        - 2064

        
        - 2065

        
        - 2066

        
        - 2067

        
        - 2068

        
        - 2069

        
        - 2070

        
        - 2071

        
        - 2072

        
        - 2073

        
        - 2074

        
        - 2075

        
        - 2076

        
        - 2077

        
        - 2078

        
        - 2079

        
        - 2080

        
        - 2081

        
        - 2082

        
        - 2083

        
        - 2084

        
        - 2085

        
        - 2086

        
        - 2087

        
        - 2088

        
        - 2089

        
        - 2090

        
        - 2091

        
        - 2092

        
        - 2093

        
        - 2094

        
        - 2095

        
        - 2096

        
        - 2097

        
        - 2098

        
        - 2099

        
        - 2100

        ---

        :param product_type:
        :type product_type: str

        **Valid values:**
        
        - climate_impact_indicators

        
        - essential_climate_variables

        ---

        :param rcm:
        :type rcm: str

        **Valid values:**
        
        - cclm4_8_17

        
        - racmo22e

        
        - csc_remo2009

        
        - rca4

        ---

        :param time_aggregation:
        :type time_aggregation: str

        **Valid values:**
        
        - daily

        
        - monthly_mean

        
        - annual_mean

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - river_discharge

        
        - mean_runoff

        
        - flood_recurrence_2_years_return_period

        
        - flood_recurrence_5_years_return_period

        
        - flood_recurrence_10_years_return_period

        
        - flood_recurrence_50_years_return_period

        
        - maximum_river_discharge

        
        - minimum_river_discharge

        
        - mean_soil_moisture

        
        - wetness_actual

        
        - wetness_potential

        
        - water_temperature_in_catchments

        
        - water_temperature_in_local_streams

        
        - aridity_potential

        
        - aridity_actual

        
        - total_nitrogen_concentration_in_catchments

        
        - total_nitrogen_load_in_catchments

        
        - total_nitrogen_concentration_in_local_streams

        
        - total_phosphorus_concentration_in_catchments

        
        - total_phosphorus_load_in_catchments

        
        - total_phosphorus_concentration_in_local_streams

        ---

        :param variable_type:
        :type variable_type: str

        **Valid values:**
        
        - relative_change_from_reference_period

        
        - absolute_change_from_reference_period

        
        - absolute_values

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_hydrology_variables_derived_projections(ensemble_member: OneOrMore[str], experiment: OneOrMore[str], gcm: str, hydrological_model: OneOrMore[str], period: OneOrMore[str], product_type: str, rcm: str, time_aggregation: str, variable: OneOrMore[str], variable_type: str):
    return Collection_sis_hydrology_variables_derived_projections.download(ensemble_member=ensemble_member, experiment=experiment, gcm=gcm, hydrological_model=hydrological_model, period=period, product_type=product_type, rcm=rcm, time_aggregation=time_aggregation, variable=variable, variable_type=variable_type)

