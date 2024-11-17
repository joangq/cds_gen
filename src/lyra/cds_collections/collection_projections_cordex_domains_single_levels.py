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

class Collection_projections_cordex_domains_single_levels(Collection):
    collection_name = 'projections-cordex-domains-single-levels'
    valid_values = dict(
        domain = ['africa', 'antarctic', 'arctic', 'australasia', 'central_america', 'central_asia', 'east_asia', 'europe', 'mediterranean', 'middle_east_and_north_africa', 'north_america', 'south_america', 'south_east_asia', 'south_asia'],
        end_year = ['1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057', '2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065', '2066', '2067', '2068', '2069', '2070', '2071', '2072', '2073', '2074', '2075', '2076', '2077', '2078', '2079', '2080', '2081', '2082', '2083', '2084', '2085', '2086', '2087', '2088', '2089', '2090', '2091', '2092', '2093', '2094', '2095', '2096', '2097', '2098', '2099', '2100', '2101'],
        ensemble_member = ['r1i1p1', 'r2i1p1', 'r3i1p1', 'r6i1p1', 'r12i1p1', 'r0i0p0'],
        experiment = ['evaluation', 'historical', 'rcp_2_6', 'rcp_4_5', 'rcp_8_5'],
        gcm_model = ['cccma_canesm2', 'cnrm_cerfacs_cm5', 'csiro_bom_access1_0', 'csiro_bom_access1_3', 'csiro_qccce_csiro_mk3_6_0', 'era_interim', 'ichec_ec_earth', 'ipsl_cm5a_lr', 'ipsl_cm5a_mr', 'miroc_miroc5', 'mohc_hadgem2_es', 'mpi_m_mpi_esm_lr', 'mpi_m_mpi_esm_mr', 'ncar_ccsm4', 'ncc_noresm1_m', 'noaa_gfdl_gfdl_esm2g', 'noaa_gfdl_esm2m'],
        horizontal_resolution = ['0_11_degree_x_0_11_degree', '0_20_degree_x_0_20_degree', '0_22_degree_x_0_22_degree', '0_44_degree_x_0_44_degree', 'interpolated_0_44_degree_x_0_44_degree'],
        rcm_model = ['awi_hirham5', 'bccr_wrf331', 'boun_regcm4_3', 'cccma_canrcm4', 'clmcom_btu_cclm4_8_17', 'clmcom_clm_cclm4_8_17', 'clmcom_cclm4_8_17_clm3_5', 'clmcom_cclm5_0_2', 'clmcom_eth_cosmo_crclim', 'clmcom_hzg_cclm5_0_15', 'clmcom_kit_cclm5_0_15', 'cmcc_cclm4_8_19', 'cnrm_aladin52', 'cnrm_aladin53', 'cnrm_aladin63', 'csiro_ccam_2008', 'cyi_wrf351', 'dmi_hirham5', 'elu_regcm4_3', 'gerics_remo2009', 'gerics_remo2015', 'guf_cclm4_8_18_germany', 'ictp_regcm4_3', 'ictp_regcm4_4', 'ictp_regcm4_6', 'ictp_regcm4_7', 'iitm_regcm4_4', 'inpe_eta', 'ipsl_wrf381p', 'isu_regcm4', 'knmi_racmo21p', 'knmi_racmo22e', 'knmi_racmo22t', 'lmd_lmdz4nemomed8', 'mgo_rrcm', 'mohc_hadrem3_ga7_05', 'mohc_hadrm3p', 'mpi_csc_remo2009', 'ncar_regcm4', 'ncar_wrf', 'ornl_regcm4_7', 'ouranos_crcm5', 'rmib_ugent_alaro_0', 'ru_core_regcm4_3', 'smhi_rca4', 'smhi_rca4_sn', 'ua_wrf', 'ucan_wrf341i', 'uhoh_wrf361h', 'ulg_mar311', 'ulg_mar36', 'unsw_wrf360j', 'unsw_wrf360k', 'unsw_wrf360l', 'uqam_crcm5', 'uqam_crcm5_sn'],
        start_year = ['1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057', '2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065', '2066', '2067', '2068', '2069', '2070', '2071', '2072', '2073', '2074', '2075', '2076', '2077', '2078', '2079', '2080', '2081', '2082', '2083', '2084', '2085', '2086', '2087', '2088', '2089', '2090', '2091', '2092', '2093', '2094', '2095', '2096', '2097', '2098', '2099', '2100'],
        temporal_resolution = ['daily_mean', 'monthly_mean', 'seasonal_mean', '3_hours', '6_hours', 'fixed'],
        variable = ['2m_air_temperature', '2m_relative_humidity', '2m_surface_specific_humidity', '10m_u_component_of_the_wind', '10m_v_component_of_the_wind', '10m_wind_speed', 'maximum_2m_temperature_in_the_last_24_hours', 'minimum_2m_temperature_in_the_last_24_hours', '200hpa_temperature', '200hpa_u_component_of_the_wind', '200hpa_v_component_of_the_wind', '500hpa_geopotential_height', '850hpa_u_component_of_the_wind', '850hpa_v_component_of_the_wind', 'evaporation', 'land_area_fraction', 'mean_sea_level_pressure', 'mean_precipitation_flux', 'orography', 'surface_pressure', 'surface_solar_radiation_downwards', 'surface_thermal_radiation_downward', 'surface_upwelling_shortwave_radiation', 'total_cloud_cover', 'total_run_off_flux'],
    )

    @Collection.wrapper
    def download(cls, domain: str, end_year: OneOrMore[str], ensemble_member: str, experiment: str, gcm_model: str, horizontal_resolution: str, rcm_model: str, start_year: OneOrMore[str], temporal_resolution: str, variable: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param domain:
        :type domain: str

        **Valid values:**
        
        - africa

        
        - antarctic

        
        - arctic

        
        - australasia

        
        - central_america

        
        - central_asia

        
        - east_asia

        
        - europe

        
        - mediterranean

        
        - middle_east_and_north_africa

        
        - north_america

        
        - south_america

        
        - south_east_asia

        
        - south_asia

        ---

        :param end_year:
        :type end_year: str

        **Valid values:**
        
        - 1949

        
        - 1950

        
        - 1951

        
        - 1952

        
        - 1953

        
        - 1954

        
        - 1955

        
        - 1956

        
        - 1957

        
        - 1958

        
        - 1959

        
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

        
        - 2101

        ---

        :param ensemble_member:
        :type ensemble_member: str

        **Valid values:**
        
        - r1i1p1

        
        - r2i1p1

        
        - r3i1p1

        
        - r6i1p1

        
        - r12i1p1

        
        - r0i0p0

        ---

        :param experiment:
        :type experiment: str

        **Valid values:**
        
        - evaluation

        
        - historical

        
        - rcp_2_6

        
        - rcp_4_5

        
        - rcp_8_5

        ---

        :param gcm_model:
        :type gcm_model: str

        **Valid values:**
        
        - cccma_canesm2

        
        - cnrm_cerfacs_cm5

        
        - csiro_bom_access1_0

        
        - csiro_bom_access1_3

        
        - csiro_qccce_csiro_mk3_6_0

        
        - era_interim

        
        - ichec_ec_earth

        
        - ipsl_cm5a_lr

        
        - ipsl_cm5a_mr

        
        - miroc_miroc5

        
        - mohc_hadgem2_es

        
        - mpi_m_mpi_esm_lr

        
        - mpi_m_mpi_esm_mr

        
        - ncar_ccsm4

        
        - ncc_noresm1_m

        
        - noaa_gfdl_gfdl_esm2g

        
        - noaa_gfdl_esm2m

        ---

        :param horizontal_resolution:
        :type horizontal_resolution: str

        **Valid values:**
        
        - 0_11_degree_x_0_11_degree

        
        - 0_20_degree_x_0_20_degree

        
        - 0_22_degree_x_0_22_degree

        
        - 0_44_degree_x_0_44_degree

        
        - interpolated_0_44_degree_x_0_44_degree

        ---

        :param rcm_model:
        :type rcm_model: str

        **Valid values:**
        
        - awi_hirham5

        
        - bccr_wrf331

        
        - boun_regcm4_3

        
        - cccma_canrcm4

        
        - clmcom_btu_cclm4_8_17

        
        - clmcom_clm_cclm4_8_17

        
        - clmcom_cclm4_8_17_clm3_5

        
        - clmcom_cclm5_0_2

        
        - clmcom_eth_cosmo_crclim

        
        - clmcom_hzg_cclm5_0_15

        
        - clmcom_kit_cclm5_0_15

        
        - cmcc_cclm4_8_19

        
        - cnrm_aladin52

        
        - cnrm_aladin53

        
        - cnrm_aladin63

        
        - csiro_ccam_2008

        
        - cyi_wrf351

        
        - dmi_hirham5

        
        - elu_regcm4_3

        
        - gerics_remo2009

        
        - gerics_remo2015

        
        - guf_cclm4_8_18_germany

        
        - ictp_regcm4_3

        
        - ictp_regcm4_4

        
        - ictp_regcm4_6

        
        - ictp_regcm4_7

        
        - iitm_regcm4_4

        
        - inpe_eta

        
        - ipsl_wrf381p

        
        - isu_regcm4

        
        - knmi_racmo21p

        
        - knmi_racmo22e

        
        - knmi_racmo22t

        
        - lmd_lmdz4nemomed8

        
        - mgo_rrcm

        
        - mohc_hadrem3_ga7_05

        
        - mohc_hadrm3p

        
        - mpi_csc_remo2009

        
        - ncar_regcm4

        
        - ncar_wrf

        
        - ornl_regcm4_7

        
        - ouranos_crcm5

        
        - rmib_ugent_alaro_0

        
        - ru_core_regcm4_3

        
        - smhi_rca4

        
        - smhi_rca4_sn

        
        - ua_wrf

        
        - ucan_wrf341i

        
        - uhoh_wrf361h

        
        - ulg_mar311

        
        - ulg_mar36

        
        - unsw_wrf360j

        
        - unsw_wrf360k

        
        - unsw_wrf360l

        
        - uqam_crcm5

        
        - uqam_crcm5_sn

        ---

        :param start_year:
        :type start_year: str

        **Valid values:**
        
        - 1948

        
        - 1949

        
        - 1950

        
        - 1951

        
        - 1952

        
        - 1953

        
        - 1954

        
        - 1955

        
        - 1956

        
        - 1957

        
        - 1958

        
        - 1959

        
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

        :param temporal_resolution:
        :type temporal_resolution: str

        **Valid values:**
        
        - daily_mean

        
        - monthly_mean

        
        - seasonal_mean

        
        - 3_hours

        
        - 6_hours

        
        - fixed

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - 2m_air_temperature

        
        - 2m_relative_humidity

        
        - 2m_surface_specific_humidity

        
        - 10m_u_component_of_the_wind

        
        - 10m_v_component_of_the_wind

        
        - 10m_wind_speed

        
        - maximum_2m_temperature_in_the_last_24_hours

        
        - minimum_2m_temperature_in_the_last_24_hours

        
        - 200hpa_temperature

        
        - 200hpa_u_component_of_the_wind

        
        - 200hpa_v_component_of_the_wind

        
        - 500hpa_geopotential_height

        
        - 850hpa_u_component_of_the_wind

        
        - 850hpa_v_component_of_the_wind

        
        - evaporation

        
        - land_area_fraction

        
        - mean_sea_level_pressure

        
        - mean_precipitation_flux

        
        - orography

        
        - surface_pressure

        
        - surface_solar_radiation_downwards

        
        - surface_thermal_radiation_downward

        
        - surface_upwelling_shortwave_radiation

        
        - total_cloud_cover

        
        - total_run_off_flux

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_projections_cordex_domains_single_levels(domain: str, end_year: OneOrMore[str], ensemble_member: str, experiment: str, gcm_model: str, horizontal_resolution: str, rcm_model: str, start_year: OneOrMore[str], temporal_resolution: str, variable: OneOrMore[str]):
    return Collection_projections_cordex_domains_single_levels.download(domain=domain, end_year=end_year, ensemble_member=ensemble_member, experiment=experiment, gcm_model=gcm_model, horizontal_resolution=horizontal_resolution, rcm_model=rcm_model, start_year=start_year, temporal_resolution=temporal_resolution, variable=variable)

