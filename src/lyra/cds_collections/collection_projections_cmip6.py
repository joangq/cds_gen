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

class Collection_projections_cmip6(Collection):
    collection_name = 'projections-cmip6'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        experiment = ['historical', 'ssp1_1_9', 'ssp1_2_6', 'ssp4_3_4', 'ssp5_3_4os', 'ssp2_4_5', 'ssp4_6_0', 'ssp3_7_0', 'ssp5_8_5'],
        level = ['1', '5', '10', '20', '30', '50', '70', '100', '150', '200', '250', '300', '400', '500', '600', '700', '850', '925', '1000'],
        model = ['access_cm2', 'access_esm1_5', 'awi_cm_1_1_mr', 'awi_esm_1_1_lr', 'bcc_csm2_mr', 'bcc_esm1', 'cams_csm1_0', 'canesm5', 'canesm5_canoe', 'cesm2', 'cesm2_fv2', 'cesm2_waccm', 'cesm2_waccm_fv2', 'ciesm', 'cmcc_cm2_hr4', 'cmcc_cm2_sr5', 'cmcc_esm2', 'cnrm_cm6_1', 'cnrm_cm6_1_hr', 'cnrm_esm2_1', 'e3sm_1_0', 'e3sm_1_1', 'e3sm_1_1_eca', 'ec_earth3', 'ec_earth3_aerchem', 'ec_earth3_cc', 'ec_earth3_veg', 'ec_earth3_veg_lr', 'fgoals_f3_l', 'fgoals_g3', 'fio_esm_2_0', 'gfdl_esm4', 'giss_e2_1_g', 'giss_e2_1_h', 'hadgem3_gc31_ll', 'hadgem3_gc31_mm', 'iitm_esm', 'inm_cm4_8', 'inm_cm5_0', 'ipsl_cm5a2_inca', 'ipsl_cm6a_lr', 'kace_1_0_g', 'kiost_esm', 'mcm_ua_1_0', 'miroc6', 'miroc_es2h', 'miroc_es2l', 'mpi_esm_1_2_ham', 'mpi_esm1_2_hr', 'mpi_esm1_2_lr', 'mri_esm2_0', 'nesm3', 'norcpm1', 'noresm2_lm', 'noresm2_mm', 'sam0_unicon', 'taiesm1', 'ukesm1_0_ll'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        temporal_resolution = ['monthly', 'daily', 'fixed'],
        variable = ['air_temperature', 'capacity_of_soil_to_store_water', 'daily_maximum_near_surface_air_temperature', 'daily_minimum_near_surface_air_temperature', 'eastward_near_surface_wind', 'eastward_wind', 'evaporation_including_sublimation_and_transpiration', 'geopotential_height', 'grid_cell_area_for_atmospheric_grid_variables', 'grid_cell_area_for_ocean_variables', 'land_ice_area_percentage', 'moisture_in_upper_portion_of_soil_column', 'near_surface_air_temperature', 'near_surface_relative_humidity', 'near_surface_specific_humidity', 'near_surface_wind_speed', 'northward_near_surface_wind', 'northward_wind', 'percentage_of_the_grid_cell_occupied_by_land_including_lakes', 'precipitation', 'relative_humidity', 'sea_area_percentage', 'sea_floor_depth_below_geoid', 'sea_ice_thickness', 'sea_level_pressure', 'sea_surface_height_above_geoid', 'sea_surface_salinity', 'sea_surface_temperature', 'sea_ice_area_percentage_on_ocean_grid', 'sea_ice_mass_per_area', 'snow_depth', 'snowfall_flux', 'specific_humidity', 'surface_air_pressure', 'surface_altitude', 'surface_downward_eastward_wind_stress', 'surface_downward_northward_wind_stress', 'surface_downwelling_longwave_radiation', 'surface_downwelling_shortwave_radiation', 'surface_snow_amount', 'surface_temperature', 'surface_temperature_of_sea_ice', 'surface_upward_latent_heat_flux', 'surface_upward_sensible_heat_flux', 'surface_upwelling_longwave_radiation', 'surface_upwelling_shortwave_radiation', 'toa_incident_shortwave_radiation', 'toa_outgoing_longwave_radiation', 'toa_outgoing_shortwave_radiation', 'total_cloud_cover_percentage', 'total_runoff'],
        year = ['1850', '1851', '1852', '1853', '1854', '1855', '1856', '1857', '1858', '1859', '1860', '1861', '1862', '1863', '1864', '1865', '1866', '1867', '1868', '1869', '1870', '1871', '1872', '1873', '1874', '1875', '1876', '1877', '1878', '1879', '1880', '1881', '1882', '1883', '1884', '1885', '1886', '1887', '1888', '1889', '1890', '1891', '1892', '1893', '1894', '1895', '1896', '1897', '1898', '1899', '1900', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909', '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057', '2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065', '2066', '2067', '2068', '2069', '2070', '2071', '2072', '2073', '2074', '2075', '2076', '2077', '2078', '2079', '2080', '2081', '2082', '2083', '2084', '2085', '2086', '2087', '2088', '2089', '2090', '2091', '2092', '2093', '2094', '2095', '2096', '2097', '2098', '2099', '2100', '2101', '2102', '2103', '2104', '2105', '2106', '2107', '2108', '2109', '2110', '2111', '2112', '2113', '2114', '2115', '2116', '2117', '2118', '2119', '2120', '2121', '2122', '2123', '2124', '2125', '2126', '2127', '2128', '2129', '2130', '2131', '2132', '2133', '2134', '2135', '2136', '2137', '2138', '2139', '2140', '2141', '2142', '2143', '2144', '2145', '2146', '2147', '2148', '2149', '2150', '2151', '2152', '2153', '2154', '2155', '2156', '2157', '2158', '2159', '2160', '2161', '2162', '2163', '2164', '2165', '2166', '2167', '2168', '2169', '2170', '2171', '2172', '2173', '2174', '2175', '2176', '2177', '2178', '2179', '2180', '2181', '2182', '2183', '2184', '2185', '2186', '2187', '2188', '2189', '2190', '2191', '2192', '2193', '2194', '2195', '2196', '2197', '2198', '2199', '2200', '2201', '2202', '2203', '2204', '2205', '2206', '2207', '2208', '2209', '2210', '2211', '2212', '2213', '2214', '2215', '2216', '2217', '2218', '2219', '2220', '2221', '2222', '2223', '2224', '2225', '2226', '2227', '2228', '2229', '2230', '2231', '2232', '2233', '2234', '2235', '2236', '2237', '2238', '2239', '2240', '2241', '2242', '2243', '2244', '2245', '2246', '2247', '2248', '2249', '2250', '2251', '2252', '2253', '2254', '2255', '2256', '2257', '2258', '2259', '2260', '2261', '2262', '2263', '2264', '2265', '2266', '2267', '2268', '2269', '2270', '2271', '2272', '2273', '2274', '2275', '2276', '2277', '2278', '2279', '2280', '2281', '2282', '2283', '2284', '2285', '2286', '2287', '2288', '2289', '2290', '2291', '2292', '2293', '2294', '2295', '2296', '2297', '2298', '2299', '2300'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], experiment: str, level: OneOrMore[str], model: str, month: OneOrMore[str], temporal_resolution: str, variable: str, year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): 
        """
        Parameters
        ----------
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

        :param experiment:
        :type experiment: str

        **Valid values:**
        
        - historical

        
        - ssp1_1_9

        
        - ssp1_2_6

        
        - ssp4_3_4

        
        - ssp5_3_4os

        
        - ssp2_4_5

        
        - ssp4_6_0

        
        - ssp3_7_0

        
        - ssp5_8_5

        ---

        :param level:
        :type level: str

        **Valid values:**
        
        - 1

        
        - 5

        
        - 10

        
        - 20

        
        - 30

        
        - 50

        
        - 70

        
        - 100

        
        - 150

        
        - 200

        
        - 250

        
        - 300

        
        - 400

        
        - 500

        
        - 600

        
        - 700

        
        - 850

        
        - 925

        
        - 1000

        ---

        :param model:
        :type model: str

        **Valid values:**
        
        - access_cm2

        
        - access_esm1_5

        
        - awi_cm_1_1_mr

        
        - awi_esm_1_1_lr

        
        - bcc_csm2_mr

        
        - bcc_esm1

        
        - cams_csm1_0

        
        - canesm5

        
        - canesm5_canoe

        
        - cesm2

        
        - cesm2_fv2

        
        - cesm2_waccm

        
        - cesm2_waccm_fv2

        
        - ciesm

        
        - cmcc_cm2_hr4

        
        - cmcc_cm2_sr5

        
        - cmcc_esm2

        
        - cnrm_cm6_1

        
        - cnrm_cm6_1_hr

        
        - cnrm_esm2_1

        
        - e3sm_1_0

        
        - e3sm_1_1

        
        - e3sm_1_1_eca

        
        - ec_earth3

        
        - ec_earth3_aerchem

        
        - ec_earth3_cc

        
        - ec_earth3_veg

        
        - ec_earth3_veg_lr

        
        - fgoals_f3_l

        
        - fgoals_g3

        
        - fio_esm_2_0

        
        - gfdl_esm4

        
        - giss_e2_1_g

        
        - giss_e2_1_h

        
        - hadgem3_gc31_ll

        
        - hadgem3_gc31_mm

        
        - iitm_esm

        
        - inm_cm4_8

        
        - inm_cm5_0

        
        - ipsl_cm5a2_inca

        
        - ipsl_cm6a_lr

        
        - kace_1_0_g

        
        - kiost_esm

        
        - mcm_ua_1_0

        
        - miroc6

        
        - miroc_es2h

        
        - miroc_es2l

        
        - mpi_esm_1_2_ham

        
        - mpi_esm1_2_hr

        
        - mpi_esm1_2_lr

        
        - mri_esm2_0

        
        - nesm3

        
        - norcpm1

        
        - noresm2_lm

        
        - noresm2_mm

        
        - sam0_unicon

        
        - taiesm1

        
        - ukesm1_0_ll

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

        
        - fixed

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - air_temperature

        
        - capacity_of_soil_to_store_water

        
        - daily_maximum_near_surface_air_temperature

        
        - daily_minimum_near_surface_air_temperature

        
        - eastward_near_surface_wind

        
        - eastward_wind

        
        - evaporation_including_sublimation_and_transpiration

        
        - geopotential_height

        
        - grid_cell_area_for_atmospheric_grid_variables

        
        - grid_cell_area_for_ocean_variables

        
        - land_ice_area_percentage

        
        - moisture_in_upper_portion_of_soil_column

        
        - near_surface_air_temperature

        
        - near_surface_relative_humidity

        
        - near_surface_specific_humidity

        
        - near_surface_wind_speed

        
        - northward_near_surface_wind

        
        - northward_wind

        
        - percentage_of_the_grid_cell_occupied_by_land_including_lakes

        
        - precipitation

        
        - relative_humidity

        
        - sea_area_percentage

        
        - sea_floor_depth_below_geoid

        
        - sea_ice_thickness

        
        - sea_level_pressure

        
        - sea_surface_height_above_geoid

        
        - sea_surface_salinity

        
        - sea_surface_temperature

        
        - sea_ice_area_percentage_on_ocean_grid

        
        - sea_ice_mass_per_area

        
        - snow_depth

        
        - snowfall_flux

        
        - specific_humidity

        
        - surface_air_pressure

        
        - surface_altitude

        
        - surface_downward_eastward_wind_stress

        
        - surface_downward_northward_wind_stress

        
        - surface_downwelling_longwave_radiation

        
        - surface_downwelling_shortwave_radiation

        
        - surface_snow_amount

        
        - surface_temperature

        
        - surface_temperature_of_sea_ice

        
        - surface_upward_latent_heat_flux

        
        - surface_upward_sensible_heat_flux

        
        - surface_upwelling_longwave_radiation

        
        - surface_upwelling_shortwave_radiation

        
        - toa_incident_shortwave_radiation

        
        - toa_outgoing_longwave_radiation

        
        - toa_outgoing_shortwave_radiation

        
        - total_cloud_cover_percentage

        
        - total_runoff

        ---

        :param year:
        :type year: str

        **Valid values:**
        
        - 1850

        
        - 1851

        
        - 1852

        
        - 1853

        
        - 1854

        
        - 1855

        
        - 1856

        
        - 1857

        
        - 1858

        
        - 1859

        
        - 1860

        
        - 1861

        
        - 1862

        
        - 1863

        
        - 1864

        
        - 1865

        
        - 1866

        
        - 1867

        
        - 1868

        
        - 1869

        
        - 1870

        
        - 1871

        
        - 1872

        
        - 1873

        
        - 1874

        
        - 1875

        
        - 1876

        
        - 1877

        
        - 1878

        
        - 1879

        
        - 1880

        
        - 1881

        
        - 1882

        
        - 1883

        
        - 1884

        
        - 1885

        
        - 1886

        
        - 1887

        
        - 1888

        
        - 1889

        
        - 1890

        
        - 1891

        
        - 1892

        
        - 1893

        
        - 1894

        
        - 1895

        
        - 1896

        
        - 1897

        
        - 1898

        
        - 1899

        
        - 1900

        
        - 1901

        
        - 1902

        
        - 1903

        
        - 1904

        
        - 1905

        
        - 1906

        
        - 1907

        
        - 1908

        
        - 1909

        
        - 1910

        
        - 1911

        
        - 1912

        
        - 1913

        
        - 1914

        
        - 1915

        
        - 1916

        
        - 1917

        
        - 1918

        
        - 1919

        
        - 1920

        
        - 1921

        
        - 1922

        
        - 1923

        
        - 1924

        
        - 1925

        
        - 1926

        
        - 1927

        
        - 1928

        
        - 1929

        
        - 1930

        
        - 1931

        
        - 1932

        
        - 1933

        
        - 1934

        
        - 1935

        
        - 1936

        
        - 1937

        
        - 1938

        
        - 1939

        
        - 1940

        
        - 1941

        
        - 1942

        
        - 1943

        
        - 1944

        
        - 1945

        
        - 1946

        
        - 1947

        
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

        
        - 2101

        
        - 2102

        
        - 2103

        
        - 2104

        
        - 2105

        
        - 2106

        
        - 2107

        
        - 2108

        
        - 2109

        
        - 2110

        
        - 2111

        
        - 2112

        
        - 2113

        
        - 2114

        
        - 2115

        
        - 2116

        
        - 2117

        
        - 2118

        
        - 2119

        
        - 2120

        
        - 2121

        
        - 2122

        
        - 2123

        
        - 2124

        
        - 2125

        
        - 2126

        
        - 2127

        
        - 2128

        
        - 2129

        
        - 2130

        
        - 2131

        
        - 2132

        
        - 2133

        
        - 2134

        
        - 2135

        
        - 2136

        
        - 2137

        
        - 2138

        
        - 2139

        
        - 2140

        
        - 2141

        
        - 2142

        
        - 2143

        
        - 2144

        
        - 2145

        
        - 2146

        
        - 2147

        
        - 2148

        
        - 2149

        
        - 2150

        
        - 2151

        
        - 2152

        
        - 2153

        
        - 2154

        
        - 2155

        
        - 2156

        
        - 2157

        
        - 2158

        
        - 2159

        
        - 2160

        
        - 2161

        
        - 2162

        
        - 2163

        
        - 2164

        
        - 2165

        
        - 2166

        
        - 2167

        
        - 2168

        
        - 2169

        
        - 2170

        
        - 2171

        
        - 2172

        
        - 2173

        
        - 2174

        
        - 2175

        
        - 2176

        
        - 2177

        
        - 2178

        
        - 2179

        
        - 2180

        
        - 2181

        
        - 2182

        
        - 2183

        
        - 2184

        
        - 2185

        
        - 2186

        
        - 2187

        
        - 2188

        
        - 2189

        
        - 2190

        
        - 2191

        
        - 2192

        
        - 2193

        
        - 2194

        
        - 2195

        
        - 2196

        
        - 2197

        
        - 2198

        
        - 2199

        
        - 2200

        
        - 2201

        
        - 2202

        
        - 2203

        
        - 2204

        
        - 2205

        
        - 2206

        
        - 2207

        
        - 2208

        
        - 2209

        
        - 2210

        
        - 2211

        
        - 2212

        
        - 2213

        
        - 2214

        
        - 2215

        
        - 2216

        
        - 2217

        
        - 2218

        
        - 2219

        
        - 2220

        
        - 2221

        
        - 2222

        
        - 2223

        
        - 2224

        
        - 2225

        
        - 2226

        
        - 2227

        
        - 2228

        
        - 2229

        
        - 2230

        
        - 2231

        
        - 2232

        
        - 2233

        
        - 2234

        
        - 2235

        
        - 2236

        
        - 2237

        
        - 2238

        
        - 2239

        
        - 2240

        
        - 2241

        
        - 2242

        
        - 2243

        
        - 2244

        
        - 2245

        
        - 2246

        
        - 2247

        
        - 2248

        
        - 2249

        
        - 2250

        
        - 2251

        
        - 2252

        
        - 2253

        
        - 2254

        
        - 2255

        
        - 2256

        
        - 2257

        
        - 2258

        
        - 2259

        
        - 2260

        
        - 2261

        
        - 2262

        
        - 2263

        
        - 2264

        
        - 2265

        
        - 2266

        
        - 2267

        
        - 2268

        
        - 2269

        
        - 2270

        
        - 2271

        
        - 2272

        
        - 2273

        
        - 2274

        
        - 2275

        
        - 2276

        
        - 2277

        
        - 2278

        
        - 2279

        
        - 2280

        
        - 2281

        
        - 2282

        
        - 2283

        
        - 2284

        
        - 2285

        
        - 2286

        
        - 2287

        
        - 2288

        
        - 2289

        
        - 2290

        
        - 2291

        
        - 2292

        
        - 2293

        
        - 2294

        
        - 2295

        
        - 2296

        
        - 2297

        
        - 2298

        
        - 2299

        
        - 2300

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

def download_projections_cmip6(day: OneOrMore[str], experiment: str, level: OneOrMore[str], model: str, month: OneOrMore[str], temporal_resolution: str, variable: str, year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
    return Collection_projections_cmip6.download(day=day, experiment=experiment, level=level, model=model, month=month, temporal_resolution=temporal_resolution, variable=variable, year=year, area_group=area_group)

