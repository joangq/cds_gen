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

class Collection_sis_marine_properties(Collection):
    collection_name = 'sis-marine-properties'
    valid_values = dict(
        experiment = ['rcp4_5', 'rcp8_5'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        origin = ['nemo_ersem', 'polcoms_ersem'],
        time_aggregation = ['day', 'month'],
        variable = ['apparent_oxygen_utilisation', 'total_chlorophyll_a', 'euphotic_zone_chlorophyll_a', 'euphotic_zone_depth', 'mole_concentration_of_nitrate_and_nitrite', 'mole_concentration_of_dissolved_oxygen', 'potential_energy_anomaly', 'sea_water_ph', 'phytoplankton_carbon', 'mole_concentration_of_phosphate', 'net_primary_production', 'saturation_state_of_aragonite', 'mole_concentration_of_silicate', 'sea_water_salinity', 'sea_water_potential_temperature', 'organic_carbon_in_the_water_column', 'u_component_of_water_velocity', 'v_component_of_water_velocity', 'zooplankton_carbon', 'secondary_production'],
        vertical_resolution = ['surface', 'water_column'],
        year = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057', '2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065', '2066', '2067', '2068', '2069', '2070', '2071', '2072', '2073', '2074', '2075', '2076', '2077', '2078', '2079', '2080', '2081', '2082', '2083', '2084', '2085', '2086', '2087', '2088', '2089', '2090', '2091', '2092', '2093', '2094', '2095', '2096', '2097', '2098', '2099'],
    )

    @Collection.wrapper
    def download(cls, experiment: OneOrMore[str], month: OneOrMore[str], origin: str, time_aggregation: str, variable: OneOrMore[str], vertical_resolution: str, year: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param experiment:
        :type experiment: str

        **Valid values:**
        
        - rcp4_5

        
        - rcp8_5

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
        
        - nemo_ersem

        
        - polcoms_ersem

        ---

        :param time_aggregation:
        :type time_aggregation: str

        **Valid values:**
        
        - day

        
        - month

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - apparent_oxygen_utilisation

        
        - total_chlorophyll_a

        
        - euphotic_zone_chlorophyll_a

        
        - euphotic_zone_depth

        
        - mole_concentration_of_nitrate_and_nitrite

        
        - mole_concentration_of_dissolved_oxygen

        
        - potential_energy_anomaly

        
        - sea_water_ph

        
        - phytoplankton_carbon

        
        - mole_concentration_of_phosphate

        
        - net_primary_production

        
        - saturation_state_of_aragonite

        
        - mole_concentration_of_silicate

        
        - sea_water_salinity

        
        - sea_water_potential_temperature

        
        - organic_carbon_in_the_water_column

        
        - u_component_of_water_velocity

        
        - v_component_of_water_velocity

        
        - zooplankton_carbon

        
        - secondary_production

        ---

        :param vertical_resolution:
        :type vertical_resolution: str

        **Valid values:**
        
        - surface

        
        - water_column

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_marine_properties(experiment: OneOrMore[str], month: OneOrMore[str], origin: str, time_aggregation: str, variable: OneOrMore[str], vertical_resolution: str, year: OneOrMore[str]):
    return Collection_sis_marine_properties.download(experiment=experiment, month=month, origin=origin, time_aggregation=time_aggregation, variable=variable, vertical_resolution=vertical_resolution, year=year)

