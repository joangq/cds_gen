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

class Collection_derived_era5_single_levels_daily_statistics(Collection):
    collection_name = 'derived-era5-single-levels-daily-statistics'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        variable = ['10m_u_component_of_wind', '10m_v_component_of_wind', '2m_dewpoint_temperature', '2m_temperature', 'mean_sea_level_pressure', 'mean_wave_direction', 'mean_wave_period', 'sea_surface_temperature', 'significant_height_of_combined_wind_waves_and_swell', 'surface_pressure', 'total_precipitation', '2m_dewpoint_temperature', '2m_temperature', 'ice_temperature_layer_1', 'ice_temperature_layer_2', 'ice_temperature_layer_3', 'ice_temperature_layer_4', 'maximum_2m_temperature_since_previous_post_processing', 'mean_sea_level_pressure', 'minimum_2m_temperature_since_previous_post_processing', 'sea_surface_temperature', 'skin_temperature', 'surface_pressure', '100m_u_component_of_wind', '100m_v_component_of_wind', '10m_u_component_of_neutral_wind', '10m_u_component_of_wind', '10m_v_component_of_neutral_wind', '10m_v_component_of_wind', '10m_wind_gust_since_previous_post_processing', 'instantaneous_10m_wind_gust', 'mean_boundary_layer_dissipation', 'mean_convective_precipitation_rate', 'mean_convective_snowfall_rate', 'mean_eastward_gravity_wave_surface_stress', 'mean_eastward_turbulent_surface_stress', 'mean_evaporation_rate', 'mean_gravity_wave_dissipation', 'mean_large_scale_precipitation_fraction', 'mean_large_scale_precipitation_rate', 'mean_large_scale_snowfall_rate', 'mean_northward_gravity_wave_surface_stress', 'mean_northward_turbulent_surface_stress', 'mean_potential_evaporation_rate', 'mean_runoff_rate', 'mean_snow_evaporation_rate', 'mean_snowfall_rate', 'mean_snowmelt_rate', 'mean_sub_surface_runoff_rate', 'mean_surface_direct_short_wave_radiation_flux', 'mean_surface_direct_short_wave_radiation_flux_clear_sky', 'mean_surface_downward_long_wave_radiation_flux', 'mean_surface_downward_long_wave_radiation_flux_clear_sky', 'mean_surface_downward_short_wave_radiation_flux', 'mean_surface_downward_short_wave_radiation_flux_clear_sky', 'mean_surface_downward_uv_radiation_flux', 'mean_surface_latent_heat_flux', 'mean_surface_net_long_wave_radiation_flux', 'mean_surface_net_long_wave_radiation_flux_clear_sky', 'mean_surface_net_short_wave_radiation_flux', 'mean_surface_net_short_wave_radiation_flux_clear_sky', 'mean_surface_runoff_rate', 'mean_surface_sensible_heat_flux', 'mean_top_downward_short_wave_radiation_flux', 'mean_top_net_long_wave_radiation_flux', 'mean_top_net_long_wave_radiation_flux_clear_sky', 'mean_top_net_short_wave_radiation_flux', 'mean_top_net_short_wave_radiation_flux_clear_sky', 'mean_total_precipitation_rate', 'mean_vertically_integrated_moisture_divergence', 'clear_sky_direct_solar_radiation_at_surface', 'downward_uv_radiation_at_the_surface', 'forecast_logarithm_of_surface_roughness_for_heat', 'instantaneous_surface_sensible_heat_flux', 'near_ir_albedo_for_diffuse_radiation', 'near_ir_albedo_for_direct_radiation', 'surface_latent_heat_flux', 'surface_net_solar_radiation', 'surface_net_solar_radiation_clear_sky', 'surface_net_thermal_radiation', 'surface_net_thermal_radiation_clear_sky', 'surface_sensible_heat_flux', 'surface_solar_radiation_downward_clear_sky', 'surface_solar_radiation_downwards', 'surface_thermal_radiation_downward_clear_sky', 'surface_thermal_radiation_downwards', 'toa_incident_solar_radiation', 'top_net_solar_radiation', 'top_net_solar_radiation_clear_sky', 'top_net_thermal_radiation', 'top_net_thermal_radiation_clear_sky', 'total_sky_direct_solar_radiation_at_surface', 'uv_visible_albedo_for_diffuse_radiation', 'uv_visible_albedo_for_direct_radiation', 'cloud_base_height', 'high_cloud_cover', 'low_cloud_cover', 'medium_cloud_cover', 'total_cloud_cover', 'total_column_cloud_ice_water', 'total_column_cloud_liquid_water', 'vertical_integral_of_divergence_of_cloud_frozen_water_flux', 'vertical_integral_of_divergence_of_cloud_liquid_water_flux', 'vertical_integral_of_eastward_cloud_frozen_water_flux', 'vertical_integral_of_eastward_cloud_liquid_water_flux', 'vertical_integral_of_northward_cloud_frozen_water_flux', 'vertical_integral_of_northward_cloud_liquid_water_flux', 'lake_bottom_temperature', 'lake_cover', 'lake_depth', 'lake_ice_depth', 'lake_ice_temperature', 'lake_mix_layer_depth', 'lake_mix_layer_temperature', 'lake_shape_factor', 'lake_total_layer_temperature', 'evaporation', 'potential_evaporation', 'runoff', 'sub_surface_runoff', 'surface_runoff', 'convective_precipitation', 'convective_rain_rate', 'instantaneous_large_scale_surface_precipitation_fraction', 'large_scale_rain_rate', 'large_scale_precipitation', 'large_scale_precipitation_fraction', 'maximum_total_precipitation_rate_since_previous_post_processing', 'minimum_total_precipitation_rate_since_previous_post_processing', 'precipitation_type', 'total_column_rain_water', 'total_precipitation', 'convective_snowfall', 'convective_snowfall_rate_water_equivalent', 'large_scale_snowfall_rate_water_equivalent', 'large_scale_snowfall', 'snow_albedo', 'snow_density', 'snow_depth', 'snow_evaporation', 'snowfall', 'snowmelt', 'temperature_of_snow_layer', 'total_column_snow_water', 'soil_temperature_level_1', 'soil_temperature_level_2', 'soil_temperature_level_3', 'soil_temperature_level_4', 'soil_type', 'volumetric_soil_water_layer_1', 'volumetric_soil_water_layer_2', 'volumetric_soil_water_layer_3', 'volumetric_soil_water_layer_4', 'vertical_integral_of_divergence_of_cloud_frozen_water_flux', 'vertical_integral_of_divergence_of_cloud_liquid_water_flux', 'vertical_integral_of_divergence_of_geopotential_flux', 'vertical_integral_of_divergence_of_kinetic_energy_flux', 'vertical_integral_of_divergence_of_mass_flux', 'vertical_integral_of_divergence_of_moisture_flux', 'vertical_integral_of_divergence_of_ozone_flux', 'vertical_integral_of_divergence_of_thermal_energy_flux', 'vertical_integral_of_divergence_of_total_energy_flux', 'vertical_integral_of_eastward_cloud_frozen_water_flux', 'vertical_integral_of_eastward_cloud_liquid_water_flux', 'vertical_integral_of_eastward_geopotential_flux', 'vertical_integral_of_eastward_heat_flux', 'vertical_integral_of_eastward_kinetic_energy_flux', 'vertical_integral_of_eastward_mass_flux', 'vertical_integral_of_eastward_ozone_flux', 'vertical_integral_of_eastward_total_energy_flux', 'vertical_integral_of_eastward_water_vapour_flux', 'vertical_integral_of_energy_conversion', 'vertical_integral_of_kinetic_energy', 'vertical_integral_of_mass_of_atmosphere', 'vertical_integral_of_mass_tendency', 'vertical_integral_of_northward_cloud_frozen_water_flux', 'vertical_integral_of_northward_cloud_liquid_water_flux', 'vertical_integral_of_northward_geopotential_flux', 'vertical_integral_of_northward_heat_flux', 'vertical_integral_of_northward_kinetic_energy_flux', 'vertical_integral_of_northward_mass_flux', 'vertical_integral_of_northward_ozone_flux', 'vertical_integral_of_northward_total_energy_flux', 'vertical_integral_of_northward_water_vapour_flux', 'vertical_integral_of_potential_and_internal_energy', 'vertical_integral_of_potential_internal_and_latent_energy', 'vertical_integral_of_temperature', 'vertical_integral_of_thermal_energy', 'vertical_integral_of_total_energy', 'vertically_integrated_moisture_divergence', 'high_vegetation_cover', 'leaf_area_index_high_vegetation', 'leaf_area_index_low_vegetation', 'low_vegetation_cover', 'type_of_high_vegetation', 'type_of_low_vegetation', 'air_density_over_the_oceans', 'coefficient_of_drag_with_waves', 'free_convective_velocity_over_the_oceans', 'maximum_individual_wave_height', 'mean_direction_of_total_swell', 'mean_direction_of_wind_waves', 'mean_period_of_total_swell', 'mean_period_of_wind_waves', 'mean_square_slope_of_waves', 'mean_wave_direction', 'mean_wave_direction_of_first_swell_partition', 'mean_wave_direction_of_second_swell_partition', 'mean_wave_direction_of_third_swell_partition', 'mean_wave_period', 'mean_wave_period_based_on_first_moment', 'mean_wave_period_based_on_first_moment_for_swell', 'mean_wave_period_based_on_first_moment_for_wind_waves', 'mean_wave_period_based_on_second_moment_for_swell', 'mean_wave_period_based_on_second_moment_for_wind_waves', 'mean_wave_period_of_first_swell_partition', 'mean_wave_period_of_second_swell_partition', 'mean_wave_period_of_third_swell_partition', 'mean_zero_crossing_wave_period', 'model_bathymetry', 'normalized_energy_flux_into_ocean', 'normalized_energy_flux_into_waves', 'normalized_stress_into_ocean', 'ocean_surface_stress_equivalent_10m_neutral_wind_direction', 'ocean_surface_stress_equivalent_10m_neutral_wind_speed', 'peak_wave_period', 'period_corresponding_to_maximum_individual_wave_height', 'significant_height_of_combined_wind_waves_and_swell', 'significant_height_of_total_swell', 'significant_height_of_wind_waves', 'significant_wave_height_of_first_swell_partition', 'significant_wave_height_of_second_swell_partition', 'significant_wave_height_of_third_swell_partition', 'wave_spectral_directional_width', 'wave_spectral_directional_width_for_swell', 'wave_spectral_directional_width_for_wind_waves', 'wave_spectral_kurtosis', 'wave_spectral_peakedness', 'wave_spectral_skewness', 'angle_of_sub_gridscale_orography', 'anisotropy_of_sub_gridscale_orography', 'benjamin_feir_index', 'boundary_layer_dissipation', 'boundary_layer_height', 'charnock', 'convective_available_potential_energy', 'convective_inhibition', 'duct_base_height', 'eastward_gravity_wave_surface_stress', 'eastward_turbulent_surface_stress', 'forecast_albedo', 'forecast_surface_roughness', 'friction_velocity', 'geopotential', 'gravity_wave_dissipation', 'instantaneous_eastward_turbulent_surface_stress', 'instantaneous_moisture_flux', 'instantaneous_northward_turbulent_surface_stress', 'k_index', 'land_sea_mask', 'mean_vertical_gradient_of_refractivity_inside_trapping_layer', 'minimum_vertical_gradient_of_refractivity_inside_trapping_layer', 'northward_gravity_wave_surface_stress', 'northward_turbulent_surface_stress', 'sea_ice_cover', 'skin_reservoir_content', 'slope_of_sub_gridscale_orography', 'standard_deviation_of_filtered_subgrid_orography', 'standard_deviation_of_orography', 'total_column_ozone', 'total_column_supercooled_liquid_water', 'total_column_water', 'total_column_water_vapour', 'total_totals_index', 'trapping_layer_base_height', 'trapping_layer_top_height', 'u_component_stokes_drift', 'v_component_stokes_drift', 'zero_degree_level'],
        year = ['1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        daily_statistic = ['daily_mean', 'daily_minimum', 'daily_maximum', 'daily_sum'],
        frequency = ['1_hourly', '3_hourly', '6_hourly'],
        product_type = ['reanalysis', 'ensemble_members', 'ensemble_mean'],
        time_zone = ['utc-12:00', 'utc-11:00', 'utc-10:00', 'utc-09:00', 'utc-08:00', 'utc-07:00', 'utc-06:00', 'utc-05:00', 'utc-04:00', 'utc-03:00', 'utc-02:00', 'utc-01:00', 'utc+00:00', 'utc+01:00', 'utc+02:00', 'utc+03:00', 'utc+04:00', 'utc+05:00', 'utc+06:00', 'utc+07:00', 'utc+08:00', 'utc+09:00', 'utc+10:00', 'utc+11:00', 'utc+12:00', 'utc+13:00', 'utc+14:00'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], year: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global', daily_statistic: str = 'daily_mean', frequency: str = '1_hourly', product_type: str = 'reanalysis', time_zone: str = 'utc+00:00'): 
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
        
        - 10m_u_component_of_wind

        
        - 10m_v_component_of_wind

        
        - 2m_dewpoint_temperature

        
        - 2m_temperature

        
        - mean_sea_level_pressure

        
        - mean_wave_direction

        
        - mean_wave_period

        
        - sea_surface_temperature

        
        - significant_height_of_combined_wind_waves_and_swell

        
        - surface_pressure

        
        - total_precipitation

        
        - 2m_dewpoint_temperature

        
        - 2m_temperature

        
        - ice_temperature_layer_1

        
        - ice_temperature_layer_2

        
        - ice_temperature_layer_3

        
        - ice_temperature_layer_4

        
        - maximum_2m_temperature_since_previous_post_processing

        
        - mean_sea_level_pressure

        
        - minimum_2m_temperature_since_previous_post_processing

        
        - sea_surface_temperature

        
        - skin_temperature

        
        - surface_pressure

        
        - 100m_u_component_of_wind

        
        - 100m_v_component_of_wind

        
        - 10m_u_component_of_neutral_wind

        
        - 10m_u_component_of_wind

        
        - 10m_v_component_of_neutral_wind

        
        - 10m_v_component_of_wind

        
        - 10m_wind_gust_since_previous_post_processing

        
        - instantaneous_10m_wind_gust

        
        - mean_boundary_layer_dissipation

        
        - mean_convective_precipitation_rate

        
        - mean_convective_snowfall_rate

        
        - mean_eastward_gravity_wave_surface_stress

        
        - mean_eastward_turbulent_surface_stress

        
        - mean_evaporation_rate

        
        - mean_gravity_wave_dissipation

        
        - mean_large_scale_precipitation_fraction

        
        - mean_large_scale_precipitation_rate

        
        - mean_large_scale_snowfall_rate

        
        - mean_northward_gravity_wave_surface_stress

        
        - mean_northward_turbulent_surface_stress

        
        - mean_potential_evaporation_rate

        
        - mean_runoff_rate

        
        - mean_snow_evaporation_rate

        
        - mean_snowfall_rate

        
        - mean_snowmelt_rate

        
        - mean_sub_surface_runoff_rate

        
        - mean_surface_direct_short_wave_radiation_flux

        
        - mean_surface_direct_short_wave_radiation_flux_clear_sky

        
        - mean_surface_downward_long_wave_radiation_flux

        
        - mean_surface_downward_long_wave_radiation_flux_clear_sky

        
        - mean_surface_downward_short_wave_radiation_flux

        
        - mean_surface_downward_short_wave_radiation_flux_clear_sky

        
        - mean_surface_downward_uv_radiation_flux

        
        - mean_surface_latent_heat_flux

        
        - mean_surface_net_long_wave_radiation_flux

        
        - mean_surface_net_long_wave_radiation_flux_clear_sky

        
        - mean_surface_net_short_wave_radiation_flux

        
        - mean_surface_net_short_wave_radiation_flux_clear_sky

        
        - mean_surface_runoff_rate

        
        - mean_surface_sensible_heat_flux

        
        - mean_top_downward_short_wave_radiation_flux

        
        - mean_top_net_long_wave_radiation_flux

        
        - mean_top_net_long_wave_radiation_flux_clear_sky

        
        - mean_top_net_short_wave_radiation_flux

        
        - mean_top_net_short_wave_radiation_flux_clear_sky

        
        - mean_total_precipitation_rate

        
        - mean_vertically_integrated_moisture_divergence

        
        - clear_sky_direct_solar_radiation_at_surface

        
        - downward_uv_radiation_at_the_surface

        
        - forecast_logarithm_of_surface_roughness_for_heat

        
        - instantaneous_surface_sensible_heat_flux

        
        - near_ir_albedo_for_diffuse_radiation

        
        - near_ir_albedo_for_direct_radiation

        
        - surface_latent_heat_flux

        
        - surface_net_solar_radiation

        
        - surface_net_solar_radiation_clear_sky

        
        - surface_net_thermal_radiation

        
        - surface_net_thermal_radiation_clear_sky

        
        - surface_sensible_heat_flux

        
        - surface_solar_radiation_downward_clear_sky

        
        - surface_solar_radiation_downwards

        
        - surface_thermal_radiation_downward_clear_sky

        
        - surface_thermal_radiation_downwards

        
        - toa_incident_solar_radiation

        
        - top_net_solar_radiation

        
        - top_net_solar_radiation_clear_sky

        
        - top_net_thermal_radiation

        
        - top_net_thermal_radiation_clear_sky

        
        - total_sky_direct_solar_radiation_at_surface

        
        - uv_visible_albedo_for_diffuse_radiation

        
        - uv_visible_albedo_for_direct_radiation

        
        - cloud_base_height

        
        - high_cloud_cover

        
        - low_cloud_cover

        
        - medium_cloud_cover

        
        - total_cloud_cover

        
        - total_column_cloud_ice_water

        
        - total_column_cloud_liquid_water

        
        - vertical_integral_of_divergence_of_cloud_frozen_water_flux

        
        - vertical_integral_of_divergence_of_cloud_liquid_water_flux

        
        - vertical_integral_of_eastward_cloud_frozen_water_flux

        
        - vertical_integral_of_eastward_cloud_liquid_water_flux

        
        - vertical_integral_of_northward_cloud_frozen_water_flux

        
        - vertical_integral_of_northward_cloud_liquid_water_flux

        
        - lake_bottom_temperature

        
        - lake_cover

        
        - lake_depth

        
        - lake_ice_depth

        
        - lake_ice_temperature

        
        - lake_mix_layer_depth

        
        - lake_mix_layer_temperature

        
        - lake_shape_factor

        
        - lake_total_layer_temperature

        
        - evaporation

        
        - potential_evaporation

        
        - runoff

        
        - sub_surface_runoff

        
        - surface_runoff

        
        - convective_precipitation

        
        - convective_rain_rate

        
        - instantaneous_large_scale_surface_precipitation_fraction

        
        - large_scale_rain_rate

        
        - large_scale_precipitation

        
        - large_scale_precipitation_fraction

        
        - maximum_total_precipitation_rate_since_previous_post_processing

        
        - minimum_total_precipitation_rate_since_previous_post_processing

        
        - precipitation_type

        
        - total_column_rain_water

        
        - total_precipitation

        
        - convective_snowfall

        
        - convective_snowfall_rate_water_equivalent

        
        - large_scale_snowfall_rate_water_equivalent

        
        - large_scale_snowfall

        
        - snow_albedo

        
        - snow_density

        
        - snow_depth

        
        - snow_evaporation

        
        - snowfall

        
        - snowmelt

        
        - temperature_of_snow_layer

        
        - total_column_snow_water

        
        - soil_temperature_level_1

        
        - soil_temperature_level_2

        
        - soil_temperature_level_3

        
        - soil_temperature_level_4

        
        - soil_type

        
        - volumetric_soil_water_layer_1

        
        - volumetric_soil_water_layer_2

        
        - volumetric_soil_water_layer_3

        
        - volumetric_soil_water_layer_4

        
        - vertical_integral_of_divergence_of_cloud_frozen_water_flux

        
        - vertical_integral_of_divergence_of_cloud_liquid_water_flux

        
        - vertical_integral_of_divergence_of_geopotential_flux

        
        - vertical_integral_of_divergence_of_kinetic_energy_flux

        
        - vertical_integral_of_divergence_of_mass_flux

        
        - vertical_integral_of_divergence_of_moisture_flux

        
        - vertical_integral_of_divergence_of_ozone_flux

        
        - vertical_integral_of_divergence_of_thermal_energy_flux

        
        - vertical_integral_of_divergence_of_total_energy_flux

        
        - vertical_integral_of_eastward_cloud_frozen_water_flux

        
        - vertical_integral_of_eastward_cloud_liquid_water_flux

        
        - vertical_integral_of_eastward_geopotential_flux

        
        - vertical_integral_of_eastward_heat_flux

        
        - vertical_integral_of_eastward_kinetic_energy_flux

        
        - vertical_integral_of_eastward_mass_flux

        
        - vertical_integral_of_eastward_ozone_flux

        
        - vertical_integral_of_eastward_total_energy_flux

        
        - vertical_integral_of_eastward_water_vapour_flux

        
        - vertical_integral_of_energy_conversion

        
        - vertical_integral_of_kinetic_energy

        
        - vertical_integral_of_mass_of_atmosphere

        
        - vertical_integral_of_mass_tendency

        
        - vertical_integral_of_northward_cloud_frozen_water_flux

        
        - vertical_integral_of_northward_cloud_liquid_water_flux

        
        - vertical_integral_of_northward_geopotential_flux

        
        - vertical_integral_of_northward_heat_flux

        
        - vertical_integral_of_northward_kinetic_energy_flux

        
        - vertical_integral_of_northward_mass_flux

        
        - vertical_integral_of_northward_ozone_flux

        
        - vertical_integral_of_northward_total_energy_flux

        
        - vertical_integral_of_northward_water_vapour_flux

        
        - vertical_integral_of_potential_and_internal_energy

        
        - vertical_integral_of_potential_internal_and_latent_energy

        
        - vertical_integral_of_temperature

        
        - vertical_integral_of_thermal_energy

        
        - vertical_integral_of_total_energy

        
        - vertically_integrated_moisture_divergence

        
        - high_vegetation_cover

        
        - leaf_area_index_high_vegetation

        
        - leaf_area_index_low_vegetation

        
        - low_vegetation_cover

        
        - type_of_high_vegetation

        
        - type_of_low_vegetation

        
        - air_density_over_the_oceans

        
        - coefficient_of_drag_with_waves

        
        - free_convective_velocity_over_the_oceans

        
        - maximum_individual_wave_height

        
        - mean_direction_of_total_swell

        
        - mean_direction_of_wind_waves

        
        - mean_period_of_total_swell

        
        - mean_period_of_wind_waves

        
        - mean_square_slope_of_waves

        
        - mean_wave_direction

        
        - mean_wave_direction_of_first_swell_partition

        
        - mean_wave_direction_of_second_swell_partition

        
        - mean_wave_direction_of_third_swell_partition

        
        - mean_wave_period

        
        - mean_wave_period_based_on_first_moment

        
        - mean_wave_period_based_on_first_moment_for_swell

        
        - mean_wave_period_based_on_first_moment_for_wind_waves

        
        - mean_wave_period_based_on_second_moment_for_swell

        
        - mean_wave_period_based_on_second_moment_for_wind_waves

        
        - mean_wave_period_of_first_swell_partition

        
        - mean_wave_period_of_second_swell_partition

        
        - mean_wave_period_of_third_swell_partition

        
        - mean_zero_crossing_wave_period

        
        - model_bathymetry

        
        - normalized_energy_flux_into_ocean

        
        - normalized_energy_flux_into_waves

        
        - normalized_stress_into_ocean

        
        - ocean_surface_stress_equivalent_10m_neutral_wind_direction

        
        - ocean_surface_stress_equivalent_10m_neutral_wind_speed

        
        - peak_wave_period

        
        - period_corresponding_to_maximum_individual_wave_height

        
        - significant_height_of_combined_wind_waves_and_swell

        
        - significant_height_of_total_swell

        
        - significant_height_of_wind_waves

        
        - significant_wave_height_of_first_swell_partition

        
        - significant_wave_height_of_second_swell_partition

        
        - significant_wave_height_of_third_swell_partition

        
        - wave_spectral_directional_width

        
        - wave_spectral_directional_width_for_swell

        
        - wave_spectral_directional_width_for_wind_waves

        
        - wave_spectral_kurtosis

        
        - wave_spectral_peakedness

        
        - wave_spectral_skewness

        
        - angle_of_sub_gridscale_orography

        
        - anisotropy_of_sub_gridscale_orography

        
        - benjamin_feir_index

        
        - boundary_layer_dissipation

        
        - boundary_layer_height

        
        - charnock

        
        - convective_available_potential_energy

        
        - convective_inhibition

        
        - duct_base_height

        
        - eastward_gravity_wave_surface_stress

        
        - eastward_turbulent_surface_stress

        
        - forecast_albedo

        
        - forecast_surface_roughness

        
        - friction_velocity

        
        - geopotential

        
        - gravity_wave_dissipation

        
        - instantaneous_eastward_turbulent_surface_stress

        
        - instantaneous_moisture_flux

        
        - instantaneous_northward_turbulent_surface_stress

        
        - k_index

        
        - land_sea_mask

        
        - mean_vertical_gradient_of_refractivity_inside_trapping_layer

        
        - minimum_vertical_gradient_of_refractivity_inside_trapping_layer

        
        - northward_gravity_wave_surface_stress

        
        - northward_turbulent_surface_stress

        
        - sea_ice_cover

        
        - skin_reservoir_content

        
        - slope_of_sub_gridscale_orography

        
        - standard_deviation_of_filtered_subgrid_orography

        
        - standard_deviation_of_orography

        
        - total_column_ozone

        
        - total_column_supercooled_liquid_water

        
        - total_column_water

        
        - total_column_water_vapour

        
        - total_totals_index

        
        - trapping_layer_base_height

        
        - trapping_layer_top_height

        
        - u_component_stokes_drift

        
        - v_component_stokes_drift

        
        - zero_degree_level

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

        ---

        :param area_group:
        :type area_group: str

        ---

        :param daily_statistic:
        :type daily_statistic: str

        **Valid values:**
        
        - daily_mean

        
        - daily_minimum

        
        - daily_maximum

        
        - daily_sum

        ---

        :param frequency:
        :type frequency: str

        **Valid values:**
        
        - 1_hourly

        
        - 3_hourly

        
        - 6_hourly

        ---

        :param product_type:
        :type product_type: str

        **Valid values:**
        
        - reanalysis

        
        - ensemble_members

        
        - ensemble_mean

        ---

        :param time_zone:
        :type time_zone: str

        **Valid values:**
        
        - utc-12:00

        
        - utc-11:00

        
        - utc-10:00

        
        - utc-09:00

        
        - utc-08:00

        
        - utc-07:00

        
        - utc-06:00

        
        - utc-05:00

        
        - utc-04:00

        
        - utc-03:00

        
        - utc-02:00

        
        - utc-01:00

        
        - utc+00:00

        
        - utc+01:00

        
        - utc+02:00

        
        - utc+03:00

        
        - utc+04:00

        
        - utc+05:00

        
        - utc+06:00

        
        - utc+07:00

        
        - utc+08:00

        
        - utc+09:00

        
        - utc+10:00

        
        - utc+11:00

        
        - utc+12:00

        
        - utc+13:00

        
        - utc+14:00

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_derived_era5_single_levels_daily_statistics(day: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], year: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global', daily_statistic: str = 'daily_mean', frequency: str = '1_hourly', product_type: str = 'reanalysis', time_zone: str = 'utc+00:00'):
    return Collection_derived_era5_single_levels_daily_statistics.download(day=day, month=month, variable=variable, year=year, area_group=area_group, daily_statistic=daily_statistic, frequency=frequency, product_type=product_type, time_zone=time_zone)

