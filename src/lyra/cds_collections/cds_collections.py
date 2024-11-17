from lyra.translator import Collection
from lyra.common import OneOrMore
from lyra.common import GeographicExtentType
from lyra.common import GeographicExtentMapType
from lyra.common import LabelType
from lyra.common import FreeEditionType
from lyra.common import UNREACHABLE
from lyra.downloader import download_data
from typing import Union, Optional

"""
This code has been automatically generated
by Lyra. Specifically, the format for
this code can be found in

`lyra.translator.translate`
"""

class Collection_sis_energy_derived_projections(Collection):

    @Collection.wrapper
    def download(cls, energy_product_type: OneOrMore[str], ensemble_member: OneOrMore[str], rcm: str, spatial_aggregation: str, temporal_aggregation: str, gcm: OneOrMore[str], variable: OneOrMore[str], experiment: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, energy_product_type: OneOrMore[str], ensemble_member: OneOrMore[str], rcm: str, spatial_aggregation: str, temporal_aggregation: str, gcm: OneOrMore[str], variable: OneOrMore[str], experiment: OneOrMore[str]):
        energy_product_type_valid_values = ['capacity_factor_ratio', 'energy', 'power']
        assert energy_product_type in energy_product_type_valid_values

        ensemble_member_valid_values = ['r12i1p1', 'r1i1p1', 'r3i1p1']
        assert ensemble_member in ensemble_member_valid_values

        rcm_valid_values = ['aladin63', 'cclm4_8_17', 'hirham5', 'racmo22e', 'regcm4', 'rca4', 'wrf381p']
        assert rcm in rcm_valid_values

        spatial_aggregation_valid_values = ['country_level', 'sub_country_level', 'maritime_country_level', 'maritime_sub_country_level', 'original_grid']
        assert spatial_aggregation in spatial_aggregation_valid_values

        temporal_aggregation_valid_values = ['3_hourly', 'daily', 'monthly', 'seasonal', 'annual']
        assert temporal_aggregation in temporal_aggregation_valid_values

        gcm_valid_values = ['cnrm_cm5', 'ec_earth', 'ipsl_cm5a_mr', 'hadgem2_es', 'mpi_esm_lr', 'noresm1_m']
        assert gcm in gcm_valid_values

        variable_valid_values = ['wind_speed_at_100m', 'wind_speed_at_10m', 'surface_downwelling_shortwave_radiation', '2m_air_temperature', 'total_precipitation', 'electricity_demand', 'hydro_power_generation_reservoirs', 'hydro_power_generation_rivers', 'solar_photovoltaic_power_generation', 'wind_power_generation_offshore', 'wind_power_generation_onshore']
        assert variable in variable_valid_values

        experiment_valid_values = ['rcp_2_6', 'rcp_4_5', 'rcp_8_5']
        assert experiment in experiment_valid_values

        return download_data(energy_product_type=energy_product_type, ensemble_member=ensemble_member, rcm=rcm, spatial_aggregation=spatial_aggregation, temporal_aggregation=temporal_aggregation, gcm=gcm, variable=variable, experiment=experiment)

class Collection_satellite_lake_water_level(Collection):

    @Collection.wrapper
    def download(cls, region: OneOrMore[str], lake: OneOrMore[str], variable: str = 'all'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, region: OneOrMore[str], lake: OneOrMore[str], variable: str = 'all'):
        region_valid_values = ['oceania', 'southern_america', 'northern_africa', 'southern_africa', 'northern_north_america', 'southern_north_america', 'northern_europe', 'southern_europe', 'northern_asia', 'southwestern_asia', 'southeastern_asia']
        assert region in region_valid_values

        lake_valid_values = ['albert', 'bagre', 'bankim', 'bogoria', 'fitri', 'kainji', 'kossou', 'kyoga', 'lagdo', 'langano', 'mangbeto', 'nasser', 'roseires', 'shiroro', 'tana', 'tchad', 'turkana', 'volta', 'ziway', 'bangweulu', 'cahora_bassa', 'chishi', 'edouard', 'george', 'hendrik_verwoerd', 'kabele', 'kabwe', 'kariba', 'kisale', 'kinkony', 'kivu', 'mai_ndombe', 'malawi', 'mweru', 'naivasha', 'rukwa', 'tanganika', 'tumba', 'victoria', 'zimbambo', 'sulunga', 'amadjuak', 'athabasca', 'aylmer', 'baker', 'bienville', 'birch', 'big_trout', 'bluenose', 'caribou', 'cedar', 'claire', 'dubawnt', 'faber', 'gods', 'grande_trois', 'greatslave', 'hottah', 'iliamna', 'kamilukuak', 'kasba', 'manitoba', 'nueltin', 'old_wives', 'swan', 'williston', 'winnipegosis', 'winnipeg', 'atlin', 'churchill', 'teshekpuk', 'black', 'tustumena', 'cormorant', 'cumberland', 'american_falls', 'cayuga', 'cerros_colorados', 'chapala', 'des_bois', 'erie', 'fort_peck', 'hinojo', 'huron', 'michigan', 'mono', 'mullet', 'nezahualcoyoti', 'nicaragua', 'nipissing', 'oahe', 'ontario', 'saint_jean', 'sakakawea', 'san_martin', 'superior', 'tres_marias', 'viedma', 'walker', 'yellowstone', 'okeechobee', 'argentino', 'balbina', 'chocon', 'cienagachilloa', 'cochrane', 'fontana', 'guri', 'lagoa_dos_patos', 'ranco', 'sobradino', 'titicaca', 'todos_los_santos', 'valencia', 'brokopondo', 'cabaliana', 'cardiel', 'biarini', 'coari', 'azhibeksorkoli', 'hovsgol', 'tengiz', 'uvs', 'alakol', 'aydarkul', 'bairab', 'balkhash', 'beas', 'beysehir', 'biylikol', 'bugunskoye', 'caspian', 'chardarya', 'chagbo_co', 'chatyrkol', 'egridir', 'gyeze_caka', 'habbaniyah', 'hamrin', 'hawizeh_marshes', 'heishi_beihu', 'issykkul', 'iznik', 'jayakwadi', 'kairakum', 'kamyshlybas', 'kapchagayskoye', 'kara_bogaz_gol', 'karasor', 'langa_co', 'lumajangdong_co', 'luotuo', 'memar', 'mingacevir', 'mossoul', 'saksak', 'sarykamish', 'sasykkol', 'saysan', 'sevan', 'srisailam', 'tharthar', 'toktogul', 'van', 'achit', 'aqqikol_hu', 'ayakkum', 'bosten', 'cuodarima', 'dagze_co', 'dalai', 'danau_towuti', 'danausingkarak', 'dangqiong', 'dogaicoring_q', 'dorgon', 'dorsoidong_co', 'garkung', 'gyaring_co', 'hala', 'har', 'hoh_xil_hu', 'hongze', 'hulun', 'hyargas', 'kokonor', 'lano', 'lixiodain_co', 'migriggyangzham', 'namco', 'namngum', 'ngangze', 'ngoring_co', 'serbug', 'soungari', 'tangra_yumco', 'telashi', 'telmen', 'tonle_sap', 'ulan_ul', 'ulungur', 'xiangyang', 'yamzho_yumco', 'zhari_namco', 'zhelin', 'ziling', 'zonag', 'chlew_larn', 'bay', 'boontsagaan', 'xuelian_hu', 'barkal', 'orba_co', 'baikal', 'baunt', 'bratskoye', 'chlya', 'chukochye', 'illmen', 'inarinjarvi', 'krasnoyarskoye', 'kubenskoye', 'kulundinskoye', 'kumskoye', 'kuybyshevskoye', 'ladoga', 'novosibirskoye', 'onega', 'peipus', 'pyaozero', 'rybinskoye', 'saratovskoye', 'segozerskoye', 'tchany', 'teletskoye', 'umbozero', 'vanajanselka', 'vanerm', 'vattern', 'zeyskoye', 'bolmen', 'bodensee', 'khanka', 'kremenchutska', 'leman', 'prespa', 'tsimlyanskoye', 'rosarito', 'corangamite', 'pukaki', 'argyle']
        assert lake in lake_valid_values

        variable_valid_values = ['all']
        assert variable in variable_valid_values

        return download_data(region=region, lake=lake, variable=variable)

class Collection_satellite_lake_water_temperature(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], version: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: str = 'all'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], version: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: str = 'all'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        version_valid_values = ['4_0', '4_2', '4_5', '4_5_1', '4_5_2']
        assert version in version_valid_values

        year_valid_values = ['1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['all']
        assert variable in variable_valid_values

        return download_data(day=day, version=version, year=year, month=month, variable=variable)

class Collection_multi_origin_c3s_atlas(Collection):

    @Collection.wrapper
    def download(cls, period: str, origin: str, variable: str, domain: str, experiment: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, period: str, origin: str, variable: str, domain: str, experiment: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        period_valid_values = ['1850-2005', '1850-2014', '1940-2022', '1950-2021', '1950-2022', '1958-2014', '1970-2005', '2006-2100', '2015-2100']
        assert period in period_valid_values

        origin_valid_values = ['cmip5', 'cmip6', 'cordex_core', 'cordex_eur_11', 'e_obs', 'era5', 'era5_land', 'oras5']
        assert origin in origin_valid_values

        variable_valid_values = ['monthly_mean_of_daily_accumulated_evaporation', 'monthly_mean_of_daily_accumulated_precipitation', 'monthly_sea_level_pressure', 'monthly_near_surface_specific_humidity', 'monthly_mean_of_daily_accumulated_runoff', 'monthly_mean_of_daily_accumulated_snowfall_precipitation', 'monthly_mean_of_daily_accumulated_soil_moisture_in_upper_soil_portion', 'monthly_surface_thermal_radiation_downwards', 'monthly_surface_solar_radiation_downwards', 'monthly_fraction_of_cloud_cover', 'annual_cooling_degree_days', 'annual_consecutive_dry_days', 'monthly_count_of_frost_days', 'annual_heating_degree_days', 'monthly_maximum_of_1_day_accumulated_precipitation', 'monthly_maximum_of_5_day_accumulated_precipitation', 'monthly_mean_of_daily_mean_wind_speed', 'monthly_mean_of_sea_ice_area_percentage', 'monthly_standardised_precipitation_index_for_6_months_cumulation_period', 'monthly_mean_of_sea_surface_temperature', 'monthly_mean_of_daily_mean_temperature', 'monthly_mean_of_daily_minimum_temperature', 'monthly_minimum_of_daily_minimum_temperature', 'monthly_mean_of_daily_maximum_temperature', 'monthly_count_of_days_with_maximum_temperature_above_35_c', 'monthly_count_of_days_with_bias_adjusted_maximum_temperature_above_35_c', 'monthly_count_of_days_with_maximum_temperature_above_40_c', 'monthly_count_of_days_with_bias_adjusted_maximum_temperature_above_40_c', 'monthly_maximum_of_daily_maximum_temperature', 'monthly_standardised_precipitation_evapotranspiration_index_for_6_months_cumulation_period']
        assert variable in variable_valid_values

        domain_valid_values = ['europe', 'euro_cordex', 'global', 'global_mosaic']
        assert domain in domain_valid_values

        experiment_valid_values = ['historical', 'rcp_2_6', 'rcp_4_5', 'rcp_8_5', 'ssp1_2_6', 'ssp2_4_5', 'ssp3_7_0', 'ssp5_8_5']
        assert experiment in experiment_valid_values

        return download_data(period=period, origin=origin, variable=variable, domain=domain, experiment=experiment, area_group=area_group)

class Collection_seasonal_postprocessed_single_levels(Collection):

    @Collection.wrapper
    def download(cls, system: str, leadtime_month: OneOrMore[str], originating_centre: str, year: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, system: str, leadtime_month: OneOrMore[str], originating_centre: str, year: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        system_valid_values = ['1', '2', '3', '4', '5', '6', '7', '8', '12', '13', '14', '15', '21', '35', '51', '600', '601', '602', '603']
        assert system in system_valid_values

        leadtime_month_valid_values = ['1', '2', '3', '4', '5', '6']
        assert leadtime_month in leadtime_month_valid_values

        originating_centre_valid_values = ['ecmwf', 'ukmo', 'meteo_france', 'dwd', 'cmcc', 'ncep', 'jma', 'eccc']
        assert originating_centre in originating_centre_valid_values

        year_valid_values = ['2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        product_type_valid_values = ['ensemble_mean', 'monthly_mean']
        assert product_type in product_type_valid_values

        variable_valid_values = ['10m_u_component_of_wind_anomaly', '10m_v_component_of_wind_anomaly', '10m_wind_gust_anomaly', '10m_wind_speed_anomaly', '2m_dewpoint_temperature_anomaly', '2m_temperature_anomaly', 'east_west_surface_stress_anomalous_rate_of_accumulation', 'evaporation_anomalous_rate_of_accumulation', 'maximum_2m_temperature_in_the_last_24_hours_anomaly', 'mean_sea_level_pressure_anomaly', 'mean_sub_surface_runoff_rate_anomaly', 'mean_surface_runoff_rate_anomaly', 'minimum_2m_temperature_in_the_last_24_hours_anomaly', 'north_south_surface_stress_anomalous_rate_of_accumulation', 'runoff_anomalous_rate_of_accumulation', 'sea_surface_temperature_anomaly', 'sea_ice_cover_anomaly', 'snow_density_anomaly', 'snow_depth_anomaly', 'snowfall_anomalous_rate_of_accumulation', 'soil_temperature_anomaly_level_1', 'solar_insolation_anomalous_rate_of_accumulation', 'surface_latent_heat_flux_anomalous_rate_of_accumulation', 'surface_sensible_heat_flux_anomalous_rate_of_accumulation', 'surface_solar_radiation_anomalous_rate_of_accumulation', 'surface_solar_radiation_downwards_anomalous_rate_of_accumulation', 'surface_thermal_radiation_anomalous_rate_of_accumulation', 'surface_thermal_radiation_downwards_anomalous_rate_of_accumulation', 'top_solar_radiation_anomalous_rate_of_accumulation', 'top_thermal_radiation_anomalous_rate_of_accumulation', 'total_cloud_cover_anomaly', 'total_column_ice_water_anomaly', 'total_column_liquid_water_anomaly', 'total_column_water_vapour_anomaly', 'total_precipitation_anomalous_rate_of_accumulation']
        assert variable in variable_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(system=system, leadtime_month=leadtime_month, originating_centre=originating_centre, year=year, month=month, product_type=product_type, variable=variable, data_format=data_format, area_group=area_group)

class Collection_satellite_ice_sheet_mass_balance(Collection):

    @Collection.wrapper
    def download(cls, variable: str = 'all'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, variable: str = 'all'):
        variable_valid_values = ['all']
        assert variable in variable_valid_values

        return download_data(variable=variable)

class Collection_satellite_soil_moisture(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time_aggregation: OneOrMore[str], version: OneOrMore[str], year: OneOrMore[str], type_of_sensor: OneOrMore[str], month: OneOrMore[str], type_of_record: OneOrMore[str], variable: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time_aggregation: OneOrMore[str], version: OneOrMore[str], year: OneOrMore[str], type_of_sensor: OneOrMore[str], month: OneOrMore[str], type_of_record: OneOrMore[str], variable: OneOrMore[str]):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_aggregation_valid_values = ['day_average', '10_day_average', 'month_average']
        assert time_aggregation in time_aggregation_valid_values

        version_valid_values = ['v202212', 'v201706', 'v201812', 'deprecated_v201912', 'v201912_1', 'v202012']
        assert version in version_valid_values

        year_valid_values = ['1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        type_of_sensor_valid_values = ['active', 'passive', 'combined_passive_and_active']
        assert type_of_sensor in type_of_sensor_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        type_of_record_valid_values = ['icdr', 'cdr']
        assert type_of_record in type_of_record_valid_values

        variable_valid_values = ['surface_soil_moisture', 'volumetric_surface_soil_moisture']
        assert variable in variable_valid_values

        return download_data(day=day, time_aggregation=time_aggregation, version=version, year=year, type_of_sensor=type_of_sensor, month=month, type_of_record=type_of_record, variable=variable)

class Collection_insitu_gridded_observations_alpine_precipitation(Collection):

    @Collection.wrapper
    def download(cls, dataset_issue: OneOrMore[str], variable: str = 'precipitation', version: OneOrMore[str] = '1.2'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, dataset_issue: OneOrMore[str], variable: str = 'precipitation', version: OneOrMore[str] = '1.2'):
        dataset_issue_valid_values = ['laprec1871', 'laprec1901']
        assert dataset_issue in dataset_issue_valid_values

        variable_valid_values = ['precipitation']
        assert variable in variable_valid_values

        version_valid_values = ['1_1', '1_2']
        assert version in version_valid_values

        return download_data(dataset_issue=dataset_issue, variable=variable, version=version)

class Collection_reanalysis_cerra_model_levels(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time: OneOrMore[str], data_type: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], model_level: OneOrMore[str], data_format: str = 'grib'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time: OneOrMore[str], data_type: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], model_level: OneOrMore[str], data_format: str = 'grib'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_valid_values = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
        assert time in time_valid_values

        data_type_valid_values = ['ensemble_members', 'reanalysis']
        assert data_type in data_type_valid_values

        year_valid_values = ['1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['specific_humidity', 'temperature', 'u_component_of_wind', 'v_component_of_wind']
        assert variable in variable_valid_values

        model_level_valid_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106']
        assert model_level in model_level_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(day=day, time=time, data_type=data_type, year=year, month=month, variable=variable, model_level=model_level, data_format=data_format)

class Collection_reanalysis_uerra_europe_single_levels(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time: OneOrMore[str], origin: str, year: OneOrMore[str], month: OneOrMore[str], variable: str, data_format: str = 'grib'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time: OneOrMore[str], origin: str, year: OneOrMore[str], month: OneOrMore[str], variable: str, data_format: str = 'grib'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_valid_values = ['00:00', '06:00', '12:00', '18:00']
        assert time in time_valid_values

        origin_valid_values = ['mescan_surfex', 'uerra_harmonie']
        assert origin in origin_valid_values

        year_valid_values = ['1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['10m_wind_direction', '10m_wind_speed', '2m_relative_humidity', '2m_temperature', 'albedo', 'high_cloud_cover', 'land_sea_mask', 'low_cloud_cover', 'mean_sea_level_pressure', 'medium_cloud_cover', 'orography', 'skin_temperature', 'snow_density', 'snow_depth_water_equivalent', 'surface_pressure', 'surface_roughness', 'total_cloud_cover', 'total_column_integrated_water_vapour', 'total_precipitation']
        assert variable in variable_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(day=day, time=time, origin=origin, year=year, month=month, variable=variable, data_format=data_format)

class Collection_insitu_observations_near_surface_temperature_us_climate_reference_network(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time_aggregation: OneOrMore[str], year: OneOrMore[str], format: str, month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time_aggregation: OneOrMore[str], year: OneOrMore[str], format: str, month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_aggregation_valid_values = ['daily', 'hourly', 'monthly', 'sub_hourly']
        assert time_aggregation in time_aggregation_valid_values

        year_valid_values = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
        assert year in year_valid_values

        format_valid_values = ['netcdf', 'csv']
        assert format in format_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['air_temperature', 'daily_maximum_air_temperature', 'daily_minimum_air_temperature', 'relative_humidity', 'daily_maximum_relative_humidity', 'daily_minimum_relative_humidity', 'downward_shortwave_irradiance_at_earth_surface', 'hourly_maximum_downward_shortwave_irradiance_at_earth_surface', 'hourly_minimum_downward_shortwave_irradiance_at_earth_surface', 'hourly_maximum_soil_temperature', 'hourly_minimum_soil_temperature', 'monthly_maximum_soil_temperature', 'monthly_minimum_soil_temperature', 'soil_temperature', 'soil_temperature_100cm_from_earth_surface', 'soil_temperature_10cm_from_earth_surface', 'soil_temperature_20cm_from_earth_surface', 'soil_temperature_50cm_from_earth_surface', 'soil_temperature_5cm_from_earth_surface', 'soil_moisture_100cm_from_earth_surface', 'soil_moisture_10cm_from_earth_surface', 'soil_moisture_20cm_from_earth_surface', 'soil_moisture_50cm_from_earth_surface', 'soil_moisture_5cm_from_earth_surface', 'accumulated_precipitation', 'wind_speed_2_meters_from_earth_surface']
        assert variable in variable_valid_values

        return download_data(day=day, time_aggregation=time_aggregation, year=year, format=format, month=month, variable=variable, area_group=area_group)

class Collection_seasonal_original_pressure_levels(Collection):

    @Collection.wrapper
    def download(cls, system: str, day: OneOrMore[str], originating_centre: str, year: OneOrMore[str], leadtime_hour: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], pressure_level: OneOrMore[str], data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, system: str, day: OneOrMore[str], originating_centre: str, year: OneOrMore[str], leadtime_hour: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], pressure_level: OneOrMore[str], data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        system_valid_values = ['1', '2', '3', '4', '5', '6', '7', '8', '12', '13', '14', '15', '21', '35', '51', '600', '601', '602', '603']
        assert system in system_valid_values

        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        originating_centre_valid_values = ['ecmwf', 'ukmo', 'meteo_france', 'dwd', 'cmcc', 'ncep', 'jma', 'eccc']
        assert originating_centre in originating_centre_valid_values

        year_valid_values = ['1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        leadtime_hour_valid_values = ['12', '24', '36', '48', '60', '72', '84', '96', '108', '120', '132', '144', '156', '168', '180', '192', '204', '216', '228', '240', '252', '264', '276', '288', '300', '312', '324', '336', '348', '360', '372', '384', '396', '408', '420', '432', '444', '456', '468', '480', '492', '504', '516', '528', '540', '552', '564', '576', '588', '600', '612', '624', '636', '648', '660', '672', '684', '696', '708', '720', '732', '744', '756', '768', '780', '792', '804', '816', '828', '840', '852', '864', '876', '888', '900', '912', '924', '936', '948', '960', '972', '984', '996', '1008', '1020', '1032', '1044', '1056', '1068', '1080', '1092', '1104', '1116', '1128', '1140', '1152', '1164', '1176', '1188', '1200', '1212', '1224', '1236', '1248', '1260', '1272', '1284', '1296', '1308', '1320', '1332', '1344', '1356', '1368', '1380', '1392', '1404', '1416', '1428', '1440', '1452', '1464', '1476', '1488', '1500', '1512', '1524', '1536', '1548', '1560', '1572', '1584', '1596', '1608', '1620', '1632', '1644', '1656', '1668', '1680', '1692', '1704', '1716', '1728', '1740', '1752', '1764', '1776', '1788', '1800', '1812', '1824', '1836', '1848', '1860', '1872', '1884', '1896', '1908', '1920', '1932', '1944', '1956', '1968', '1980', '1992', '2004', '2016', '2028', '2040', '2052', '2064', '2076', '2088', '2100', '2112', '2124', '2136', '2148', '2160', '2172', '2184', '2196', '2208', '2220', '2232', '2244', '2256', '2268', '2280', '2292', '2304', '2316', '2328', '2340', '2352', '2364', '2376', '2388', '2400', '2412', '2424', '2436', '2448', '2460', '2472', '2484', '2496', '2508', '2520', '2532', '2544', '2556', '2568', '2580', '2592', '2604', '2616', '2628', '2640', '2652', '2664', '2676', '2688', '2700', '2712', '2724', '2736', '2748', '2760', '2772', '2784', '2796', '2808', '2820', '2832', '2844', '2856', '2868', '2880', '2892', '2904', '2916', '2928', '2940', '2952', '2964', '2976', '2988', '3000', '3012', '3024', '3036', '3048', '3060', '3072', '3084', '3096', '3108', '3120', '3132', '3144', '3156', '3168', '3180', '3192', '3204', '3216', '3228', '3240', '3252', '3264', '3276', '3288', '3300', '3312', '3324', '3336', '3348', '3360', '3372', '3384', '3396', '3408', '3420', '3432', '3444', '3456', '3468', '3480', '3492', '3504', '3516', '3528', '3540', '3552', '3564', '3576', '3588', '3600', '3612', '3624', '3636', '3648', '3660', '3672', '3684', '3696', '3708', '3720', '3732', '3744', '3756', '3768', '3780', '3792', '3804', '3816', '3828', '3840', '3852', '3864', '3876', '3888', '3900', '3912', '3924', '3936', '3948', '3960', '3972', '3984', '3996', '4008', '4020', '4032', '4044', '4056', '4068', '4080', '4092', '4104', '4116', '4128', '4140', '4152', '4164', '4176', '4188', '4200', '4212', '4224', '4236', '4248', '4260', '4272', '4284', '4296', '4308', '4320', '4332', '4344', '4356', '4368', '4380', '4392', '4404', '4416', '4428', '4440', '4452', '4464', '4476', '4488', '4500', '4512', '4524', '4536', '4548', '4560', '4572', '4584', '4596', '4608', '4620', '4632', '4644', '4656', '4668', '4680', '4692', '4704', '4716', '4728', '4740', '4752', '4764', '4776', '4788', '4800', '4812', '4824', '4836', '4848', '4860', '4872', '4884', '4896', '4908', '4920', '4932', '4944', '4956', '4968', '4980', '4992', '5004', '5016', '5028', '5040', '5052', '5064', '5076', '5088', '5100', '5112', '5124', '5136', '5148', '5160']
        assert leadtime_hour in leadtime_hour_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['geopotential', 'specific_humidity', 'temperature', 'u_component_of_wind', 'v_component_of_wind']
        assert variable in variable_valid_values

        pressure_level_valid_values = ['10', '30', '50', '100', '200', '300', '400', '500', '700', '850', '925', '1000']
        assert pressure_level in pressure_level_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(system=system, day=day, originating_centre=originating_centre, year=year, leadtime_hour=leadtime_hour, month=month, variable=variable, pressure_level=pressure_level, data_format=data_format, area_group=area_group)

class Collection_satellite_albedo(Collection):

    @Collection.wrapper
    def download(cls, product_version: OneOrMore[str], year: OneOrMore[str], sensor: str, nominal_day: OneOrMore[str], month: OneOrMore[str], horizontal_resolution: OneOrMore[str], satellite: OneOrMore[str], variable: OneOrMore[str], area: Optional[str] = None, area_group: Optional[Union[GeographicExtentMapType, LabelType]] = None): UNREACHABLE()
    
    @classmethod
    def __download__(cls, product_version: OneOrMore[str], year: OneOrMore[str], sensor: str, nominal_day: OneOrMore[str], month: OneOrMore[str], horizontal_resolution: OneOrMore[str], satellite: OneOrMore[str], variable: OneOrMore[str], area: Optional[str] = None, area_group: Optional[Union[GeographicExtentMapType, LabelType]] = None):
        product_version_valid_values = ['v0', 'v1', 'v2', 'v3']
        assert product_version in product_version_valid_values

        year_valid_values = ['1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
        assert year in year_valid_values

        sensor_valid_values = ['avhrr', 'vgt', 'olci_and_slstr']
        assert sensor in sensor_valid_values

        nominal_day_valid_values = ['03', '10', '13', '20', '21', '22', '23', '24', '28', '29', '30', '31']
        assert nominal_day in nominal_day_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        horizontal_resolution_valid_values = ['300m', '1km', '4km']
        assert horizontal_resolution in horizontal_resolution_valid_values

        satellite_valid_values = ['proba', 'spot', 'noaa_7', 'noaa_9', 'noaa_11', 'noaa_14', 'noaa_16', 'noaa_17', 'sentinel_3']
        assert satellite in satellite_valid_values

        variable_valid_values = ['albb_bh', 'albb_dh', 'alsp_bh', 'alsp_dh']
        assert variable in variable_valid_values

        return download_data(product_version=product_version, year=year, sensor=sensor, nominal_day=nominal_day, month=month, horizontal_resolution=horizontal_resolution, satellite=satellite, variable=variable, area=area, area_group=area_group)

class Collection_satellite_upper_troposphere_humidity(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], year: OneOrMore[str], sensor_on_satellite: str, month: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global', variable: str = 'all'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], year: OneOrMore[str], sensor_on_satellite: str, month: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global', variable: str = 'all'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        year_valid_values = ['1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
        assert year in year_valid_values

        sensor_on_satellite_valid_values = ['mhs_on_metop_a', 'mhs_on_metop_b', 'mhs_on_metop_c', 'amsu_b_on_noaa_15', 'amsu_b_on_noaa_16', 'amsu_b_on_noaa_17', 'mhs_on_noaa_18', 'mhs_on_noaa_19']
        assert sensor_on_satellite in sensor_on_satellite_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['all']
        assert variable in variable_valid_values

        return download_data(day=day, year=year, sensor_on_satellite=sensor_on_satellite, month=month, area_group=area_group, variable=variable)

class Collection_projections_cordex_domains_single_levels(Collection):

    @Collection.wrapper
    def download(cls, start_year: OneOrMore[str], ensemble_member: str, end_year: OneOrMore[str], rcm_model: str, gcm_model: str, horizontal_resolution: str, temporal_resolution: str, variable: OneOrMore[str], experiment: str, domain: str): UNREACHABLE()
    
    @classmethod
    def __download__(cls, start_year: OneOrMore[str], ensemble_member: str, end_year: OneOrMore[str], rcm_model: str, gcm_model: str, horizontal_resolution: str, temporal_resolution: str, variable: OneOrMore[str], experiment: str, domain: str):
        start_year_valid_values = ['1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057', '2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065', '2066', '2067', '2068', '2069', '2070', '2071', '2072', '2073', '2074', '2075', '2076', '2077', '2078', '2079', '2080', '2081', '2082', '2083', '2084', '2085', '2086', '2087', '2088', '2089', '2090', '2091', '2092', '2093', '2094', '2095', '2096', '2097', '2098', '2099', '2100']
        assert start_year in start_year_valid_values

        ensemble_member_valid_values = ['r1i1p1', 'r2i1p1', 'r3i1p1', 'r6i1p1', 'r12i1p1', 'r0i0p0']
        assert ensemble_member in ensemble_member_valid_values

        end_year_valid_values = ['1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057', '2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065', '2066', '2067', '2068', '2069', '2070', '2071', '2072', '2073', '2074', '2075', '2076', '2077', '2078', '2079', '2080', '2081', '2082', '2083', '2084', '2085', '2086', '2087', '2088', '2089', '2090', '2091', '2092', '2093', '2094', '2095', '2096', '2097', '2098', '2099', '2100', '2101']
        assert end_year in end_year_valid_values

        rcm_model_valid_values = ['awi_hirham5', 'bccr_wrf331', 'boun_regcm4_3', 'cccma_canrcm4', 'clmcom_btu_cclm4_8_17', 'clmcom_clm_cclm4_8_17', 'clmcom_cclm4_8_17_clm3_5', 'clmcom_cclm5_0_2', 'clmcom_eth_cosmo_crclim', 'clmcom_hzg_cclm5_0_15', 'clmcom_kit_cclm5_0_15', 'cmcc_cclm4_8_19', 'cnrm_aladin52', 'cnrm_aladin53', 'cnrm_aladin63', 'csiro_ccam_2008', 'cyi_wrf351', 'dmi_hirham5', 'elu_regcm4_3', 'gerics_remo2009', 'gerics_remo2015', 'guf_cclm4_8_18_germany', 'ictp_regcm4_3', 'ictp_regcm4_4', 'ictp_regcm4_6', 'ictp_regcm4_7', 'iitm_regcm4_4', 'inpe_eta', 'ipsl_wrf381p', 'isu_regcm4', 'knmi_racmo21p', 'knmi_racmo22e', 'knmi_racmo22t', 'lmd_lmdz4nemomed8', 'mgo_rrcm', 'mohc_hadrem3_ga7_05', 'mohc_hadrm3p', 'mpi_csc_remo2009', 'ncar_regcm4', 'ncar_wrf', 'ornl_regcm4_7', 'ouranos_crcm5', 'rmib_ugent_alaro_0', 'ru_core_regcm4_3', 'smhi_rca4', 'smhi_rca4_sn', 'ua_wrf', 'ucan_wrf341i', 'uhoh_wrf361h', 'ulg_mar311', 'ulg_mar36', 'unsw_wrf360j', 'unsw_wrf360k', 'unsw_wrf360l', 'uqam_crcm5', 'uqam_crcm5_sn']
        assert rcm_model in rcm_model_valid_values

        gcm_model_valid_values = ['cccma_canesm2', 'cnrm_cerfacs_cm5', 'csiro_bom_access1_0', 'csiro_bom_access1_3', 'csiro_qccce_csiro_mk3_6_0', 'era_interim', 'ichec_ec_earth', 'ipsl_cm5a_lr', 'ipsl_cm5a_mr', 'miroc_miroc5', 'mohc_hadgem2_es', 'mpi_m_mpi_esm_lr', 'mpi_m_mpi_esm_mr', 'ncar_ccsm4', 'ncc_noresm1_m', 'noaa_gfdl_gfdl_esm2g', 'noaa_gfdl_esm2m']
        assert gcm_model in gcm_model_valid_values

        horizontal_resolution_valid_values = ['0_11_degree_x_0_11_degree', '0_20_degree_x_0_20_degree', '0_22_degree_x_0_22_degree', '0_44_degree_x_0_44_degree', 'interpolated_0_44_degree_x_0_44_degree']
        assert horizontal_resolution in horizontal_resolution_valid_values

        temporal_resolution_valid_values = ['daily_mean', 'monthly_mean', 'seasonal_mean', '3_hours', '6_hours', 'fixed']
        assert temporal_resolution in temporal_resolution_valid_values

        variable_valid_values = ['2m_air_temperature', '2m_relative_humidity', '2m_surface_specific_humidity', '10m_u_component_of_the_wind', '10m_v_component_of_the_wind', '10m_wind_speed', 'maximum_2m_temperature_in_the_last_24_hours', 'minimum_2m_temperature_in_the_last_24_hours', '200hpa_temperature', '200hpa_u_component_of_the_wind', '200hpa_v_component_of_the_wind', '500hpa_geopotential_height', '850hpa_u_component_of_the_wind', '850hpa_v_component_of_the_wind', 'evaporation', 'land_area_fraction', 'mean_sea_level_pressure', 'mean_precipitation_flux', 'orography', 'surface_pressure', 'surface_solar_radiation_downwards', 'surface_thermal_radiation_downward', 'surface_upwelling_shortwave_radiation', 'total_cloud_cover', 'total_run_off_flux']
        assert variable in variable_valid_values

        experiment_valid_values = ['evaluation', 'historical', 'rcp_2_6', 'rcp_4_5', 'rcp_8_5']
        assert experiment in experiment_valid_values

        domain_valid_values = ['africa', 'antarctic', 'arctic', 'australasia', 'central_america', 'central_asia', 'east_asia', 'europe', 'mediterranean', 'middle_east_and_north_africa', 'north_america', 'south_america', 'south_east_asia', 'south_asia']
        assert domain in domain_valid_values

        return download_data(start_year=start_year, ensemble_member=ensemble_member, end_year=end_year, rcm_model=rcm_model, gcm_model=gcm_model, horizontal_resolution=horizontal_resolution, temporal_resolution=temporal_resolution, variable=variable, experiment=experiment, domain=domain)

class Collection_sis_health_vector(Collection):

    @Collection.wrapper
    def download(cls, ensemble_statistic: OneOrMore[str], variable: OneOrMore[str], experiment: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, ensemble_statistic: OneOrMore[str], variable: OneOrMore[str], experiment: OneOrMore[str]):
        ensemble_statistic_valid_values = ['ensemble_members_average', 'ensemble_members_standard_deviation']
        assert ensemble_statistic in ensemble_statistic_valid_values

        variable_valid_values = ['suitability', 'season_length']
        assert variable in variable_valid_values

        experiment_valid_values = ['rcp4_5', 'rcp8_5']
        assert experiment in experiment_valid_values

        return download_data(ensemble_statistic=ensemble_statistic, variable=variable, experiment=experiment)

class Collection_reanalysis_cerra_pressure_levels(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time: OneOrMore[str], data_type: OneOrMore[str], year: OneOrMore[str], leadtime_hour: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], pressure_level: OneOrMore[str], data_format: str = 'grib'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time: OneOrMore[str], data_type: OneOrMore[str], year: OneOrMore[str], leadtime_hour: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], pressure_level: OneOrMore[str], data_format: str = 'grib'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_valid_values = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
        assert time in time_valid_values

        data_type_valid_values = ['ensemble_members', 'reanalysis']
        assert data_type in data_type_valid_values

        year_valid_values = ['1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
        assert year in year_valid_values

        leadtime_hour_valid_values = ['1', '2', '3', '4', '5', '6', '9', '12', '15', '18', '21', '24', '27', '30']
        assert leadtime_hour in leadtime_hour_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        product_type_valid_values = ['analysis', 'forecast']
        assert product_type in product_type_valid_values

        variable_valid_values = ['cloud_cover', 'geopotential', 'relative_humidity', 'specific_cloud_ice_water_content', 'specific_cloud_liquid_water_content', 'specific_rain_water_content', 'specific_snow_water_content', 'temperature', 'turbulent_kinetic_energy', 'u_component_of_wind', 'v_component_of_wind']
        assert variable in variable_valid_values

        pressure_level_valid_values = ['1', '2', '3', '5', '7', '10', '20', '30', '50', '70', '100', '150', '200', '250', '300', '400', '500', '600', '700', '750', '800', '825', '850', '875', '900', '925', '950', '975', '1000']
        assert pressure_level in pressure_level_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(day=day, time=time, data_type=data_type, year=year, leadtime_hour=leadtime_hour, month=month, product_type=product_type, variable=variable, pressure_level=pressure_level, data_format=data_format)

class Collection_sis_marine_properties(Collection):

    @Collection.wrapper
    def download(cls, time_aggregation: str, vertical_resolution: str, origin: str, year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], experiment: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, time_aggregation: str, vertical_resolution: str, origin: str, year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], experiment: OneOrMore[str]):
        time_aggregation_valid_values = ['day', 'month']
        assert time_aggregation in time_aggregation_valid_values

        vertical_resolution_valid_values = ['surface', 'water_column']
        assert vertical_resolution in vertical_resolution_valid_values

        origin_valid_values = ['nemo_ersem', 'polcoms_ersem']
        assert origin in origin_valid_values

        year_valid_values = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057', '2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065', '2066', '2067', '2068', '2069', '2070', '2071', '2072', '2073', '2074', '2075', '2076', '2077', '2078', '2079', '2080', '2081', '2082', '2083', '2084', '2085', '2086', '2087', '2088', '2089', '2090', '2091', '2092', '2093', '2094', '2095', '2096', '2097', '2098', '2099']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['apparent_oxygen_utilisation', 'total_chlorophyll_a', 'euphotic_zone_chlorophyll_a', 'euphotic_zone_depth', 'mole_concentration_of_nitrate_and_nitrite', 'mole_concentration_of_dissolved_oxygen', 'potential_energy_anomaly', 'sea_water_ph', 'phytoplankton_carbon', 'mole_concentration_of_phosphate', 'net_primary_production', 'saturation_state_of_aragonite', 'mole_concentration_of_silicate', 'sea_water_salinity', 'sea_water_potential_temperature', 'organic_carbon_in_the_water_column', 'u_component_of_water_velocity', 'v_component_of_water_velocity', 'zooplankton_carbon', 'secondary_production']
        assert variable in variable_valid_values

        experiment_valid_values = ['rcp4_5', 'rcp8_5']
        assert experiment in experiment_valid_values

        return download_data(time_aggregation=time_aggregation, vertical_resolution=vertical_resolution, origin=origin, year=year, month=month, variable=variable, experiment=experiment)

class Collection_reanalysis_uerra_europe_soil_levels(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time: OneOrMore[str], origin: str, year: OneOrMore[str], month: OneOrMore[str], soil_level: OneOrMore[str], variable: str, data_format: str = 'grib'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time: OneOrMore[str], origin: str, year: OneOrMore[str], month: OneOrMore[str], soil_level: OneOrMore[str], variable: str, data_format: str = 'grib'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_valid_values = ['00:00', '06:00', '12:00', '18:00']
        assert time in time_valid_values

        origin_valid_values = ['mescan_surfex', 'uerra_harmonie']
        assert origin in origin_valid_values

        year_valid_values = ['1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        soil_level_valid_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
        assert soil_level in soil_level_valid_values

        variable_valid_values = ['soil_temperature', 'volumetric_soil_moisture', 'volumetric_transpiration_stress_onset', 'volumetric_wilting_point']
        assert variable in variable_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(day=day, time=time, origin=origin, year=year, month=month, soil_level=soil_level, variable=variable, data_format=data_format)

class Collection_sis_biodiversity_era5_regional(Collection):

    @Collection.wrapper
    def download(cls, region: OneOrMore[str], origin: str, statistic: OneOrMore[str], derived_variable: OneOrMore[str], variable: OneOrMore[str], version: OneOrMore[str] = '1.0'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, region: OneOrMore[str], origin: str, statistic: OneOrMore[str], derived_variable: OneOrMore[str], variable: OneOrMore[str], version: OneOrMore[str] = '1.0'):
        region_valid_values = ['central_africa', 'northern_brazil', 'europe']
        assert region in region_valid_values

        origin_valid_values = ['era5', 'era5_land']
        assert origin in origin_valid_values

        statistic_valid_values = ['mean', 'median', '25th_quartile', '75th_quartile']
        assert statistic in statistic_valid_values

        derived_variable_valid_values = ['annual_maximum', 'annual_maximum_of_daily_mean', 'annual_mean', 'annual_mean_of_daily_maximum', 'annual_mean_of_daily_minimum', 'annual_minimum', 'annual_sum', 'coldest_quarter', 'driest_quarter', 'end_of_season', 'length_of_season', 'maximum_length', 'mean_intensity', 'mean_length_with_minimum_5_days', 'monthly_mean', 'monthly_mean_of_daily_maximum', 'monthly_mean_of_daily_minimum', 'monthly_sum', 'number_of_occurrences', 'start_of_season', 'warmest_quarter', 'wettest_quarter']
        assert derived_variable in derived_variable_valid_values

        variable_valid_values = ['annual_mean_temperature', 'mean_diurnal_range', 'isothermality', 'temperature_seasonality', 'maximum_temperature_of_warmest_month', 'minimum_temperature_of_coldest_month', 'temperature_annual_range', 'mean_temperature_of_wettest_quarter', 'mean_temperature_of_driest_quarter', 'mean_temperature_of_warmest_quarter', 'mean_temperature_of_coldest_quarter', 'annual_precipitation', 'precipitation_of_wettest_month', 'precipitation_of_driest_month', 'precipitation_seasonality', 'precipitation_of_wettest_quarter', 'precipitation_of_driest_quarter', 'precipitation_of_warmest_quarter', 'precipitation_of_coldest_quarter', 'aridity', 'dry_spells', 'dry_days', 'summer_days', 'surface_latent_heat_flux', 'surface_sensible_heat_flux', 'evaporative_fraction', 'frost_days', 'growing_season', 'growing_degree_days', 'growing_degree_days_during_growing_season_length', 'koeppen_geiger_class', 'potential_evaporation', '2m_temperature', 'precipitation', 'water_vapor_pressure', 'cloud_cover', 'volumetric_soil_water', 'wind_speed', 'zonal_wind_speed', 'meridional_wind_speed']
        assert variable in variable_valid_values

        version_valid_values = ['1_0']
        assert version in version_valid_values

        return download_data(region=region, origin=origin, statistic=statistic, derived_variable=derived_variable, variable=variable, version=version)

class Collection_sis_hydrology_variables_derived_seasonal_reforecast(Collection):

    @Collection.wrapper
    def download(cls, version: OneOrMore[str], hydrological_model: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, version: OneOrMore[str], hydrological_model: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str]):
        version_valid_values = ['1']
        assert version in version_valid_values

        hydrological_model_valid_values = ['e_hypecatch_m00', 'lisflood_efas', 'vic_wur']
        assert hydrological_model in hydrological_model_valid_values

        year_valid_values = ['1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['river_discharge', 'reference_river_discharge_lower_tercile', 'reference_river_discharge_upper_tercile', 'brier_skill_score_above_normal_conditions', 'brier_skill_score_below_normal_conditions', 'continuous_ranked_probability_skill_score', 'fair_ranked_probability_skill_score']
        assert variable in variable_valid_values

        return download_data(version=version, hydrological_model=hydrological_model, year=year, month=month, variable=variable)

class Collection_reanalysis_era5_single_levels(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], download_format: str = 'unarchived', data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global', product_type: OneOrMore[str] = 'reanalysis'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], download_format: str = 'unarchived', data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global', product_type: OneOrMore[str] = 'reanalysis'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_valid_values = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
        assert time in time_valid_values

        year_valid_values = ['1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['10m_u_component_of_wind', '10m_v_component_of_wind', '2m_dewpoint_temperature', '2m_temperature', 'mean_sea_level_pressure', 'mean_wave_direction', 'mean_wave_period', 'sea_surface_temperature', 'significant_height_of_combined_wind_waves_and_swell', 'surface_pressure', 'total_precipitation', '2m_dewpoint_temperature', '2m_temperature', 'ice_temperature_layer_1', 'ice_temperature_layer_2', 'ice_temperature_layer_3', 'ice_temperature_layer_4', 'maximum_2m_temperature_since_previous_post_processing', 'mean_sea_level_pressure', 'minimum_2m_temperature_since_previous_post_processing', 'sea_surface_temperature', 'skin_temperature', 'surface_pressure', '100m_u_component_of_wind', '100m_v_component_of_wind', '10m_u_component_of_neutral_wind', '10m_u_component_of_wind', '10m_v_component_of_neutral_wind', '10m_v_component_of_wind', '10m_wind_gust_since_previous_post_processing', 'instantaneous_10m_wind_gust', 'mean_boundary_layer_dissipation', 'mean_convective_precipitation_rate', 'mean_convective_snowfall_rate', 'mean_eastward_gravity_wave_surface_stress', 'mean_eastward_turbulent_surface_stress', 'mean_evaporation_rate', 'mean_gravity_wave_dissipation', 'mean_large_scale_precipitation_fraction', 'mean_large_scale_precipitation_rate', 'mean_large_scale_snowfall_rate', 'mean_northward_gravity_wave_surface_stress', 'mean_northward_turbulent_surface_stress', 'mean_potential_evaporation_rate', 'mean_runoff_rate', 'mean_snow_evaporation_rate', 'mean_snowfall_rate', 'mean_snowmelt_rate', 'mean_sub_surface_runoff_rate', 'mean_surface_direct_short_wave_radiation_flux', 'mean_surface_direct_short_wave_radiation_flux_clear_sky', 'mean_surface_downward_long_wave_radiation_flux', 'mean_surface_downward_long_wave_radiation_flux_clear_sky', 'mean_surface_downward_short_wave_radiation_flux', 'mean_surface_downward_short_wave_radiation_flux_clear_sky', 'mean_surface_downward_uv_radiation_flux', 'mean_surface_latent_heat_flux', 'mean_surface_net_long_wave_radiation_flux', 'mean_surface_net_long_wave_radiation_flux_clear_sky', 'mean_surface_net_short_wave_radiation_flux', 'mean_surface_net_short_wave_radiation_flux_clear_sky', 'mean_surface_runoff_rate', 'mean_surface_sensible_heat_flux', 'mean_top_downward_short_wave_radiation_flux', 'mean_top_net_long_wave_radiation_flux', 'mean_top_net_long_wave_radiation_flux_clear_sky', 'mean_top_net_short_wave_radiation_flux', 'mean_top_net_short_wave_radiation_flux_clear_sky', 'mean_total_precipitation_rate', 'mean_vertically_integrated_moisture_divergence', 'clear_sky_direct_solar_radiation_at_surface', 'downward_uv_radiation_at_the_surface', 'forecast_logarithm_of_surface_roughness_for_heat', 'instantaneous_surface_sensible_heat_flux', 'near_ir_albedo_for_diffuse_radiation', 'near_ir_albedo_for_direct_radiation', 'surface_latent_heat_flux', 'surface_net_solar_radiation', 'surface_net_solar_radiation_clear_sky', 'surface_net_thermal_radiation', 'surface_net_thermal_radiation_clear_sky', 'surface_sensible_heat_flux', 'surface_solar_radiation_downward_clear_sky', 'surface_solar_radiation_downwards', 'surface_thermal_radiation_downward_clear_sky', 'surface_thermal_radiation_downwards', 'toa_incident_solar_radiation', 'top_net_solar_radiation', 'top_net_solar_radiation_clear_sky', 'top_net_thermal_radiation', 'top_net_thermal_radiation_clear_sky', 'total_sky_direct_solar_radiation_at_surface', 'uv_visible_albedo_for_diffuse_radiation', 'uv_visible_albedo_for_direct_radiation', 'cloud_base_height', 'high_cloud_cover', 'low_cloud_cover', 'medium_cloud_cover', 'total_cloud_cover', 'total_column_cloud_ice_water', 'total_column_cloud_liquid_water', 'vertical_integral_of_divergence_of_cloud_frozen_water_flux', 'vertical_integral_of_divergence_of_cloud_liquid_water_flux', 'vertical_integral_of_eastward_cloud_frozen_water_flux', 'vertical_integral_of_eastward_cloud_liquid_water_flux', 'vertical_integral_of_northward_cloud_frozen_water_flux', 'vertical_integral_of_northward_cloud_liquid_water_flux', 'lake_bottom_temperature', 'lake_cover', 'lake_depth', 'lake_ice_depth', 'lake_ice_temperature', 'lake_mix_layer_depth', 'lake_mix_layer_temperature', 'lake_shape_factor', 'lake_total_layer_temperature', 'evaporation', 'potential_evaporation', 'runoff', 'sub_surface_runoff', 'surface_runoff', 'convective_precipitation', 'convective_rain_rate', 'instantaneous_large_scale_surface_precipitation_fraction', 'large_scale_rain_rate', 'large_scale_precipitation', 'large_scale_precipitation_fraction', 'maximum_total_precipitation_rate_since_previous_post_processing', 'minimum_total_precipitation_rate_since_previous_post_processing', 'precipitation_type', 'total_column_rain_water', 'total_precipitation', 'convective_snowfall', 'convective_snowfall_rate_water_equivalent', 'large_scale_snowfall_rate_water_equivalent', 'large_scale_snowfall', 'snow_albedo', 'snow_density', 'snow_depth', 'snow_evaporation', 'snowfall', 'snowmelt', 'temperature_of_snow_layer', 'total_column_snow_water', 'soil_temperature_level_1', 'soil_temperature_level_2', 'soil_temperature_level_3', 'soil_temperature_level_4', 'soil_type', 'volumetric_soil_water_layer_1', 'volumetric_soil_water_layer_2', 'volumetric_soil_water_layer_3', 'volumetric_soil_water_layer_4', 'vertical_integral_of_divergence_of_cloud_frozen_water_flux', 'vertical_integral_of_divergence_of_cloud_liquid_water_flux', 'vertical_integral_of_divergence_of_geopotential_flux', 'vertical_integral_of_divergence_of_kinetic_energy_flux', 'vertical_integral_of_divergence_of_mass_flux', 'vertical_integral_of_divergence_of_moisture_flux', 'vertical_integral_of_divergence_of_ozone_flux', 'vertical_integral_of_divergence_of_thermal_energy_flux', 'vertical_integral_of_divergence_of_total_energy_flux', 'vertical_integral_of_eastward_cloud_frozen_water_flux', 'vertical_integral_of_eastward_cloud_liquid_water_flux', 'vertical_integral_of_eastward_geopotential_flux', 'vertical_integral_of_eastward_heat_flux', 'vertical_integral_of_eastward_kinetic_energy_flux', 'vertical_integral_of_eastward_mass_flux', 'vertical_integral_of_eastward_ozone_flux', 'vertical_integral_of_eastward_total_energy_flux', 'vertical_integral_of_eastward_water_vapour_flux', 'vertical_integral_of_energy_conversion', 'vertical_integral_of_kinetic_energy', 'vertical_integral_of_mass_of_atmosphere', 'vertical_integral_of_mass_tendency', 'vertical_integral_of_northward_cloud_frozen_water_flux', 'vertical_integral_of_northward_cloud_liquid_water_flux', 'vertical_integral_of_northward_geopotential_flux', 'vertical_integral_of_northward_heat_flux', 'vertical_integral_of_northward_kinetic_energy_flux', 'vertical_integral_of_northward_mass_flux', 'vertical_integral_of_northward_ozone_flux', 'vertical_integral_of_northward_total_energy_flux', 'vertical_integral_of_northward_water_vapour_flux', 'vertical_integral_of_potential_and_internal_energy', 'vertical_integral_of_potential_internal_and_latent_energy', 'vertical_integral_of_temperature', 'vertical_integral_of_thermal_energy', 'vertical_integral_of_total_energy', 'vertically_integrated_moisture_divergence', 'high_vegetation_cover', 'leaf_area_index_high_vegetation', 'leaf_area_index_low_vegetation', 'low_vegetation_cover', 'type_of_high_vegetation', 'type_of_low_vegetation', 'air_density_over_the_oceans', 'coefficient_of_drag_with_waves', 'free_convective_velocity_over_the_oceans', 'maximum_individual_wave_height', 'mean_direction_of_total_swell', 'mean_direction_of_wind_waves', 'mean_period_of_total_swell', 'mean_period_of_wind_waves', 'mean_square_slope_of_waves', 'mean_wave_direction', 'mean_wave_direction_of_first_swell_partition', 'mean_wave_direction_of_second_swell_partition', 'mean_wave_direction_of_third_swell_partition', 'mean_wave_period', 'mean_wave_period_based_on_first_moment', 'mean_wave_period_based_on_first_moment_for_swell', 'mean_wave_period_based_on_first_moment_for_wind_waves', 'mean_wave_period_based_on_second_moment_for_swell', 'mean_wave_period_based_on_second_moment_for_wind_waves', 'mean_wave_period_of_first_swell_partition', 'mean_wave_period_of_second_swell_partition', 'mean_wave_period_of_third_swell_partition', 'mean_zero_crossing_wave_period', 'model_bathymetry', 'normalized_energy_flux_into_ocean', 'normalized_energy_flux_into_waves', 'normalized_stress_into_ocean', 'ocean_surface_stress_equivalent_10m_neutral_wind_direction', 'ocean_surface_stress_equivalent_10m_neutral_wind_speed', 'peak_wave_period', 'period_corresponding_to_maximum_individual_wave_height', 'significant_height_of_combined_wind_waves_and_swell', 'significant_height_of_total_swell', 'significant_height_of_wind_waves', 'significant_wave_height_of_first_swell_partition', 'significant_wave_height_of_second_swell_partition', 'significant_wave_height_of_third_swell_partition', 'wave_spectral_directional_width', 'wave_spectral_directional_width_for_swell', 'wave_spectral_directional_width_for_wind_waves', 'wave_spectral_kurtosis', 'wave_spectral_peakedness', 'wave_spectral_skewness', 'angle_of_sub_gridscale_orography', 'anisotropy_of_sub_gridscale_orography', 'benjamin_feir_index', 'boundary_layer_dissipation', 'boundary_layer_height', 'charnock', 'convective_available_potential_energy', 'convective_inhibition', 'duct_base_height', 'eastward_gravity_wave_surface_stress', 'eastward_turbulent_surface_stress', 'forecast_albedo', 'forecast_surface_roughness', 'friction_velocity', 'geopotential', 'gravity_wave_dissipation', 'instantaneous_eastward_turbulent_surface_stress', 'instantaneous_moisture_flux', 'instantaneous_northward_turbulent_surface_stress', 'k_index', 'land_sea_mask', 'mean_vertical_gradient_of_refractivity_inside_trapping_layer', 'minimum_vertical_gradient_of_refractivity_inside_trapping_layer', 'northward_gravity_wave_surface_stress', 'northward_turbulent_surface_stress', 'sea_ice_cover', 'skin_reservoir_content', 'slope_of_sub_gridscale_orography', 'standard_deviation_of_filtered_subgrid_orography', 'standard_deviation_of_orography', 'total_column_ozone', 'total_column_supercooled_liquid_water', 'total_column_water', 'total_column_water_vapour', 'total_totals_index', 'trapping_layer_base_height', 'trapping_layer_top_height', 'u_component_stokes_drift', 'v_component_stokes_drift', 'zero_degree_level']
        assert variable in variable_valid_values

        download_format_valid_values = ['unarchived', 'zip']
        assert download_format in download_format_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        product_type_valid_values = ['reanalysis', 'ensemble_members', 'ensemble_mean', 'ensemble_spread']
        assert product_type in product_type_valid_values

        return download_data(day=day, time=time, year=year, month=month, variable=variable, download_format=download_format, data_format=data_format, area_group=area_group, product_type=product_type)

class Collection_sis_energy_derived_reanalysis(Collection):

    @Collection.wrapper
    def download(cls, energy_product_type: OneOrMore[str], year: OneOrMore[str], spatial_aggregation: OneOrMore[str], month: OneOrMore[str], temporal_aggregation: OneOrMore[str], variable: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, energy_product_type: OneOrMore[str], year: OneOrMore[str], spatial_aggregation: OneOrMore[str], month: OneOrMore[str], temporal_aggregation: OneOrMore[str], variable: OneOrMore[str]):
        energy_product_type_valid_values = ['capacity_factor_ratio', 'energy', 'power']
        assert energy_product_type in energy_product_type_valid_values

        year_valid_values = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        spatial_aggregation_valid_values = ['original_grid', 'country_level', 'sub_country_level', 'maritime_country_level', 'maritime_sub_country_level']
        assert spatial_aggregation in spatial_aggregation_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        temporal_aggregation_valid_values = ['hourly', 'daily', 'monthly', 'seasonal', 'annual']
        assert temporal_aggregation in temporal_aggregation_valid_values

        variable_valid_values = ['wind_speed_at_100m', 'wind_speed_at_10m', 'surface_downwelling_shortwave_radiation', 'pressure_at_sea_level', '2m_air_temperature', 'total_precipitation', 'electricity_demand', 'hydro_power_generation_reservoirs', 'hydro_power_generation_rivers', 'solar_photovoltaic_power_generation', 'wind_power_generation_offshore', 'wind_power_generation_onshore']
        assert variable in variable_valid_values

        return download_data(energy_product_type=energy_product_type, year=year, spatial_aggregation=spatial_aggregation, month=month, temporal_aggregation=temporal_aggregation, variable=variable)

class Collection_satellite_sea_level_global(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], version: str = 'vDT2021'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], version: str = 'vDT2021'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        year_valid_values = ['1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['daily', 'monthly_mean']
        assert variable in variable_valid_values

        version_valid_values = ['vdt2018', 'vdt2021']
        assert version in version_valid_values

        return download_data(day=day, year=year, month=month, variable=variable, version=version)

class Collection_satellite_sea_surface_temperature_ensemble_product(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: str = 'all'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: str = 'all'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        year_valid_values = ['1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['all']
        assert variable in variable_valid_values

        return download_data(day=day, year=year, month=month, variable=variable)

class Collection_reanalysis_carra_height_levels(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], leadtime_hour: OneOrMore[str], height_level: OneOrMore[str], month: OneOrMore[str], product_type: str, variable: OneOrMore[str], domain: str, data_format: str = 'grib'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], leadtime_hour: OneOrMore[str], height_level: OneOrMore[str], month: OneOrMore[str], product_type: str, variable: OneOrMore[str], domain: str, data_format: str = 'grib'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_valid_values = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
        assert time in time_valid_values

        year_valid_values = ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        leadtime_hour_valid_values = ['1', '2', '3', '4', '5', '6', '9', '12', '15', '18', '21', '24', '27', '30']
        assert leadtime_hour in leadtime_hour_valid_values

        height_level_valid_values = ['15_m', '30_m', '50_m', '75_m', '100_m', '150_m', '200_m', '250_m', '300_m', '400_m', '500_m']
        assert height_level in height_level_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        product_type_valid_values = ['analysis', 'forecast']
        assert product_type in product_type_valid_values

        variable_valid_values = ['pressure', 'relative_humidity', 'specific_cloud_ice_water_content', 'specific_cloud_liquid_water_content', 'temperature', 'wind_direction', 'wind_speed']
        assert variable in variable_valid_values

        domain_valid_values = ['east_domain', 'west_domain']
        assert domain in domain_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(day=day, time=time, year=year, leadtime_hour=leadtime_hour, height_level=height_level, month=month, product_type=product_type, variable=variable, domain=domain, data_format=data_format)

class Collection_derived_era5_land_daily_statistics(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], year: str, month: str, variable: OneOrMore[str], time_zone: str = 'utc+00:00', area_group: Union[FreeEditionType, GeographicExtentType] = 'global', frequency: str = '1_hourly', daily_statistic: str = 'daily_mean'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], year: str, month: str, variable: OneOrMore[str], time_zone: str = 'utc+00:00', area_group: Union[FreeEditionType, GeographicExtentType] = 'global', frequency: str = '1_hourly', daily_statistic: str = 'daily_mean'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        year_valid_values = ['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['2m_dewpoint_temperature', '2m_temperature', 'skin_temperature', 'soil_temperature_level_1', 'soil_temperature_level_2', 'soil_temperature_level_3', 'soil_temperature_level_4', 'lake_bottom_temperature', 'lake_ice_depth', 'lake_ice_temperature', 'lake_mix_layer_depth', 'lake_mix_layer_temperature', 'lake_shape_factor', 'lake_total_layer_temperature', 'snow_albedo', 'snow_cover', 'snow_density', 'snow_depth', 'snow_depth_water_equivalent', 'temperature_of_snow_layer', 'skin_reservoir_content', 'volumetric_soil_water_layer_1', 'volumetric_soil_water_layer_2', 'volumetric_soil_water_layer_3', 'volumetric_soil_water_layer_4', '10m_u_component_of_wind', '10m_v_component_of_wind', 'surface_pressure', 'leaf_area_index_high_vegetation', 'leaf_area_index_low_vegetation', 'forecast_albedo']
        assert variable in variable_valid_values

        time_zone_valid_values = ['utc-12:00', 'utc-11:00', 'utc-10:00', 'utc-09:00', 'utc-08:00', 'utc-07:00', 'utc-06:00', 'utc-05:00', 'utc-04:00', 'utc-03:00', 'utc-02:00', 'utc-01:00', 'utc+00:00', 'utc+01:00', 'utc+02:00', 'utc+03:00', 'utc+04:00', 'utc+05:00', 'utc+06:00', 'utc+07:00', 'utc+08:00', 'utc+09:00', 'utc+10:00', 'utc+11:00', 'utc+12:00', 'utc+13:00', 'utc+14:00']
        assert time_zone in time_zone_valid_values

        frequency_valid_values = ['1_hourly', '3_hourly', '6_hourly']
        assert frequency in frequency_valid_values

        daily_statistic_valid_values = ['daily_mean', 'daily_minimum', 'daily_maximum']
        assert daily_statistic in daily_statistic_valid_values

        return download_data(day=day, year=year, month=month, variable=variable, time_zone=time_zone, area_group=area_group, frequency=frequency, daily_statistic=daily_statistic)

class Collection_insitu_observations_woudc_ozone_total_column_and_profiles(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], year: OneOrMore[str], format: str, observation_type: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], year: OneOrMore[str], format: str, observation_type: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        year_valid_values = ['1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
        assert year in year_valid_values

        format_valid_values = ['netcdf', 'csv']
        assert format in format_valid_values

        observation_type_valid_values = ['total_column', 'vertical_profile']
        assert observation_type in observation_type_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['air_temperature', 'relative_humidity', 'wind_from_direction', 'wind_speed', 'geopotential_height', 'total_ozone_column', 'column_sulphur_dioxide', 'ozone_partial_pressure']
        assert variable in variable_valid_values

        return download_data(day=day, year=year, format=format, observation_type=observation_type, month=month, variable=variable, area_group=area_group)

class Collection_insitu_glaciers_extent(Collection):

    @Collection.wrapper
    def download(cls, product_type: OneOrMore[str], variable: OneOrMore[str], version: str = '7'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, product_type: OneOrMore[str], variable: OneOrMore[str], version: str = '7'):
        product_type_valid_values = ['gridded', 'vector', 'hypsometry']
        assert product_type in product_type_valid_values

        variable_valid_values = ['glacier_area']
        assert variable in variable_valid_values

        version_valid_values = ['rgi_5_0', 'rgi_6_0', 'rgi_7_0']
        assert version in version_valid_values

        return download_data(product_type=product_type, variable=variable, version=version)

class Collection_projections_cmip5_daily_pressure_levels(Collection):

    @Collection.wrapper
    def download(cls, period: OneOrMore[str], model: str, variable: OneOrMore[str], experiment: str, ensemble_member: str = 'r1i1p1'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, period: OneOrMore[str], model: str, variable: OneOrMore[str], experiment: str, ensemble_member: str = 'r1i1p1'):
        period_valid_values = ['19500101-19591231', '19600101-19691231', '19700101-19791231', '19780101-19821231', '19780401-19781231', '19780901-19781230', '19790101-19791231', '19790101-19811231', '19790101-19831230', '19790101-19831231', '19790101-19841231', '19790101-19881231', '19790101-19931231', '19790101-20081231', '19790101-20091231', '19800101-19801231', '19800101-19891231', '19810101-19811231', '19820101-19821231', '19820101-19841231', '19830101-19831231', '19830101-19871231', '19840101-19841231', '19840101-19881230', '19840101-19881231', '19850101-19851231', '19850101-19871231', '19850101-19891231', '19860101-19861231', '19870101-19871231', '19880101-19881231', '19880101-19901231', '19880101-19921231', '19890101-19891231', '19890101-19931230', '19890101-19931231', '19890101-19981231', '19900101-19901231', '19900101-19941231', '19900101-19991231', '19910101-19911231', '19910101-19931231', '19920101-19921231', '19930101-19931231', '19930101-19971231', '19940101-19941231', '19940101-19961231', '19940101-19981230', '19940101-19981231', '19940101-20081231', '19950101-19951231', '19950101-19991231', '19960101-19961231', '19970101-19971231', '19970101-19991231', '19980101-19981231', '19980101-20021231', '19990101-19991231', '19990101-20031230', '19990101-20031231', '19990101-20051231', '19990101-20081231', '20000101-20001231', '20000101-20021231', '20000101-20051231', '20000101-20091231', '20010101-20011231', '20020101-20021231', '20030101-20031231', '20030101-20051231', '20030101-20071231', '20040101-20041231', '20040101-20081230', '20040101-20081231', '20050101-20051231', '20060101-20061231', '20060101-20081231', '20060101-20101231', '20070101-20071231', '20080101-20081231', '20090101-20091231', '18600101-18641231', '18610101-18651231', '18650101-18691231', '18660101-18701231', '18700101-18741231', '18710101-18751231', '18750101-18791231', '18760101-18801231', '18800101-18841231', '18810101-18851231', '18850101-18891231', '18860101-18901231', '18900101-18941231', '18910101-18951231', '18950101-18991231', '18960101-19001231', '19000101-19041231', '19010101-19051231', '19050101-19091231', '19060101-19101231', '19100101-19141231', '19110101-19151231', '19150101-19191231', '19160101-19201231', '19200101-19241231', '19210101-19251231', '19250101-19291231', '19250101-19741231', '19260101-19301231', '19300101-19341231', '19310101-19351231', '19341201-19591130', '19350101-19391231', '19360101-19401231', '19400101-19441231', '19410101-19451231', '19410101-19501231', '19450101-19491231', '19460101-19501231', '19491201-19541130', '19500101-19501231', '19500101-19521231', '19500101-19541231', '19500101-19591231', '19500101-19651231', '19500101-20051231', '19500102-19541231', '19510101-19511231', '19510101-19551231', '19510101-19601231', '19520101-19521231', '19530101-19531231', '19530101-19551231', '19540101-19541231', '19541201-19591130', '19550101-19551231', '19550101-19591231', '19560101-19561231', '19560101-19581231', '19560101-19601231', '19570101-19571231', '19580101-19581231', '19590101-19591231', '19590101-19611231', '19591201-19641130', '19591201-19841130', '19600101-19601231', '19600101-19641231', '19600101-19691231', '19610101-19611231', '19610101-19651231', '19610101-19701231', '19620101-19621231', '19620101-19641231', '19630101-19631231', '19640101-19641231', '19641201-19691130', '19650101-19651231', '19650101-19671231', '19650101-19691231', '19660101-19661231', '19660101-19701231', '19660101-19811231', '19670101-19671231', '19680101-19681231', '19680101-19701231', '19690101-19691231', '19691201-19741130', '19700101-19701231', '19700101-19741231', '19700101-19791231', '19710101-19711231', '19710101-19731231', '19710101-19751231', '19710101-19801231', '19720101-19721231', '19730101-19731231', '19740101-19741231', '19740101-19761231', '19741201-19791130', '19750101-19751231', '19750101-19791231', '19750101-20121231', '19760101-19761231', '19760101-19801231', '19770101-19771231', '19770101-19791231', '19780101-19781231', '19790101-19791231', '19791201-19841130', '19800101-19801231', '19800101-19821231', '19800101-19841231', '19800101-19891231', '19801201-19851130', '19810101-19811231', '19810101-19851231', '19810101-19901231', '19820101-19821231', '19820101-19971231', '19830101-19831231', '19830101-19851231', '19840101-19841231', '19841201-19891130', '19841201-20051230', '19850101-19851231', '19850101-19891231', '19851201-19901130', '19860101-19861231', '19860101-19881231', '19860101-19901231', '19870101-19871231', '19880101-19881231', '19890101-19891231', '19890101-19911231', '19891201-19941130', '19900101-19901231', '19900101-19941231', '19900101-19991231', '19901201-19951130', '19910101-19911231', '19910101-19951231', '19910101-20001231', '19920101-19921231', '19920101-19941231', '19930101-19931231', '19940101-19941231', '19941201-19991130', '19950101-19951231', '19950101-19971231', '19950101-19991231', '19951201-20001130', '19960101-19961231', '19960101-20001231', '19970101-19971231', '19980101-19981231', '19980101-20001231', '19990101-19991231', '19991201-20041130', '20000101-20001231', '20000101-20041231', '20000101-20051231', '20001201-20051130', '20010101-20011231', '20010101-20031231', '20010101-20051231', '20020101-20021231', '20030101-20031231', '20040101-20041231', '20040101-20061231', '20041201-20051130', '20041201-20051230', '20050101-20051231', '20050101-20091231', '20051201-20101130', '20060101-20061231', '20060101-20081231', '20060101-20091231', '20060101-20101231', '20060101-20151231', '20060101-20251231', '20060101-20301230', '20060101-20301231', '20060101-21001231', '20070101-20071231', '20080101-20081231', '20090101-20091231', '20090101-20111231', '20100101-20101231', '20100101-20141231', '20100101-20191231', '20101201-20111130', '20101201-20151130', '20110101-20111231', '20110101-20151231', '20110101-20201231', '20111201-20161130', '20120101-20121231', '20120101-20141231', '20130101-20131231', '20140101-20141231', '20150101-20151231', '20150101-20171231', '20150101-20191231', '20151201-20201130', '20160101-20161231', '20160101-20201231', '20160101-20251231', '20161201-20211130', '20170101-20171231', '20180101-20181231', '20180101-20201231', '20190101-20191231', '20200101-20201231', '20200101-20241231', '20200101-20291231', '20201201-20251130', '20210101-20211231', '20210101-20231231', '20210101-20251231', '20210101-20301231', '20211201-20261130', '20220101-20221231', '20230101-20231231', '20240101-20241231', '20240101-20261231', '20250101-20251231', '20250101-20291231', '20251201-20301130', '20260101-20261231', '20260101-20301231', '20260101-20351231', '20260101-20451231', '20261201-20311130', '20270101-20271231', '20270101-20291231', '20280101-20281231', '20290101-20291231', '20300101-20301231', '20300101-20321231', '20300101-20341231', '20300101-20391231', '20301201-20351130', '20310101-20311231', '20310101-20351230', '20310101-20351231', '20310101-20401231', '20310101-20551231', '20311201-20361130', '20320101-20321231', '20330101-20331231', '20330101-20351231', '20340101-20341231', '20350101-20351231', '20350101-20391231', '20351201-20401130', '20360101-20361231', '20360101-20381231', '20360101-20401231', '20360101-20451231', '20361201-20411130', '20370101-20371231', '20380101-20381231', '20390101-20391231', '20390101-20411231', '20400101-20401231', '20400101-20441231', '20400101-20491231', '20401201-20451130', '20410101-20411231', '20410101-20451231', '20410101-20501231', '20411201-20461130', '20420101-20421231', '20420101-20441231', '20430101-20431231', '20440101-20441231', '20450101-20451231', '20450101-20471231', '20450101-20491231', '20451201-20501130', '20460101-20461231', '20460101-20501231', '20460101-20551231', '20460101-20651231', '20461201-20511130', '20470101-20471231', '20480101-20481231', '20480101-20501231', '20490101-20491231', '20500101-20501231', '20500101-20541231', '20500101-20591231', '20501201-20551130', '20510101-20511231', '20510101-20531231', '20510101-20551231', '20510101-20601231', '20511201-20561130', '20520101-20521231', '20530101-20531231', '20540101-20541231', '20540101-20561231', '20550101-20551231', '20550101-20591231', '20551201-20601130', '20560101-20561231', '20560101-20601231', '20560101-20651231', '20560101-21001231', '20561201-20611130', '20570101-20571231', '20570101-20591231', '20580101-20581231', '20590101-20591231', '20600101-20601231', '20600101-20621231', '20600101-20641231', '20600101-20691231', '20601201-20651130', '20610101-20611231', '20610101-20651231', '20610101-20701231', '20611201-20661130', '20620101-20621231', '20630101-20631231', '20630101-20651231', '20640101-20641231', '20650101-20651231', '20650101-20691231', '20651201-20701130', '20660101-20661231', '20660101-20681231', '20660101-20701231', '20660101-20751231', '20660101-20851231', '20661201-20711130', '20670101-20671231', '20680101-20681231', '20690101-20691231', '20690101-20711231', '20700101-20701231', '20700101-20741231', '20700101-20791231', '20701201-20751130', '20710101-20711231', '20710101-20751231', '20710101-20801231', '20711201-20761130', '20720101-20721231', '20720101-20741231', '20730101-20731231', '20740101-20741231', '20750101-20751231', '20750101-20771231', '20750101-20791231', '20751201-20801130', '20760101-20761231', '20760101-20801231', '20760101-20851231', '20761201-20811130', '20770101-20771231', '20780101-20781231', '20780101-20801231', '20790101-20791231', '20800101-20801231', '20800101-20841231', '20800101-20891231', '20801201-20851130', '20810101-20811231', '20810101-20831231', '20810101-20851231', '20810101-20901231', '20811201-20861130', '20820101-20821231', '20830101-20831231', '20840101-20841231', '20840101-20861231', '20850101-20851231', '20850101-20891231', '20851201-20901130', '20860101-20861231', '20860101-20901231', '20860101-20951231', '20860101-20991230', '20860101-20991231', '20861201-20911130', '20870101-20871231', '20870101-20891231', '20880101-20881231', '20890101-20891231', '20900101-20901231', '20900101-20921231', '20900101-20941231', '20900101-21001231', '20901201-20951130', '20910101-20911231', '20910101-20951231', '20910101-21001231', '20911201-20961130', '20920101-20921231', '20930101-20931231', '20930101-20951231', '20940101-20941231', '20950101-20951231', '20950101-20991231', '20950101-21001231', '20951201-20991030', '20951201-20991130', '20951201-20991230', '20960101-20961231', '20960101-20981231', '20960101-21001231', '20960101-21051231', '20961201-20991230', '20970101-20971231', '20980101-20981231', '20990101-20991231', '20990101-21001230', '20990101-21001231', '20991101-20991230', '20991201-20991230', '21000101-21000131', '21000101-21001230', '21000101-21001231', '21010101-21101231', '21060101-21151231', '21110101-21201231', '21160101-21251231', '21210101-21301231', '21260101-21351231', '21310101-21401231', '21360101-21451231', '21410101-21501231', '21460101-21551231', '21510101-21601231', '21560101-21651231', '21610101-21701231', '21660101-21751231', '21710101-21801231', '21760101-21851231', '21810101-21811231', '21810101-21901231', '21810101-22001231', '21820101-21821231', '21830101-21831231', '21840101-21841231', '21850101-21851231', '21860101-21861231', '21860101-21951231', '21870101-21871231', '21880101-21881231', '21890101-21891231', '21900101-21901231', '21910101-21911231', '21910101-22001231', '21920101-21921231', '21930101-21931231', '21940101-21941231', '21950101-21951231', '21960101-21961231', '21960101-22051231', '21970101-21971231', '21980101-21981231', '21990101-21991231', '22000101-22001231', '22010101-22101231', '22060101-22151231', '22110101-22201231', '22160101-22251231', '22210101-22301231', '22260101-22351231', '22310101-22401231', '22360101-22451231', '22410101-22501231', '22460101-22551231', '22510101-22601231', '22560101-22651231', '22610101-22701231', '22660101-22751231', '22710101-22801231', '22760101-22851231', '22810101-22901231', '22810101-23001231', '22860101-22951231', '22910101-23001231', '22960101-23001231']
        assert period in period_valid_values

        model_valid_values = ['access1_0', 'access1_3', 'bcc_csm1_1', 'bcc_csm1_1_m', 'bnu_esm', 'ccsm4', 'cmcc_cesm', 'cmcc_cm', 'cmcc_cms', 'cnrm_cm5', 'canam4', 'canesm2', 'ec_earth', 'fgoals_g2', 'fgoals_s2', 'gfdl_cm3', 'gfdl_esm2g', 'gfdl_esm2m', 'gfdl_hiram_c180', 'gfdl_hiram_c360', 'hadcem3', 'hadgem2_a', 'hadgem2_cc', 'hadgem2_es', 'inmcm4', 'ipsl_cm5a_lr', 'ipsl_cm5a_mr', 'ipsl_cm5b_lr', 'mpi_esm_lr', 'mpi_esm_mr', 'mpi_esm_p', 'noresm1_m']
        assert model in model_valid_values

        variable_valid_values = ['geopotential_height', 'temperature', 'u_component_of_wind', 'v_component_of_wind']
        assert variable in variable_valid_values

        experiment_valid_values = ['amip', 'historical', 'rcp_2_6', 'rcp_4_5', 'rcp_6_0', 'rcp_8_5']
        assert experiment in experiment_valid_values

        ensemble_member_valid_values = ['r10i1p1', 'r12i1p1', 'r1i1p1', 'r2i1p1', 'r3i1p1', 'r4i1p1', 'r5i1p1', 'r6i1p1', 'r7i1p1', 'r8i1p1', 'r9i1p1']
        assert ensemble_member in ensemble_member_valid_values

        return download_data(period=period, model=model, variable=variable, experiment=experiment, ensemble_member=ensemble_member)

class Collection_satellite_fire_burned_area(Collection):

    @Collection.wrapper
    def download(cls, region: OneOrMore[str], version: str, origin: str, year: OneOrMore[str], sensor: str, nominal_day: OneOrMore[str], month: OneOrMore[str], variable: str): UNREACHABLE()
    
    @classmethod
    def __download__(cls, region: OneOrMore[str], version: str, origin: str, year: OneOrMore[str], sensor: str, nominal_day: OneOrMore[str], month: OneOrMore[str], variable: str):
        region_valid_values = ['north_america', 'south_america', 'europe', 'asia', 'africa', 'australia']
        assert region in region_valid_values

        version_valid_values = ['5_1_1cds', '1_0', '1_1', '5_0cds', '5_1cds']
        assert version in version_valid_values

        origin_valid_values = ['c3s', 'esa_cci']
        assert origin in origin_valid_values

        year_valid_values = ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
        assert year in year_valid_values

        sensor_valid_values = ['modis', 'olci']
        assert sensor in sensor_valid_values

        nominal_day_valid_values = ['01', '07', '22']
        assert nominal_day in nominal_day_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['grid_variables', 'pixel_variables']
        assert variable in variable_valid_values

        return download_data(region=region, version=version, origin=origin, year=year, sensor=sensor, nominal_day=nominal_day, month=month, variable=variable)

class Collection_reanalysis_uerra_europe_pressure_levels(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: str, pressure_level: OneOrMore[str], data_format: str = 'grib'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: str, pressure_level: OneOrMore[str], data_format: str = 'grib'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_valid_values = ['00:00', '06:00', '12:00', '18:00']
        assert time in time_valid_values

        year_valid_values = ['1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['geopotential', 'geopotential_height', 'relative_humidity', 'temperature', 'u_component_of_wind', 'v_component_of_wind']
        assert variable in variable_valid_values

        pressure_level_valid_values = ['10', '20', '30', '50', '70', '100', '150', '200', '250', '300', '400', '500', '600', '700', '750', '800', '825', '850', '875', '900', '925', '950', '975', '1000']
        assert pressure_level in pressure_level_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(day=day, time=time, year=year, month=month, variable=variable, pressure_level=pressure_level, data_format=data_format)

class Collection_satellite_sea_ice_edge_type(Collection):

    @Collection.wrapper
    def download(cls, region: str, day: OneOrMore[str], cdr_type: str, year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], version: str = '3_0'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, region: str, day: OneOrMore[str], cdr_type: str, year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], version: str = '3_0'):
        region_valid_values = ['northern_hemisphere', 'southern_hemisphere']
        assert region in region_valid_values

        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        cdr_type_valid_values = ['cdr', 'icdr']
        assert cdr_type in cdr_type_valid_values

        year_valid_values = ['1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['sea_ice_edge', 'sea_ice_type']
        assert variable in variable_valid_values

        version_valid_values = ['1_0', '2_0', '3_0']
        assert version in version_valid_values

        return download_data(region=region, day=day, cdr_type=cdr_type, year=year, month=month, variable=variable, version=version)

class Collection_sis_ocean_wave_timeseries(Collection):

    @Collection.wrapper
    def download(cls, year: OneOrMore[str], variable: OneOrMore[str], experiment: str): UNREACHABLE()
    
    @classmethod
    def __download__(cls, year: OneOrMore[str], variable: OneOrMore[str], experiment: str):
        year_valid_values = ['1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057', '2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065', '2066', '2067', '2068', '2069', '2070', '2071', '2072', '2073', '2074', '2075', '2076', '2077', '2078', '2079', '2080', '2081', '2082', '2083', '2084', '2085', '2086', '2087', '2088', '2089', '2090', '2091', '2092', '2093', '2094', '2095', '2096', '2097', '2098', '2099', '2100']
        assert year in year_valid_values

        variable_valid_values = ['Mean wave direction', 'Mean wave period', 'Peak wave period', 'Significant wave height', 'Wave spectral directional width']
        assert variable in variable_valid_values

        experiment_valid_values = ['ERA5 reanalysis', 'Historical', 'RCP4.5', 'RCP8.5']
        assert experiment in experiment_valid_values

        return download_data(year=year, variable=variable, experiment=experiment)

class Collection_satellite_cloud_properties(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time_aggregation: str, origin: str, climate_data_record_type: str, year: OneOrMore[str], product_family: str, sensor_on_satellite: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time_aggregation: str, origin: str, climate_data_record_type: str, year: OneOrMore[str], product_family: str, sensor_on_satellite: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_aggregation_valid_values = ['monthly_mean', 'daily_mean']
        assert time_aggregation in time_aggregation_valid_values

        origin_valid_values = ['c3s', 'eumetsat', 'esa']
        assert origin in origin_valid_values

        climate_data_record_type_valid_values = ['interim_climate_data_record', 'thematic_climate_data_record']
        assert climate_data_record_type in climate_data_record_type_valid_values

        year_valid_values = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
        assert year in year_valid_values

        product_family_valid_values = ['clara_a2', 'clara_a3', 'cci']
        assert product_family in product_family_valid_values

        sensor_on_satellite_valid_values = ['aatsr_on_envisat', 'atsr2_on_ers2', 'slstr_on_sentinel_3a', 'slstr_on_sentinel_3b', 'slstr_on_sentinel_3a_3b']
        assert sensor_on_satellite in sensor_on_satellite_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['cloud_fraction', 'cloud_top_level', 'cloud_physical_properties_of_the_ice_phase', 'cloud_physical_properties_of_the_liquid_phase', 'all_variables']
        assert variable in variable_valid_values

        return download_data(day=day, time_aggregation=time_aggregation, origin=origin, climate_data_record_type=climate_data_record_type, year=year, product_family=product_family, sensor_on_satellite=sensor_on_satellite, month=month, variable=variable, area_group=area_group)

class Collection_seasonal_postprocessed_pressure_levels(Collection):

    @Collection.wrapper
    def download(cls, system: str, leadtime_month: OneOrMore[str], originating_centre: str, year: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], pressure_level: OneOrMore[str], data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, system: str, leadtime_month: OneOrMore[str], originating_centre: str, year: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], pressure_level: OneOrMore[str], data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        system_valid_values = ['1', '2', '3', '4', '5', '6', '7', '8', '12', '13', '14', '15', '21', '35', '51', '600', '601', '602', '603']
        assert system in system_valid_values

        leadtime_month_valid_values = ['1', '2', '3', '4', '5', '6']
        assert leadtime_month in leadtime_month_valid_values

        originating_centre_valid_values = ['ecmwf', 'ukmo', 'meteo_france', 'dwd', 'cmcc', 'ncep', 'jma', 'eccc']
        assert originating_centre in originating_centre_valid_values

        year_valid_values = ['2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        product_type_valid_values = ['ensemble_mean', 'monthly_mean']
        assert product_type in product_type_valid_values

        variable_valid_values = ['geopotential_anomaly', 'specific_humidity_anomaly', 'temperature_anomaly', 'u_component_of_wind_anomaly', 'v_component_of_wind_anomaly']
        assert variable in variable_valid_values

        pressure_level_valid_values = ['10', '30', '50', '100', '200', '300', '400', '500', '700', '850', '925', '1000']
        assert pressure_level in pressure_level_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(system=system, leadtime_month=leadtime_month, originating_centre=originating_centre, year=year, month=month, product_type=product_type, variable=variable, pressure_level=pressure_level, data_format=data_format, area_group=area_group)

class Collection_sis_heat_and_cold_spells(Collection):

    @Collection.wrapper
    def download(cls, ensemble_statistic: OneOrMore[str], definition: str, variable: OneOrMore[str], experiment: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, ensemble_statistic: OneOrMore[str], definition: str, variable: OneOrMore[str], experiment: OneOrMore[str]):
        ensemble_statistic_valid_values = ['ensemble_members_average', 'ensemble_members_standard_deviation']
        assert ensemble_statistic in ensemble_statistic_valid_values

        definition_valid_values = ['climatological_related', 'health_related', 'country_related']
        assert definition in definition_valid_values

        variable_valid_values = ['heat_wave_days', 'cold_spell_days']
        assert variable in variable_valid_values

        experiment_valid_values = ['rcp4_5', 'rcp8_5']
        assert experiment in experiment_valid_values

        return download_data(ensemble_statistic=ensemble_statistic, definition=definition, variable=variable, experiment=experiment)

class Collection_derived_gridded_glacier_mass_change(Collection):

    @Collection.wrapper
    def download(cls, hydrological_year: OneOrMore[str], product_version: str = 'wgms_fog_2023_09', variable: str = 'glacier_mass_change'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, hydrological_year: OneOrMore[str], product_version: str = 'wgms_fog_2023_09', variable: str = 'glacier_mass_change'):
        hydrological_year_valid_values = ['1975_76', '1976_77', '1977_78', '1978_79', '1979_80', '1980_81', '1981_82', '1982_83', '1983_84', '1984_85', '1985_86', '1986_87', '1987_88', '1988_89', '1989_90', '1990_91', '1991_92', '1992_93', '1993_94', '1994_95', '1995_96', '1996_97', '1997_98', '1998_99', '1999_00', '2000_01', '2001_02', '2002_03', '2003_04', '2004_05', '2005_06', '2006_07', '2007_08', '2008_09', '2009_10', '2010_11', '2011_12', '2012_13', '2013_14', '2014_15', '2015_16', '2016_17', '2017_18', '2018_19', '2019_20', '2020_21', '2021_22']
        assert hydrological_year in hydrological_year_valid_values

        product_version_valid_values = ['wgms_fog_2022_09', 'wgms_fog_2023_09']
        assert product_version in product_version_valid_values

        variable_valid_values = ['glacier_mass_change']
        assert variable in variable_valid_values

        return download_data(hydrological_year=hydrological_year, product_version=product_version, variable=variable)

class Collection_reanalysis_cerra_land(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], leadtime_hour: OneOrMore[str], soil_layer: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], level_type: OneOrMore[str], data_format: str = 'grib'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], leadtime_hour: OneOrMore[str], soil_layer: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], level_type: OneOrMore[str], data_format: str = 'grib'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_valid_values = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
        assert time in time_valid_values

        year_valid_values = ['1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
        assert year in year_valid_values

        leadtime_hour_valid_values = ['1', '2', '3']
        assert leadtime_hour in leadtime_hour_valid_values

        soil_layer_valid_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
        assert soil_layer in soil_layer_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        product_type_valid_values = ['analysis', 'forecast']
        assert product_type in product_type_valid_values

        variable_valid_values = ['albedo', 'evaporation', 'fraction_of_snow_cover', 'lake_bottom_temperature', 'lake_depth', 'lake_ice_depth', 'lake_ice_temperature', 'lake_mix_layer_depth', 'lake_mix_layer_temperature', 'lake_shape_factor', 'lake_total_layer_temperature', 'land_sea_mask', 'liquid_volumetric_soil_moisture', 'orography', 'percolation', 'skin_temperature', 'snow_albedo', 'snow_density', 'snow_depth', 'snow_depth_water_equivalent', 'snow_melt', 'soil_heat_flux', 'soil_temperature', 'surface_latent_heat_flux', 'surface_net_solar_radiation', 'surface_net_thermal_radiation', 'surface_roughness', 'surface_runoff', 'surface_sensible_heat_flux', 'surface_solar_radiation_downwards', 'surface_thermal_radiation_downwards', 'temperature_of_snow_layer', 'total_precipitation', 'volumetric_soil_moisture', 'volumetric_transpiration_stress_onset', 'volumetric_wilting_point']
        assert variable in variable_valid_values

        level_type_valid_values = ['surface', 'soil']
        assert level_type in level_type_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(day=day, time=time, year=year, leadtime_hour=leadtime_hour, soil_layer=soil_layer, month=month, product_type=product_type, variable=variable, level_type=level_type, data_format=data_format)

class Collection_satellite_sea_surface_temperature(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], year: OneOrMore[str], sensor_on_satellite: str, month: OneOrMore[str], processinglevel: str, version: str = '2_1', variable: str = 'all'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], year: OneOrMore[str], sensor_on_satellite: str, month: OneOrMore[str], processinglevel: str, version: str = '2_1', variable: str = 'all'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        year_valid_values = ['1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
        assert year in year_valid_values

        sensor_on_satellite_valid_values = ['avhrr_on_noaa_07', 'avhrr_on_noaa_15', 'avhrr_on_metop_a', 'aatsr_on_envisat', 'avhrr_on_noaa_09', 'avhrr_on_noaa_16', 'avhrr_on_metop_b', 'slstr_on_sentinel_3a', 'avhrr_on_noaa_11', 'avhrr_on_noaa_17', 'atsr1_on_ers_1', 'slstr_on_sentinel_3b', 'avhrr_on_noaa_12', 'avhrr_on_noaa_18', 'atsr2_on_ers_2', 'combined_product', 'avhrr_on_noaa_14', 'avhrr_on_noaa_19']
        assert sensor_on_satellite in sensor_on_satellite_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        processinglevel_valid_values = ['level_3c', 'level_4']
        assert processinglevel in processinglevel_valid_values

        version_valid_values = ['2_1', '2_0', '1_1']
        assert version in version_valid_values

        variable_valid_values = ['all']
        assert variable in variable_valid_values

        return download_data(day=day, year=year, sensor_on_satellite=sensor_on_satellite, month=month, processinglevel=processinglevel, version=version, variable=variable)

class Collection_reanalysis_uerra_europe_height_levels(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], height_level: OneOrMore[str], month: OneOrMore[str], variable: str, data_format: str = 'grib'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], height_level: OneOrMore[str], month: OneOrMore[str], variable: str, data_format: str = 'grib'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_valid_values = ['00:00', '06:00', '12:00', '18:00']
        assert time in time_valid_values

        year_valid_values = ['1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
        assert year in year_valid_values

        height_level_valid_values = ['15_m', '30_m', '50_m', '75_m', '100_m', '150_m', '200_m', '250_m', '300_m', '400_m', '500_m']
        assert height_level in height_level_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['pressure', 'relative_humidity', 'temperature', 'wind_direction', 'wind_speed']
        assert variable in variable_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(day=day, time=time, year=year, height_level=height_level, month=month, variable=variable, data_format=data_format)

class Collection_reanalysis_era5_land(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time: OneOrMore[str], year: str, month: str, variable: OneOrMore[str], download_format: str = 'unarchived', data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time: OneOrMore[str], year: str, month: str, variable: OneOrMore[str], download_format: str = 'unarchived', data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_valid_values = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
        assert time in time_valid_values

        year_valid_values = ['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['2m_dewpoint_temperature', '2m_temperature', 'skin_temperature', 'soil_temperature_level_1', 'soil_temperature_level_2', 'soil_temperature_level_3', 'soil_temperature_level_4', 'lake_bottom_temperature', 'lake_ice_depth', 'lake_ice_temperature', 'lake_mix_layer_depth', 'lake_mix_layer_temperature', 'lake_shape_factor', 'lake_total_layer_temperature', 'snow_albedo', 'snow_cover', 'snow_density', 'snow_depth', 'snow_depth_water_equivalent', 'snowfall', 'snowmelt', 'temperature_of_snow_layer', 'skin_reservoir_content', 'volumetric_soil_water_layer_1', 'volumetric_soil_water_layer_2', 'volumetric_soil_water_layer_3', 'volumetric_soil_water_layer_4', 'forecast_albedo', 'surface_latent_heat_flux', 'surface_net_solar_radiation', 'surface_net_thermal_radiation', 'surface_sensible_heat_flux', 'surface_solar_radiation_downwards', 'surface_thermal_radiation_downwards', 'evaporation_from_bare_soil', 'evaporation_from_open_water_surfaces_excluding_oceans', 'evaporation_from_the_top_of_canopy', 'evaporation_from_vegetation_transpiration', 'potential_evaporation', 'runoff', 'snow_evaporation', 'sub_surface_runoff', 'surface_runoff', 'total_evaporation', '10m_u_component_of_wind', '10m_v_component_of_wind', 'surface_pressure', 'total_precipitation', 'leaf_area_index_high_vegetation', 'leaf_area_index_low_vegetation']
        assert variable in variable_valid_values

        download_format_valid_values = ['unarchived', 'zip']
        assert download_format in download_format_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(day=day, time=time, year=year, month=month, variable=variable, download_format=download_format, data_format=data_format, area_group=area_group)

class Collection_reanalysis_carra_single_levels(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], leadtime_hour: OneOrMore[str], month: OneOrMore[str], product_type: str, soil_level: OneOrMore[str], variable: OneOrMore[str], level_type: str, domain: str, data_format: str = 'grib'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], leadtime_hour: OneOrMore[str], month: OneOrMore[str], product_type: str, soil_level: OneOrMore[str], variable: OneOrMore[str], level_type: str, domain: str, data_format: str = 'grib'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_valid_values = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
        assert time in time_valid_values

        year_valid_values = ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        leadtime_hour_valid_values = ['1', '2', '3', '4', '5', '6', '9', '12', '15', '18', '21', '24', '27', '30']
        assert leadtime_hour in leadtime_hour_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        product_type_valid_values = ['analysis', 'forecast']
        assert product_type in product_type_valid_values

        soil_level_valid_values = ['soil_surface', 'root_depth']
        assert soil_level in soil_level_valid_values

        variable_valid_values = ['10m_eastward_wind_gust_since_previous_post_processing', '10m_northward_wind_gust_since_previous_post_processing', '10m_u_component_of_wind', '10m_v_component_of_wind', '10m_wind_direction', '10m_wind_gust_since_previous_post_processing', '10m_wind_speed', '2m_relative_humidity', '2m_specific_humidity', '2m_temperature', 'albedo', 'cloud_base', 'cloud_top', 'direct_solar_radiation', 'evaporation', 'fog', 'fraction_of_snow_cover', 'high_cloud_cover', 'land_sea_mask', 'low_cloud_cover', 'maximum_2m_temperature_since_previous_post_processing', 'mean_sea_level_pressure', 'medium_cloud_cover', 'minimum_2m_temperature_since_previous_post_processing', 'orography', 'percolation', 'precipitation_type', 'sea_ice_area_fraction', 'sea_ice_surface_temperature', 'sea_ice_thickness', 'sea_surface_temperature', 'skin_temperature', 'snow_albedo', 'snow_density', 'snow_depth_water_equivalent', 'snow_on_ice_total_depth', 'surface_latent_heat_flux', 'surface_net_solar_radiation', 'surface_net_solar_radiation,_clear_sky', 'surface_net_thermal_radiation', 'surface_net_thermal_radiation,_clear_sky', 'surface_pressure', 'surface_roughness', 'surface_roughness_length_for_heat', 'surface_runoff', 'surface_sensible_heat_flux', 'surface_solar_radiation_downwards', 'thermal_surface_radiation_downwards', 'time_integral_of_rain_flux', 'time_integral_of_snow_evaporation_flux', 'time_integral_of_surface_eastward_momentum_flux', 'time_integral_of_surface_latent_heat_evaporation_flux', 'time_integral_of_surface_latent_heat_sublimation_flux', 'time_integral_of_surface_northward_momentum_flux', 'time_integral_of_total_solid_precipitation_flux', 'time_integrated_surface_direct_short_wave_radiation_flux', 'top_net_solar_radiation', 'top_net_thermal_radiation', 'total_cloud_cover', 'total_column_cloud_ice_water', 'total_column_cloud_liquid_water', 'total_column_graupel', 'total_column_integrated_water_vapour', 'total_precipitation', 'visibility', 'volumetric_soil_ice', 'volumetric_soil_moisture']
        assert variable in variable_valid_values

        level_type_valid_values = ['surface_or_atmosphere', 'soil_level']
        assert level_type in level_type_valid_values

        domain_valid_values = ['east_domain', 'west_domain']
        assert domain in domain_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(day=day, time=time, year=year, leadtime_hour=leadtime_hour, month=month, product_type=product_type, soil_level=soil_level, variable=variable, level_type=level_type, domain=domain, data_format=data_format)

class Collection_sis_biodiversity_cmip5_regional(Collection):

    @Collection.wrapper
    def download(cls, region: OneOrMore[str], statistic: OneOrMore[str], model: OneOrMore[str], ensemble_member: OneOrMore[str], derived_variable: OneOrMore[str], variable: OneOrMore[str], experiment: OneOrMore[str], version: OneOrMore[str] = '1.0'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, region: OneOrMore[str], statistic: OneOrMore[str], model: OneOrMore[str], ensemble_member: OneOrMore[str], derived_variable: OneOrMore[str], variable: OneOrMore[str], experiment: OneOrMore[str], version: OneOrMore[str] = '1.0'):
        region_valid_values = ['central_africa', 'northern_brazil', 'europe']
        assert region in region_valid_values

        statistic_valid_values = ['mean', 'median', '25th_quartile', '75th_quartile']
        assert statistic in statistic_valid_values

        model_valid_values = ['access1_0', 'bcc_csm1_1_m', 'csiro_mk3_6_0', 'gfdl_esm2m', 'hadgem2_cc', 'hadgem2_es', 'ipsl_cm5a_lr', 'ipsl_cm5a_mr', 'ipsl_cm5b_lr', 'noresm1_m']
        assert model in model_valid_values

        ensemble_member_valid_values = ['r1i1p1', 'r2i1p1']
        assert ensemble_member in ensemble_member_valid_values

        derived_variable_valid_values = ['annual_maximum', 'annual_maximum_of_daily_mean', 'annual_mean', 'annual_mean_of_daily_maximum', 'annual_mean_of_daily_minimum', 'annual_minimum', 'annual_sum', 'coldest_quarter', 'driest_quarter', 'end_of_season', 'length_of_season', 'maximum_length', 'mean_intensity', 'mean_length_with_minimum_5_days', 'monthly_mean', 'monthly_mean_of_daily_maximum', 'monthly_mean_of_daily_minimum', 'monthly_sum', 'number_of_occurrences', 'start_of_season', 'warmest_quarter', 'wettest_quarter']
        assert derived_variable in derived_variable_valid_values

        variable_valid_values = ['annual_mean_temperature', 'mean_diurnal_range', 'isothermality', 'temperature_seasonality', 'maximum_temperature_of_warmest_month', 'minimum_temperature_of_coldest_month', 'temperature_annual_range', 'mean_temperature_of_wettest_quarter', 'mean_temperature_of_driest_quarter', 'mean_temperature_of_warmest_quarter', 'mean_temperature_of_coldest_quarter', 'annual_precipitation', 'precipitation_of_wettest_month', 'precipitation_of_driest_month', 'precipitation_seasonality', 'precipitation_of_wettest_quarter', 'precipitation_of_driest_quarter', 'precipitation_of_warmest_quarter', 'precipitation_of_coldest_quarter', 'aridity', 'dry_spells', 'dry_days', 'summer_days', 'surface_latent_heat_flux', 'surface_sensible_heat_flux', 'evaporative_fraction', 'frost_days', 'growing_season', 'growing_degree_days', 'growing_degree_days_during_growing_season_length', 'koeppen_geiger_class', 'potential_evaporation', '2m_temperature', 'precipitation', 'water_vapor_pressure', 'cloud_cover', 'volumetric_soil_water', 'wind_speed']
        assert variable in variable_valid_values

        experiment_valid_values = ['rcp4_5', 'rcp8_5']
        assert experiment in experiment_valid_values

        version_valid_values = ['1_0']
        assert version in version_valid_values

        return download_data(region=region, statistic=statistic, model=model, ensemble_member=ensemble_member, derived_variable=derived_variable, variable=variable, experiment=experiment, version=version)

class Collection_insitu_gridded_observations_global_and_regional(Collection):

    @Collection.wrapper
    def download(cls, region: str, time_aggregation: str, version: OneOrMore[str], origin: str, statistic: OneOrMore[str], year: OneOrMore[str], horizontal_aggregation: OneOrMore[str], variable: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, region: str, time_aggregation: str, version: OneOrMore[str], origin: str, statistic: OneOrMore[str], year: OneOrMore[str], horizontal_aggregation: OneOrMore[str], variable: OneOrMore[str]):
        region_valid_values = ['africa', 'conus', 'global', 'quasi_global']
        assert region in region_valid_values

        time_aggregation_valid_values = ['daily', 'monthly']
        assert time_aggregation in time_aggregation_valid_values

        version_valid_values = ['v1_0', 'v2020_0', 'v2020_0_v6_0_fg', 'v2_0', 'v4_0', 'v4_03', 'v6_0']
        assert version in version_valid_values

        origin_valid_values = ['berkearth', 'chirps', 'cmorph', 'cpc', 'cpc_conus', 'cru', 'gistemp', 'gpcc', 'imerg']
        assert origin in origin_valid_values

        statistic_valid_values = ['maximum', 'minimum', 'mean']
        assert statistic in statistic_valid_values

        year_valid_values = ['1750', '1751', '1752', '1753', '1754', '1755', '1756', '1757', '1758', '1759', '1760', '1761', '1762', '1763', '1764', '1765', '1766', '1767', '1768', '1769', '1770', '1771', '1772', '1773', '1774', '1775', '1776', '1777', '1778', '1779', '1780', '1781', '1782', '1783', '1784', '1785', '1786', '1787', '1788', '1789', '1790', '1791', '1792', '1793', '1794', '1795', '1796', '1797', '1798', '1799', '1800', '1801', '1802', '1803', '1804', '1805', '1806', '1807', '1808', '1809', '1810', '1811', '1812', '1813', '1814', '1815', '1816', '1817', '1818', '1819', '1820', '1821', '1822', '1823', '1824', '1825', '1826', '1827', '1828', '1829', '1830', '1831', '1832', '1833', '1834', '1835', '1836', '1837', '1838', '1839', '1840', '1841', '1842', '1843', '1844', '1845', '1846', '1847', '1848', '1849', '1850', '1851', '1852', '1853', '1854', '1855', '1856', '1857', '1858', '1859', '1860', '1861', '1862', '1863', '1864', '1865', '1866', '1867', '1868', '1869', '1870', '1871', '1872', '1873', '1874', '1875', '1876', '1877', '1878', '1879', '1880', '1881', '1882', '1883', '1884', '1885', '1886', '1887', '1888', '1889', '1890', '1891', '1892', '1893', '1894', '1895', '1896', '1897', '1898', '1899', '1900', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909', '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
        assert year in year_valid_values

        horizontal_aggregation_valid_values = ['0_25_x_0_25', '0_2_x_0_2', '0_5_x_0_5', '1_x_1', '2_5_x_2_5', 'horizontal_average']
        assert horizontal_aggregation in horizontal_aggregation_valid_values

        variable_valid_values = ['temperature', 'temperature_anomaly', 'precipitation']
        assert variable in variable_valid_values

        return download_data(region=region, time_aggregation=time_aggregation, version=version, origin=origin, statistic=statistic, year=year, horizontal_aggregation=horizontal_aggregation, variable=variable)

class Collection_projections_cmip5_daily_single_levels(Collection):

    @Collection.wrapper
    def download(cls, period: OneOrMore[str], model: str, variable: OneOrMore[str], experiment: str, ensemble_member: str = 'r1i1p1'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, period: OneOrMore[str], model: str, variable: OneOrMore[str], experiment: str, ensemble_member: str = 'r1i1p1'):
        period_valid_values = ['18800101-19091231', '19100101-19391231', '19400101-19691231', '19500101-19991231', '19700101-19991231', '19700101-20081231', '19780101-20021231', '19780401-19781231', '19780901-19781230', '19780901-20081130', '19790101-19791231', '19790101-19831231', '19790101-19881230', '19790101-19881231', '19790101-19931231', '19790101-19981231', '19790101-20031231', '19790101-20051231', '19790101-20081231', '19790101-20091231', '19790101-20101231', '19800101-19801231', '19810101-19811231', '19820101-19821231', '19830101-19831231', '19840101-19841231', '19840101-19881231', '19850101-19851231', '19860101-19861231', '19870101-19871231', '19880101-19881231', '19890101-19891231', '19890101-19931231', '19890101-19981230', '19890101-19981231', '19900101-19901231', '19910101-19911231', '19920101-19921231', '19930101-19931231', '19940101-19941231', '19940101-19981231', '19940101-20081231', '19950101-19951231', '19960101-19961231', '19970101-19971231', '19980101-19981231', '19990101-19991231', '19990101-20031231', '19990101-20081230', '19990101-20081231', '19990101-20091231', '20000101-20001231', '20000101-20091231', '20000101-20101231', '20010101-20011231', '20020101-20021231', '20030101-20031231', '20030101-20081231', '20040101-20041231', '20040101-20081231', '20050101-20051231', '20060101-20061231', '20060101-20081231', '20070101-20071231', '20080101-20081231', '20090101-20091231', '18500101-18501231', '18500101-18541231', '18500101-18591231', '18500101-18691231', '18500101-18741231', '18500101-18791231', '18500101-18841231', '18500101-18991231', '18500101-19491231', '18500101-20051231', '18500101-20121230', '18510101-18511231', '18520101-18521231', '18530101-18531231', '18540101-18541231', '18550101-18551231', '18550101-18591231', '18560101-18561231', '18570101-18571231', '18580101-18581231', '18590101-18591231', '18591201-18591230', '18591201-18641130', '18591201-18691130', '18591201-18841130', '18600101-18601231', '18600101-18641231', '18600101-18691230', '18600101-18691231', '18610101-18611231', '18610101-18651231', '18620101-18621231', '18630101-18631231', '18640101-18641231', '18641201-18691130', '18650101-18651231', '18650101-18691231', '18660101-18661231', '18660101-18701231', '18670101-18671231', '18680101-18681231', '18690101-18691231', '18691201-18741130', '18691201-18791130', '18700101-18701231', '18700101-18741231', '18700101-18791230', '18700101-18791231', '18700101-18891231', '18710101-18711231', '18710101-18751231', '18720101-18721231', '18730101-18731231', '18740101-18741231', '18741201-18791130', '18750101-18751231', '18750101-18791231', '18750101-18991231', '18760101-18761231', '18760101-18801231', '18770101-18771231', '18780101-18781231', '18790101-18791231', '18791201-18841130', '18791201-18891130', '18800101-18801231', '18800101-18841231', '18800101-18891230', '18800101-18891231', '18800101-19091231', '18810101-18811231', '18810101-18851231', '18820101-18821231', '18830101-18831231', '18840101-18841231', '18841201-18891130', '18841201-19091130', '18850101-18851231', '18850101-18891231', '18850101-19191231', '18860101-18861231', '18860101-18901231', '18870101-18871231', '18880101-18881231', '18890101-18891231', '18891201-18941130', '18891201-18991130', '18900101-18901231', '18900101-18941231', '18900101-18991230', '18900101-18991231', '18900101-19091231', '18910101-18911231', '18910101-18951231', '18920101-18921231', '18930101-18931231', '18940101-18941231', '18941201-18991130', '18950101-18951231', '18950101-18991231', '18960101-18961231', '18960101-19001231', '18970101-18971231', '18980101-18981231', '18990101-18991231', '18991201-19041130', '18991201-19091130', '19000101-19001231', '19000101-19041231', '19000101-19091230', '19000101-19091231', '19000101-19241231', '19000101-19491231', '19010101-19011231', '19010101-19051231', '19020101-19021231', '19030101-19031231', '19040101-19041231', '19041201-19091130', '19050101-19051231', '19050101-19091231', '19060101-19061231', '19060101-19101231', '19070101-19071231', '19080101-19081231', '19090101-19091231', '19091201-19141130', '19091201-19191130', '19091201-19341130', '19100101-19101231', '19100101-19141231', '19100101-19191230', '19100101-19191231', '19100101-19291231', '19100101-19391231', '19110101-19111231', '19110101-19151231', '19120101-19121231', '19130101-19131231', '19140101-19141231', '19141201-19191130', '19150101-19151231', '19150101-19191231', '19160101-19161231', '19160101-19201231', '19170101-19171231', '19180101-19181231', '19190101-19191231', '19191201-19241130', '19191201-19291130', '19200101-19201231', '19200101-19241231', '19200101-19291230', '19200101-19291231', '19200101-19541231', '19210101-19211231', '19210101-19251231', '19220101-19221231', '19230101-19231231', '19240101-19241231', '19241201-19291130', '19250101-19251231', '19250101-19291231', '19250101-19491231', '19260101-19261231', '19260101-19301231', '19270101-19271231', '19280101-19281231', '19290101-19291231', '19291201-19341130', '19291201-19391130', '19300101-19301231', '19300101-19341231', '19300101-19391230', '19300101-19391231', '19300101-19491231', '19310101-19311231', '19310101-19351231', '19320101-19321231', '19330101-19331231', '19340101-19341231', '19341201-19391130', '19341201-19591130', '19350101-19351231', '19350101-19391231', '19360101-19361231', '19360101-19401231', '19370101-19371231', '19380101-19381231', '19390101-19391231', '19391201-19441130', '19391201-19491130', '19400101-19401231', '19400101-19441231', '19400101-19491230', '19400101-19491231', '19410101-19411231', '19410101-19451231', '19420101-19421231', '19430101-19431231', '19440101-19441231', '19441201-19491130', '19450101-19451231', '19450101-19491231', '19460101-19461231', '19460101-19501231', '19470101-19471231', '19480101-19481231', '19490101-19491231', '19491201-19541130', '19491201-19591130', '19500101-19501231', '19500101-19541231', '19500101-19591230', '19500101-19591231', '19500101-19691231', '19500101-19741231', '19500101-19791231', '19500101-19891231', '19500101-19991231', '19500101-20051231', '19500102-19591231', '19500102-19891231', '19510101-19511231', '19510101-19551231', '19520101-19521231', '19530101-19531231', '19540101-19541231', '19541201-19591130', '19550101-19551231', '19550101-19591231', '19550101-19891231', '19560101-19561231', '19560101-19601231', '19570101-19571231', '19580101-19581231', '19590101-19591231', '19591201-19641130', '19591201-19691130', '19591201-19841130', '19600101-19601231', '19600101-19641231', '19600101-19691230', '19600101-19691231', '19610101-19611231', '19610101-19651231', '19610101-20051231', '19620101-19621231', '19630101-19631231', '19640101-19641231', '19641201-19691130', '19650101-19651231', '19650101-19691231', '19660101-19661231', '19660101-19701231', '19670101-19671231', '19680101-19681231', '19690101-19691231', '19691201-19741130', '19691201-19791130', '19700101-19701231', '19700101-19741231', '19700101-19791230', '19700101-19791231', '19700101-19891231', '19710101-19711231', '19710101-19751231', '19720101-19721231', '19730101-19731231', '19740101-19741231', '19741201-19791130', '19750101-19751231', '19750101-19791231', '19750101-19991231', '19750101-20051231', '19750101-20121231', '19760101-19761231', '19760101-19801231', '19770101-19771231', '19780101-19781231', '19790101-19791231', '19790101-20051231', '19791201-19841130', '19791201-19891130', '19800101-19801231', '19800101-19841231', '19800101-19891230', '19800101-19891231', '19800101-20051231', '19810101-19811231', '19810101-19851231', '19820101-19821231', '19830101-19831231', '19840101-19841231', '19841201-19891130', '19841201-20051230', '19850101-19851231', '19850101-19891231', '19860101-19861231', '19860101-19901231', '19870101-19871231', '19880101-19881231', '19890101-19891231', '19891201-19941130', '19891201-19991130', '19900101-19901231', '19900101-19941231', '19900101-19991230', '19900101-19991231', '19900101-20051231', '19910101-19911231', '19910101-19951231', '19920101-19921231', '19930101-19931231', '19940101-19941231', '19941201-19991130', '19950101-19951231', '19950101-19991231', '19960101-19961231', '19960101-20001231', '19970101-19971231', '19980101-19981231', '19990101-19991231', '19991201-20041130', '19991201-20051130', '19991201-20051230', '20000101-20001231', '20000101-20041231', '20000101-20051230', '20000101-20051231', '20000101-20091130', '20000101-20091231', '20000101-20121230', '20000101-20121231', '20010101-20011231', '20010101-20051231', '20020101-20021231', '20030101-20031231', '20040101-20041231', '20041201-20051130', '20041201-20051230', '20050101-20051231', '20060101-20061231', '20070101-20071231', '20080101-20081231', '20090101-20091130', '20050101-20091231', '20051201-20101130', '20051201-20111130', '20051201-20151130', '20060101-20061231', '20060101-20091231', '20060101-20101231', '20060101-20151231', '20060101-20251231', '20060101-20301230', '20060101-20301231', '20060101-20351231', '20060101-20401231', '20060101-20551231', '20060101-20991230', '20060101-20991231', '20060101-21001231', '20060101-22051231', '20070101-20071231', '20080101-20081231', '20090101-20091231', '20100101-20101231', '20100101-20191231', '20101201-20151130', '20110101-20111231', '20110101-20151231', '20111201-20211130', '20120101-20121231', '20130101-20131231', '20140101-20141231', '20150101-20151231', '20151201-20201130', '20151201-20251130', '20160101-20161231', '20160101-20201231', '20160101-20251231', '20170101-20171231', '20180101-20181231', '20190101-20191231', '20200101-20201231', '20200101-20291231', '20201201-20251130', '20210101-20211231', '20210101-20251231', '20211201-20311130', '20220101-20221231', '20230101-20231231', '20240101-20241231', '20250101-20251231', '20251201-20301130', '20251201-20351130', '20260101-20261231', '20260101-20301231', '20260101-20351231', '20260101-20451231', '20260101-20501231', '20270101-20271231', '20280101-20281231', '20290101-20291231', '20300101-20301231', '20300101-20391231', '20301201-20351130', '20310101-20311231', '20310101-20351230', '20310101-20351231', '20310101-20551231', '20310101-20601231', '20311201-20411130', '20320101-20321231', '20330101-20331231', '20340101-20341231', '20350101-20351231', '20351201-20401130', '20351201-20451130', '20360101-20361231', '20360101-20401231', '20360101-20451231', '20370101-20371231', '20380101-20381231', '20390101-20391231', '20400101-20401231', '20400101-20491231', '20401201-20451130', '20410101-20411231', '20410101-20451231', '20410101-20701231', '20410101-20751231', '20411201-20511130', '20420101-20421231', '20430101-20431231', '20440101-20441231', '20450101-20451231', '20451201-20501130', '20451201-20551130', '20460101-20461231', '20460101-20501231', '20460101-20551231', '20460101-20651231', '20470101-20471231', '20480101-20481231', '20490101-20491231', '20500101-20501231', '20500101-20591231', '20501201-20551130', '20510101-20511231', '20510101-20551231', '20510101-20751231', '20511201-20611130', '20520101-20520731', '20520101-20521231', '20530101-20531130', '20530101-20531231', '20540101-20540630', '20540101-20541231', '20550101-20550731', '20550101-20551231', '20551201-20601130', '20551201-20651130', '20560101-20561231', '20560101-20601231', '20560101-20651231', '20560101-20801231', '20560101-21001231', '20570101-20571231', '20580101-20581231', '20590101-20591231', '20600101-20601231', '20600101-20691231', '20601201-20651130', '20610101-20611231', '20610101-20651231', '20610101-20901231', '20611201-20711130', '20620101-20621231', '20630101-20631231', '20640101-20641231', '20650101-20651231', '20651201-20701130', '20651201-20751130', '20660101-20661231', '20660101-20701231', '20660101-20751231', '20660101-20851231', '20670101-20671231', '20680101-20681231', '20690101-20691231', '20700101-20701231', '20700101-20791231', '20701201-20751130', '20710101-20711231', '20710101-20751231', '20710101-21001231', '20711201-20811130', '20720101-20721231', '20730101-20731231', '20740101-20741231', '20750101-20751231', '20751201-20801130', '20751201-20851130', '20760101-20761231', '20760101-20801231', '20760101-20851231', '20760101-21001231', '20770101-20771231', '20780101-20781231', '20790101-20791231', '20800101-20801231', '20800101-20891231', '20801201-20851130', '20810101-20811231', '20810101-20851231', '20810101-20991231', '20810101-21001230', '20810101-21001231', '20811201-20911130', '20820101-20821231', '20830101-20831231', '20840101-20841231', '20850101-20851231', '20851201-20901130', '20851201-20951130', '20860101-20861231', '20860101-20901231', '20860101-20951231', '20860101-21001231', '20870101-20871231', '20880101-20881231', '20890101-20891231', '20900101-20901231', '20900101-20991231', '20900101-21001231', '20901201-20951130', '20910101-20911231', '20910101-20951231', '20910101-21001231', '20911201-20991230', '20920101-20921231', '20930101-20931231', '20940101-20941231', '20950101-20951231', '20951201-20991030', '20951201-20991130', '20951201-20991230', '20951201-21001130', '20951201-21001230', '20960101-20961231', '20960101-21001231', '20970101-20971231', '20980101-20981231', '20990101-20990228', '20990101-20991231', '20991101-20991230', '20991201-20991230', '20991201-21091130', '21000101-21001230', '21000101-21001231', '21000101-21991231', '21001201-21001230', '21010101-21011231', '21010101-21091231', '21010101-21201231', '21010101-21241231', '21010101-21501231', '21010101-23001231', '21020101-21021231', '21030101-21031231', '21040101-21041231', '21050101-21051231', '21060101-21061231', '21070101-21071231', '21080101-21081231', '21090101-21091231', '21091201-21191130', '21100101-21101231', '21100101-21191231', '21110101-21111231', '21120101-21121231', '21130101-21131231', '21140101-21141231', '21150101-21151231', '21160101-21161231', '21170101-21171231', '21180101-21181231', '21190101-21191231', '21191201-21291130', '21200101-21201231', '21200101-21291231', '21210101-21211231', '21210101-21401231', '21220101-21221231', '21230101-21231231', '21240101-21241231', '21250101-21251231', '21250101-21491231', '21260101-21261231', '21270101-21271231', '21280101-21281231', '21290101-21291231', '21291201-21391130', '21300101-21301231', '21300101-21391231', '21310101-21311231', '21320101-21321231', '21330101-21331231', '21340101-21341231', '21350101-21351231', '21360101-21361231', '21370101-21371231', '21380101-21381231', '21390101-21391231', '21391201-21491130', '21400101-21400105', '21400101-21491231', '21410101-21601231', '21491201-21591130', '21500101-21591231', '21500101-21741231', '21510101-22001231', '21591201-21691130', '21600101-21691231', '21610101-21801231', '21691201-21791130', '21700101-21801231', '21750101-21991231', '21791201-21891130', '21810101-21811231', '21810101-21891231', '21810101-22001231', '21820101-21821231', '21830101-21831231', '21840101-21841231', '21850101-21851231', '21860101-21861231', '21870101-21871231', '21880101-21881231', '21890101-21891231', '21891201-21991130', '21900101-21901231', '21900101-22001231', '21910101-21911231', '21920101-21921231', '21930101-21931231', '21940101-21941231', '21950101-21951231', '21960101-21961231', '21970101-21971231', '21980101-21981231', '21990101-21991231', '21991201-22091130', '22000101-22001231', '22000101-22241231', '22000101-23001231', '22010101-22011231', '22010101-22091231', '22010101-22201231', '22010101-22501231', '22020101-22021231', '22030101-22031231', '22060101-23001231', '22091201-22191130', '22100101-22191231', '22191201-22291130', '22200101-22291231', '22210101-22401231', '22250101-22491231', '22291201-22391130', '22300101-22391231', '22391201-22491130', '22400101-22491231', '22410101-22601231', '22491201-22591130', '22500101-22591231', '22500101-22741231', '22510101-23001231', '22591201-22691130', '22600101-22691231', '22610101-22801231', '22691201-22791130', '22700101-22801231', '22750101-22991231', '22750101-23001231', '22791201-22891130', '22810101-22891231', '22810101-23001231', '22891201-22991130', '22900101-23001231', '22991201-22991230']
        assert period in period_valid_values

        model_valid_values = ['access1_0', 'access1_3', 'bcc_csm1_1', 'bcc_csm1_1_m', 'bnu_esm', 'ccsm4', 'cesm1_bgc', 'cesm1_cam5', 'cmcc_cesm', 'cmcc_cm', 'cmcc_cms', 'cnrm_cm5', 'csiro_mk3_6_0', 'canam4', 'cancm4', 'canesm2', 'ec_earth', 'fgoals_g2', 'fgoals_s2', 'gfdl_cm3', 'gfdl_esm2g', 'gfdl_esm2m', 'gfdl_hiram_c180', 'gfdl_hiram_c360', 'giss_e2_h', 'giss_e2_r', 'hadcem3', 'hadgem2_a', 'hadgem2_cc', 'hadgem2_es', 'inmcm4', 'ipsl_cm5a_lr', 'ipsl_cm5a_mr', 'ipsl_cm5b_lr', 'mpi_esm_lr', 'mpi_esm_mr', 'mpi_esm_p', 'noresm1_m']
        assert model in model_valid_values

        variable_valid_values = ['10m_wind_speed', '2m_temperature', 'maximum_2m_temperature_in_the_last_24_hours', 'mean_precipitation_flux', 'mean_sea_level_pressure', 'minimum_2m_temperature_in_the_last_24_hours', 'near_surface_specific_humidity', 'snowfall', 'daily_near_surface_relative_humidity', 'surface_solar_radiation_downwards']
        assert variable in variable_valid_values

        experiment_valid_values = ['amip', 'historical', 'rcp_2_6', 'rcp_4_5', 'rcp_6_0', 'rcp_8_5']
        assert experiment in experiment_valid_values

        ensemble_member_valid_values = ['r10i1p1', 'r11i1p1', 'r12i1p1', 'r13i1p1', 'r14i1p1', 'r1i1p1', 'r1i1p2', 'r1i2p1', 'r1i2p2', 'r2i1p1', 'r2i3p1', 'r3i1p1', 'r3i2p1', 'r4i1p1', 'r4i3p1', 'r5i1p1', 'r5i3p1', 'r6i1p1', 'r6i1p2', 'r6i1p3', 'r7i1p1', 'r8i1p1', 'r9i1p1']
        assert ensemble_member in ensemble_member_valid_values

        return download_data(period=period, model=model, variable=variable, experiment=experiment, ensemble_member=ensemble_member)

class Collection_sis_biodiversity_era5_global(Collection):

    @Collection.wrapper
    def download(cls, statistic: OneOrMore[str], derived_variable: OneOrMore[str], temporal_aggregation: OneOrMore[str], variable: OneOrMore[str], version: OneOrMore[str] = '1.0'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, statistic: OneOrMore[str], derived_variable: OneOrMore[str], temporal_aggregation: OneOrMore[str], variable: OneOrMore[str], version: OneOrMore[str] = '1.0'):
        statistic_valid_values = ['mean', 'median', '25th_quartile', '75th_quartile']
        assert statistic in statistic_valid_values

        derived_variable_valid_values = ['annual_maximum', 'annual_maximum_of_daily_mean', 'annual_mean', 'annual_mean_of_daily_maximum', 'annual_mean_of_daily_minimum', 'annual_minimum', 'annual_sum', 'coldest_quarter', 'driest_quarter', 'end_of_season', 'length_of_season', 'maximum_length', 'mean_intensity', 'mean_length_with_minimum_5_days', 'monthly_mean', 'monthly_mean_of_daily_maximum', 'monthly_mean_of_daily_minimum', 'monthly_sum', 'number_of_occurrences', 'start_of_season', 'warmest_quarter', 'wettest_quarter']
        assert derived_variable in derived_variable_valid_values

        temporal_aggregation_valid_values = ['annual', 'monthly', 'climatology']
        assert temporal_aggregation in temporal_aggregation_valid_values

        variable_valid_values = ['annual_mean_temperature', 'mean_diurnal_range', 'isothermality', 'temperature_seasonality', 'maximum_temperature_of_warmest_month', 'minimum_temperature_of_coldest_month', 'temperature_annual_range', 'mean_temperature_of_wettest_quarter', 'mean_temperature_of_driest_quarter', 'mean_temperature_of_warmest_quarter', 'mean_temperature_of_coldest_quarter', 'annual_precipitation', 'precipitation_of_wettest_month', 'precipitation_of_driest_month', 'precipitation_seasonality', 'precipitation_of_wettest_quarter', 'precipitation_of_driest_quarter', 'precipitation_of_warmest_quarter', 'precipitation_of_coldest_quarter', 'aridity', 'dry_spells', 'dry_days', 'summer_days', 'surface_latent_heat_flux', 'surface_sensible_heat_flux', 'evaporative_fraction', 'frost_days', 'growing_season', 'growing_degree_days', 'growing_degree_days_during_growing_season_length', 'koeppen_geiger_class', 'potential_evaporation', 'sea_ice_concentration', 'sea_surface_temperature', '2m_temperature', 'precipitation', 'water_vapour_pressure', 'cloud_cover', 'volumetric_soil_water', 'wind_speed', 'zonal_wind_speed', 'meridional_wind_speed']
        assert variable in variable_valid_values

        version_valid_values = ['1_0']
        assert version in version_valid_values

        return download_data(statistic=statistic, derived_variable=derived_variable, temporal_aggregation=temporal_aggregation, variable=variable, version=version)

class Collection_reanalysis_era5_land_monthly_means(Collection):

    @Collection.wrapper
    def download(cls, time: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], download_format: str = 'unarchived', data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, time: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], download_format: str = 'unarchived', data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        time_valid_values = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
        assert time in time_valid_values

        year_valid_values = ['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        product_type_valid_values = ['monthly_averaged_reanalysis', 'monthly_averaged_reanalysis_by_hour_of_day']
        assert product_type in product_type_valid_values

        variable_valid_values = ['2m_dewpoint_temperature', '2m_temperature', 'skin_temperature', 'soil_temperature_level_1', 'soil_temperature_level_2', 'soil_temperature_level_3', 'soil_temperature_level_4', 'lake_bottom_temperature', 'lake_ice_depth', 'lake_ice_temperature', 'lake_mix_layer_depth', 'lake_mix_layer_temperature', 'lake_shape_factor', 'lake_total_layer_temperature', 'snow_albedo', 'snow_cover', 'snow_density', 'snow_depth', 'snow_depth_water_equivalent', 'snowfall', 'snowmelt', 'temperature_of_snow_layer', 'skin_reservoir_content', 'volumetric_soil_water_layer_1', 'volumetric_soil_water_layer_2', 'volumetric_soil_water_layer_3', 'volumetric_soil_water_layer_4', 'forecast_albedo', 'surface_latent_heat_flux', 'surface_net_solar_radiation', 'surface_net_thermal_radiation', 'surface_sensible_heat_flux', 'surface_solar_radiation_downwards', 'surface_thermal_radiation_downwards', 'evaporation_from_bare_soil', 'evaporation_from_open_water_surfaces_excluding_oceans', 'evaporation_from_the_top_of_canopy', 'evaporation_from_vegetation_transpiration', 'potential_evaporation', 'runoff', 'snow_evaporation', 'sub_surface_runoff', 'surface_runoff', 'total_evaporation', '10m_u_component_of_wind', '10m_v_component_of_wind', 'surface_pressure', 'total_precipitation', 'leaf_area_index_high_vegetation', 'leaf_area_index_low_vegetation']
        assert variable in variable_valid_values

        download_format_valid_values = ['unarchived', 'zip']
        assert download_format in download_format_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(time=time, year=year, month=month, product_type=product_type, variable=variable, download_format=download_format, data_format=data_format, area_group=area_group)

class Collection_insitu_comprehensive_upper_air_observation_network(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], year: OneOrMore[str], format: str, month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], year: OneOrMore[str], format: str, month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        year_valid_values = ['1905', '1906', '1907', '1908', '1909', '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
        assert year in year_valid_values

        format_valid_values = ['netcdf', 'csv']
        assert format in format_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['air_pressure', 'air_temperature', 'dew_point_temperature', 'dew_point_depression', 'specific_humidity', 'relative_humidity', 'wind_speed', 'wind_from_direction', 'eastward_wind_speed', 'northward_wind_speed', 'geopotential_height', 'wind_bias_estimate', 'rise_bias_estimate', 'desroziers_30_uncertainty', 'humidity_bias_estimate']
        assert variable in variable_valid_values

        return download_data(day=day, year=year, format=format, month=month, variable=variable, area_group=area_group)

class Collection_projections_cmip6(Collection):

    @Collection.wrapper
    def download(cls, level: OneOrMore[str], day: OneOrMore[str], model: str, year: OneOrMore[str], month: OneOrMore[str], temporal_resolution: str, variable: str, experiment: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, level: OneOrMore[str], day: OneOrMore[str], model: str, year: OneOrMore[str], month: OneOrMore[str], temporal_resolution: str, variable: str, experiment: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        level_valid_values = ['1', '5', '10', '20', '30', '50', '70', '100', '150', '200', '250', '300', '400', '500', '600', '700', '850', '925', '1000']
        assert level in level_valid_values

        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        model_valid_values = ['access_cm2', 'access_esm1_5', 'awi_cm_1_1_mr', 'awi_esm_1_1_lr', 'bcc_csm2_mr', 'bcc_esm1', 'cams_csm1_0', 'canesm5', 'canesm5_canoe', 'cesm2', 'cesm2_fv2', 'cesm2_waccm', 'cesm2_waccm_fv2', 'ciesm', 'cmcc_cm2_hr4', 'cmcc_cm2_sr5', 'cmcc_esm2', 'cnrm_cm6_1', 'cnrm_cm6_1_hr', 'cnrm_esm2_1', 'e3sm_1_0', 'e3sm_1_1', 'e3sm_1_1_eca', 'ec_earth3', 'ec_earth3_aerchem', 'ec_earth3_cc', 'ec_earth3_veg', 'ec_earth3_veg_lr', 'fgoals_f3_l', 'fgoals_g3', 'fio_esm_2_0', 'gfdl_esm4', 'giss_e2_1_g', 'giss_e2_1_h', 'hadgem3_gc31_ll', 'hadgem3_gc31_mm', 'iitm_esm', 'inm_cm4_8', 'inm_cm5_0', 'ipsl_cm5a2_inca', 'ipsl_cm6a_lr', 'kace_1_0_g', 'kiost_esm', 'mcm_ua_1_0', 'miroc6', 'miroc_es2h', 'miroc_es2l', 'mpi_esm_1_2_ham', 'mpi_esm1_2_hr', 'mpi_esm1_2_lr', 'mri_esm2_0', 'nesm3', 'norcpm1', 'noresm2_lm', 'noresm2_mm', 'sam0_unicon', 'taiesm1', 'ukesm1_0_ll']
        assert model in model_valid_values

        year_valid_values = ['1850', '1851', '1852', '1853', '1854', '1855', '1856', '1857', '1858', '1859', '1860', '1861', '1862', '1863', '1864', '1865', '1866', '1867', '1868', '1869', '1870', '1871', '1872', '1873', '1874', '1875', '1876', '1877', '1878', '1879', '1880', '1881', '1882', '1883', '1884', '1885', '1886', '1887', '1888', '1889', '1890', '1891', '1892', '1893', '1894', '1895', '1896', '1897', '1898', '1899', '1900', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909', '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057', '2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065', '2066', '2067', '2068', '2069', '2070', '2071', '2072', '2073', '2074', '2075', '2076', '2077', '2078', '2079', '2080', '2081', '2082', '2083', '2084', '2085', '2086', '2087', '2088', '2089', '2090', '2091', '2092', '2093', '2094', '2095', '2096', '2097', '2098', '2099', '2100', '2101', '2102', '2103', '2104', '2105', '2106', '2107', '2108', '2109', '2110', '2111', '2112', '2113', '2114', '2115', '2116', '2117', '2118', '2119', '2120', '2121', '2122', '2123', '2124', '2125', '2126', '2127', '2128', '2129', '2130', '2131', '2132', '2133', '2134', '2135', '2136', '2137', '2138', '2139', '2140', '2141', '2142', '2143', '2144', '2145', '2146', '2147', '2148', '2149', '2150', '2151', '2152', '2153', '2154', '2155', '2156', '2157', '2158', '2159', '2160', '2161', '2162', '2163', '2164', '2165', '2166', '2167', '2168', '2169', '2170', '2171', '2172', '2173', '2174', '2175', '2176', '2177', '2178', '2179', '2180', '2181', '2182', '2183', '2184', '2185', '2186', '2187', '2188', '2189', '2190', '2191', '2192', '2193', '2194', '2195', '2196', '2197', '2198', '2199', '2200', '2201', '2202', '2203', '2204', '2205', '2206', '2207', '2208', '2209', '2210', '2211', '2212', '2213', '2214', '2215', '2216', '2217', '2218', '2219', '2220', '2221', '2222', '2223', '2224', '2225', '2226', '2227', '2228', '2229', '2230', '2231', '2232', '2233', '2234', '2235', '2236', '2237', '2238', '2239', '2240', '2241', '2242', '2243', '2244', '2245', '2246', '2247', '2248', '2249', '2250', '2251', '2252', '2253', '2254', '2255', '2256', '2257', '2258', '2259', '2260', '2261', '2262', '2263', '2264', '2265', '2266', '2267', '2268', '2269', '2270', '2271', '2272', '2273', '2274', '2275', '2276', '2277', '2278', '2279', '2280', '2281', '2282', '2283', '2284', '2285', '2286', '2287', '2288', '2289', '2290', '2291', '2292', '2293', '2294', '2295', '2296', '2297', '2298', '2299', '2300']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        temporal_resolution_valid_values = ['monthly', 'daily', 'fixed']
        assert temporal_resolution in temporal_resolution_valid_values

        variable_valid_values = ['air_temperature', 'capacity_of_soil_to_store_water', 'daily_maximum_near_surface_air_temperature', 'daily_minimum_near_surface_air_temperature', 'eastward_near_surface_wind', 'eastward_wind', 'evaporation_including_sublimation_and_transpiration', 'geopotential_height', 'grid_cell_area_for_atmospheric_grid_variables', 'grid_cell_area_for_ocean_variables', 'land_ice_area_percentage', 'moisture_in_upper_portion_of_soil_column', 'near_surface_air_temperature', 'near_surface_relative_humidity', 'near_surface_specific_humidity', 'near_surface_wind_speed', 'northward_near_surface_wind', 'northward_wind', 'percentage_of_the_grid_cell_occupied_by_land_including_lakes', 'precipitation', 'relative_humidity', 'sea_area_percentage', 'sea_floor_depth_below_geoid', 'sea_ice_thickness', 'sea_level_pressure', 'sea_surface_height_above_geoid', 'sea_surface_salinity', 'sea_surface_temperature', 'sea_ice_area_percentage_on_ocean_grid', 'sea_ice_mass_per_area', 'snow_depth', 'snowfall_flux', 'specific_humidity', 'surface_air_pressure', 'surface_altitude', 'surface_downward_eastward_wind_stress', 'surface_downward_northward_wind_stress', 'surface_downwelling_longwave_radiation', 'surface_downwelling_shortwave_radiation', 'surface_snow_amount', 'surface_temperature', 'surface_temperature_of_sea_ice', 'surface_upward_latent_heat_flux', 'surface_upward_sensible_heat_flux', 'surface_upwelling_longwave_radiation', 'surface_upwelling_shortwave_radiation', 'toa_incident_shortwave_radiation', 'toa_outgoing_longwave_radiation', 'toa_outgoing_shortwave_radiation', 'total_cloud_cover_percentage', 'total_runoff']
        assert variable in variable_valid_values

        experiment_valid_values = ['historical', 'ssp1_1_9', 'ssp1_2_6', 'ssp4_3_4', 'ssp5_3_4os', 'ssp2_4_5', 'ssp4_6_0', 'ssp3_7_0', 'ssp5_8_5']
        assert experiment in experiment_valid_values

        return download_data(level=level, day=day, model=model, year=year, month=month, temporal_resolution=temporal_resolution, variable=variable, experiment=experiment, area_group=area_group)

class Collection_insitu_observations_gruan_reference_network(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], year: str, format: str, month: str, variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], year: str, format: str, month: str, variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        year_valid_values = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
        assert year in year_valid_values

        format_valid_values = ['netcdf', 'csv']
        assert format in format_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['air_temperature', 'relative_humidity', 'air_relative_humidity_effective_vertical_resolution', 'eastward_wind_speed', 'northward_wind_speed', 'wind_from_direction', 'wind_speed', 'shortwave_radiation', 'altitude', 'frost_point_temperature', 'geopotential_height', 'vertical_speed_of_radiosonde', 'water_vapour_mixing_ratio']
        assert variable in variable_valid_values

        return download_data(day=day, year=year, format=format, month=month, variable=variable, area_group=area_group)

class Collection_insitu_gridded_observations_europe(Collection):

    @Collection.wrapper
    def download(cls, grid_resolution: str, period: str, version: OneOrMore[str], product_type: str, variable: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, grid_resolution: str, period: str, version: OneOrMore[str], product_type: str, variable: OneOrMore[str]):
        grid_resolution_valid_values = ['0_1deg', '0_25deg']
        assert grid_resolution in grid_resolution_valid_values

        period_valid_values = ['full_period', '1950_1964', '1965_1979', '1980_1994', '1995_2010', '2011_2019', '2011_2020', '2011_2021', '2011_2022', '2011_2023', '2011_2024']
        assert period in period_valid_values

        version_valid_values = ['30_0e', '21_0e', '22_0e', '23_1e', '24_0e', '25_0e', '26_0e', '27_0e', '28_0e', '29_0e']
        assert version in version_valid_values

        product_type_valid_values = ['ensemble_mean', 'ensemble_spread', 'elevation']
        assert product_type in product_type_valid_values

        variable_valid_values = ['mean_temperature', 'minimum_temperature', 'maximum_temperature', 'precipitation_amount', 'sea_level_pressure', 'surface_shortwave_downwelling_radiation', 'relative_humidity', 'wind_speed', 'land_surface_elevation']
        assert variable in variable_valid_values

        return download_data(grid_resolution=grid_resolution, period=period, version=version, product_type=product_type, variable=variable)

class Collection_derived_era5_pressure_levels_daily_statistics(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], year: str, month: OneOrMore[str], variable: OneOrMore[str], pressure_level: OneOrMore[str], time_zone: str = 'utc+00:00', area_group: Union[FreeEditionType, GeographicExtentType] = 'global', frequency: str = '1_hourly', product_type: str = 'reanalysis', daily_statistic: str = 'daily_mean'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], year: str, month: OneOrMore[str], variable: OneOrMore[str], pressure_level: OneOrMore[str], time_zone: str = 'utc+00:00', area_group: Union[FreeEditionType, GeographicExtentType] = 'global', frequency: str = '1_hourly', product_type: str = 'reanalysis', daily_statistic: str = 'daily_mean'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        year_valid_values = ['1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['divergence', 'fraction_of_cloud_cover', 'geopotential', 'ozone_mass_mixing_ratio', 'potential_vorticity', 'relative_humidity', 'specific_cloud_ice_water_content', 'specific_cloud_liquid_water_content', 'specific_humidity', 'specific_rain_water_content', 'specific_snow_water_content', 'temperature', 'u_component_of_wind', 'v_component_of_wind', 'vertical_velocity', 'vorticity']
        assert variable in variable_valid_values

        pressure_level_valid_values = ['1', '2', '3', '5', '7', '10', '20', '30', '50', '70', '100', '125', '150', '175', '200', '225', '250', '300', '350', '400', '450', '500', '550', '600', '650', '700', '750', '775', '800', '825', '850', '875', '900', '925', '950', '975', '1000']
        assert pressure_level in pressure_level_valid_values

        time_zone_valid_values = ['utc-12:00', 'utc-11:00', 'utc-10:00', 'utc-09:00', 'utc-08:00', 'utc-07:00', 'utc-06:00', 'utc-05:00', 'utc-04:00', 'utc-03:00', 'utc-02:00', 'utc-01:00', 'utc+00:00', 'utc+01:00', 'utc+02:00', 'utc+03:00', 'utc+04:00', 'utc+05:00', 'utc+06:00', 'utc+07:00', 'utc+08:00', 'utc+09:00', 'utc+10:00', 'utc+11:00', 'utc+12:00', 'utc+13:00', 'utc+14:00']
        assert time_zone in time_zone_valid_values

        frequency_valid_values = ['1_hourly', '3_hourly', '6_hourly']
        assert frequency in frequency_valid_values

        product_type_valid_values = ['reanalysis', 'ensemble_members', 'ensemble_mean']
        assert product_type in product_type_valid_values

        daily_statistic_valid_values = ['daily_mean', 'daily_minimum', 'daily_maximum']
        assert daily_statistic in daily_statistic_valid_values

        return download_data(day=day, year=year, month=month, variable=variable, pressure_level=pressure_level, time_zone=time_zone, area_group=area_group, frequency=frequency, product_type=product_type, daily_statistic=daily_statistic)

class Collection_reanalysis_era5_complete(Collection):

    @Collection.wrapper
    def download(cls, download_instructions: Optional[str] = None): UNREACHABLE()
    
    @classmethod
    def __download__(cls, download_instructions: Optional[str] = None):
        return download_data(download_instructions=download_instructions)

class Collection_derived_near_surface_meteorological_variables(Collection):

    @Collection.wrapper
    def download(cls, reference_dataset: str, year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], version: OneOrMore[str] = '2.1'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, reference_dataset: str, year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], version: OneOrMore[str] = '2.1'):
        reference_dataset_valid_values = ['cru', 'cru_and_gpcc']
        assert reference_dataset in reference_dataset_valid_values

        year_valid_values = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['grid_point_altitude', 'near_surface_wind_speed', 'near_surface_air_temperature', 'surface_air_pressure', 'near_surface_specific_humidity', 'surface_downwelling_shortwave_radiation', 'surface_downwelling_longwave_radiation', 'rainfall_flux', 'snowfall_flux']
        assert variable in variable_valid_values

        version_valid_values = ['deprecated (1.0)', '1_1', '2_0', '2_1']
        assert version in version_valid_values

        return download_data(reference_dataset=reference_dataset, year=year, month=month, variable=variable, version=version)

class Collection_sis_tourism_snow_indicators(Collection):

    @Collection.wrapper
    def download(cls, period: OneOrMore[str], time_aggregation: str, version: OneOrMore[str], statistic: OneOrMore[str], year: OneOrMore[str], rcm: str, gcm: OneOrMore[str], variable: OneOrMore[str], experiment: str): UNREACHABLE()
    
    @classmethod
    def __download__(cls, period: OneOrMore[str], time_aggregation: str, version: OneOrMore[str], statistic: OneOrMore[str], year: OneOrMore[str], rcm: str, gcm: OneOrMore[str], variable: OneOrMore[str], experiment: str):
        period_valid_values = ['1961_1990', '1986_2005', '1990_2015', '2021_2040', '2041_2060', '2081_2100']
        assert period in period_valid_values

        time_aggregation_valid_values = ['climatology', 'annual_data']
        assert time_aggregation in time_aggregation_valid_values

        version_valid_values = ['1_0', '1_1']
        assert version in version_valid_values

        statistic_valid_values = ['10th_percentile', '20th_percentile', '50th_percentile', '80th_percentile', '90th_percentile', 'mean', 'standard_deviation']
        assert statistic in statistic_valid_values

        year_valid_values = ['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057', '2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065', '2066', '2067', '2068', '2069', '2070', '2071', '2072', '2073', '2074', '2075', '2076', '2077', '2078', '2079', '2080', '2081', '2082', '2083', '2084', '2085', '2086', '2087', '2088', '2089', '2090', '2091', '2092', '2093', '2094', '2095', '2096', '2097', '2098', '2099', '2100']
        assert year in year_valid_values

        rcm_valid_values = ['cclm4_8_17', 'aladin53', 'wrf331f', 'remo2009', 'rca4']
        assert rcm in rcm_valid_values

        gcm_valid_values = ['mpi_esm_lr', 'cnrm_cm5', 'cm5a_mr', 'hadgem2_es', 'ec_earth']
        assert gcm in gcm_valid_values

        variable_valid_values = ['start_of_the_longest_period_with_groomed_snow', 'start_of_the_longest_period_with_managed_snow', 'start_of_the_longest_period_with_natural_snow', 'end_of_the_longest_period_with_groomed_snow', 'end_of_the_longest_period_with_managed_snow', 'end_of_the_longest_period_with_natural_snow', 'annual_amount_of_machine_made_snow_produced', 'total_precipitation_from_november_to_april', 'total_snow_precipitation_from_november_to_april', 'period_with_medium_height_of_groomed_snow', 'period_with_medium_height_of_managed_snow', 'period_with_medium_height_of_natural_snow', 'period_with_low_height_of_groomed_snow', 'period_with_low_height_of_managed_snow', 'period_with_low_height_of_natural_snow', 'period_with_high_height_of_groomed_snow', 'period_with_high_height_of_managed_snow', 'period_with_high_height_of_natural_snow', 'period_with_medium_height_of_groomed_snow_between_fourth_and_tenth_december', 'period_with_medium_height_of_managed_snow_between_fourth_and_tenth_december', 'period_with_medium_height_of_natural_snow_between_fourth_and_tenth_december', 'period_with_medium_height_of_groomed_snow_between_twenty_second_december_and_fourth_january', 'period_with_medium_height_of_managed_snow_between_twenty_second_december_and_fourth_january', 'period_with_medium_height_of_natural_snow_between_twenty_second_december_and_fourth_january', 'period_with_medium_amount_of_groomed_snow', 'period_with_medium_amount_of_managed_snow', 'period_with_medium_amount_of_natural_snow', 'period_with_high_amount_of_groomed_snow', 'period_with_high_amount_of_managed_snow', 'period_with_high_amount_of_natural_snow', 'mean_winter_air_temperature', 'monthly_mean_air_temperature_for_november', 'monthly_mean_air_temperature_for_december', 'monthly_mean_air_temperature_for_january', 'monthly_mean_air_temperature_for_february', 'monthly_mean_air_temperature_for_march', 'monthly_mean_air_temperature_for_april', 'snow_making_hours_for_WBT_lower_than_negative_2_degc', 'snow_making_hours_for_WBT_lower_than_negative_5_degc']
        assert variable in variable_valid_values

        experiment_valid_values = ['historical', 'rcp2_6', 'rcp4_5', 'rcp8_5', 'uerra_reanalysis']
        assert experiment in experiment_valid_values

        return download_data(period=period, time_aggregation=time_aggregation, version=version, statistic=statistic, year=year, rcm=rcm, gcm=gcm, variable=variable, experiment=experiment)

class Collection_reanalysis_uerra_europe_complete(Collection):

    @Collection.wrapper
    def download(cls, download_instructions: Optional[str] = None): UNREACHABLE()
    
    @classmethod
    def __download__(cls, download_instructions: Optional[str] = None):
        return download_data(download_instructions=download_instructions)

class Collection_sis_european_risk_extreme_precipitation_indicators(Collection):

    @Collection.wrapper
    def download(cls, return_period: OneOrMore[str], period: OneOrMore[str], percentile: OneOrMore[str], city: OneOrMore[str], temporal_aggregation: OneOrMore[str], product_type: OneOrMore[str], spatial_coverage: OneOrMore[str], variable: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, return_period: OneOrMore[str], period: OneOrMore[str], percentile: OneOrMore[str], city: OneOrMore[str], temporal_aggregation: OneOrMore[str], product_type: OneOrMore[str], spatial_coverage: OneOrMore[str], variable: OneOrMore[str]):
        return_period_valid_values = ['10-yrs', '100-yrs', '25-yrs', '5-yrs', '50-yrs']
        assert return_period in return_period_valid_values

        period_valid_values = ['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '1989_2018']
        assert period in period_valid_values

        percentile_valid_values = ['90th', '95th', '99th']
        assert percentile in percentile_valid_values

        city_valid_values = ['amadora', 'amersfoort', 'antwerp', 'athens', 'bilbao', 'birmingham', 'brussels', 'bucharest', 'budapest', 'frankfurt_am_main', 'koln', 'london', 'milan', 'pamplona', 'paris', 'prague', 'riga', 'rimini', 'stockholm', 'vienna']
        assert city in city_valid_values

        temporal_aggregation_valid_values = ['30_year', 'daily', 'monthly', 'yearly']
        assert temporal_aggregation in temporal_aggregation_valid_values

        product_type_valid_values = ['e_obs', 'eca_d', 'era5', 'era5_2km']
        assert product_type in product_type_valid_values

        spatial_coverage_valid_values = ['city', 'europe']
        assert spatial_coverage in spatial_coverage_valid_values

        variable_valid_values = ['maximum_1_day_precipitation', 'maximum_5_day_precipitation', 'number_of_consecutive_wet_days', 'number_of_precipitation_days_exceeding_20mm', 'number_of_precipitation_days_exceeding_fixed_percentiles', 'number_of_wet_days', 'total_precipitation', 'precipitation_at_fixed_percentiles', 'precipitation_at_fixed_return_periods', 'standardised_precipitation_exceeding_fixed_percentiles']
        assert variable in variable_valid_values

        return download_data(return_period=return_period, period=period, percentile=percentile, city=city, temporal_aggregation=temporal_aggregation, product_type=product_type, spatial_coverage=spatial_coverage, variable=variable)

class Collection_satellite_total_column_water_vapour_land_ocean(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], product: str, year: OneOrMore[str], month: OneOrMore[str], temporal_aggregation: str, horizontal_aggregation: OneOrMore[str], variable: str = 'all'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], product: str, year: OneOrMore[str], month: OneOrMore[str], temporal_aggregation: str, horizontal_aggregation: OneOrMore[str], variable: str = 'all'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        product_valid_values = ['c3s_meris_and_ssm_i', 'near_infrared_hoaps_combined']
        assert product in product_valid_values

        year_valid_values = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        temporal_aggregation_valid_values = ['monthly', 'daily']
        assert temporal_aggregation in temporal_aggregation_valid_values

        horizontal_aggregation_valid_values = ['0_05_x_0_05', '0_5_x_0_5']
        assert horizontal_aggregation in horizontal_aggregation_valid_values

        variable_valid_values = ['all']
        assert variable in variable_valid_values

        return download_data(day=day, product=product, year=year, month=month, temporal_aggregation=temporal_aggregation, horizontal_aggregation=horizontal_aggregation, variable=variable)

class Collection_sis_temperature_statistics(Collection):

    @Collection.wrapper
    def download(cls, period: str, ensemble_statistic: OneOrMore[str], statistic: OneOrMore[str], variable: str, experiment: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, period: str, ensemble_statistic: OneOrMore[str], statistic: OneOrMore[str], variable: str, experiment: OneOrMore[str]):
        period_valid_values = ['summer', 'winter', 'year']
        assert period in period_valid_values

        ensemble_statistic_valid_values = ['ensemble_members_average', 'ensemble_members_standard_deviation']
        assert ensemble_statistic in ensemble_statistic_valid_values

        statistic_valid_values = ['time_average', '1st_percentile', '5th_percentile', '10th_percentile', '25th_percentile', '50th_percentile', '75th_percentile', '90th_percentile', '95th_percentile', '97th_percentile', '99th_percentile']
        assert statistic in statistic_valid_values

        variable_valid_values = ['maximum_temperature', 'minimum_temperature', 'average_temperature']
        assert variable in variable_valid_values

        experiment_valid_values = ['rcp4_5', 'rcp8_5']
        assert experiment in experiment_valid_values

        return download_data(period=period, ensemble_statistic=ensemble_statistic, statistic=statistic, variable=variable, experiment=experiment)

class Collection_satellite_fire_radiative_power(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time_aggregation: str, version: OneOrMore[str], year: str, observation_time: OneOrMore[str], month: OneOrMore[str], satellite: OneOrMore[str], horizontal_aggregation: str, product_type: str, variable: str = 'all'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time_aggregation: str, version: OneOrMore[str], year: str, observation_time: OneOrMore[str], month: OneOrMore[str], satellite: OneOrMore[str], horizontal_aggregation: str, product_type: str, variable: str = 'all'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_aggregation_valid_values = ['day', '27_days', 'month']
        assert time_aggregation in time_aggregation_valid_values

        version_valid_values = ['1_0', '1_2']
        assert version in version_valid_values

        year_valid_values = ['2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        observation_time_valid_values = ['night', 'day']
        assert observation_time in observation_time_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        satellite_valid_values = ['sentinel_3a', 'sentinel_3b']
        assert satellite in satellite_valid_values

        horizontal_aggregation_valid_values = ['0_1_degree_x_0_1_degree', '0_25_degree_x_0_25_degree']
        assert horizontal_aggregation in horizontal_aggregation_valid_values

        product_type_valid_values = ['gridded', 'table_summary']
        assert product_type in product_type_valid_values

        variable_valid_values = ['all']
        assert variable in variable_valid_values

        return download_data(day=day, time_aggregation=time_aggregation, version=version, year=year, observation_time=observation_time, month=month, satellite=satellite, horizontal_aggregation=horizontal_aggregation, product_type=product_type, variable=variable)

class Collection_satellite_methane(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], sensor_and_algorithm: str, version: OneOrMore[str], year: OneOrMore[str], processing_level: OneOrMore[str], month: OneOrMore[str], variable: str): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], sensor_and_algorithm: str, version: OneOrMore[str], year: OneOrMore[str], processing_level: OneOrMore[str], month: OneOrMore[str], variable: str):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        sensor_and_algorithm_valid_values = ['iasi_metop_a_nlis', 'iasi_metop_b_nlis', 'iasi_metop_c_nlis', 'sciamachy_imap', 'sciamachy_wfmd', 'tanso_fts_ocfp', 'tanso_fts_ocpr', 'tanso_fts_srfp', 'tanso_fts_srpr', 'tanso2_fts_srfp', 'tanso2_fts_srpr', 'merged_emma', 'merged_obs4mips']
        assert sensor_and_algorithm in sensor_and_algorithm_valid_values

        version_valid_values = ['4_3', '4_5', '7_2', '7_3', '9_0', '9_1', '10_2', '2_0_1', '2_3_8', '2_3_9', '3', '3_0', '3_1', '4_0', '4_1', '4_2', '4_4', '4_5', '7_0', '7_1', '7_2', '7_3', '8_1', '8_4', '9_0', '9_1', '10_2', '2_0_0', '2_0_1', '2_3_8', '2_3_9']
        assert version in version_valid_values

        year_valid_values = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
        assert year in year_valid_values

        processing_level_valid_values = ['level_2', 'level_3']
        assert processing_level in processing_level_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['ch4', 'xch4']
        assert variable in variable_valid_values

        return download_data(day=day, sensor_and_algorithm=sensor_and_algorithm, version=version, year=year, processing_level=processing_level, month=month, variable=variable)

class Collection_satellite_ice_sheet_elevation_change(Collection):

    @Collection.wrapper
    def download(cls, climate_data_record_type: OneOrMore[str], version: OneOrMore[str], domain: OneOrMore[str], variable: str = 'all'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, climate_data_record_type: OneOrMore[str], version: OneOrMore[str], domain: OneOrMore[str], variable: str = 'all'):
        climate_data_record_type_valid_values = ['icdr', 'tcdr']
        assert climate_data_record_type in climate_data_record_type_valid_values

        version_valid_values = ['2_0', '3_0', '4_0', '5_0']
        assert version in version_valid_values

        domain_valid_values = ['antarctica', 'greenland']
        assert domain in domain_valid_values

        variable_valid_values = ['all']
        assert variable in variable_valid_values

        return download_data(climate_data_record_type=climate_data_record_type, version=version, domain=domain, variable=variable)

class Collection_seasonal_monthly_pressure_levels(Collection):

    @Collection.wrapper
    def download(cls, system: str, leadtime_month: OneOrMore[str], originating_centre: str, year: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], pressure_level: OneOrMore[str], data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, system: str, leadtime_month: OneOrMore[str], originating_centre: str, year: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], pressure_level: OneOrMore[str], data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        system_valid_values = ['1', '2', '3', '4', '5', '6', '7', '8', '12', '13', '14', '15', '21', '35', '51', '600', '601', '602', '603']
        assert system in system_valid_values

        leadtime_month_valid_values = ['1', '2', '3', '4', '5', '6']
        assert leadtime_month in leadtime_month_valid_values

        originating_centre_valid_values = ['ecmwf', 'ukmo', 'meteo_france', 'dwd', 'cmcc', 'ncep', 'jma', 'eccc']
        assert originating_centre in originating_centre_valid_values

        year_valid_values = ['1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        product_type_valid_values = ['ensemble_mean', 'hindcast_climate_mean', 'monthly_mean']
        assert product_type in product_type_valid_values

        variable_valid_values = ['geopotential', 'specific_humidity', 'temperature', 'u_component_of_wind', 'v_component_of_wind']
        assert variable in variable_valid_values

        pressure_level_valid_values = ['10', '30', '50', '100', '200', '300', '400', '500', '700', '850', '925', '1000']
        assert pressure_level in pressure_level_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(system=system, leadtime_month=leadtime_month, originating_centre=originating_centre, year=year, month=month, product_type=product_type, variable=variable, pressure_level=pressure_level, data_format=data_format, area_group=area_group)

class Collection_satellite_carbon_dioxide(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], sensor_and_algorithm: str, version: OneOrMore[str], year: OneOrMore[str], processing_level: OneOrMore[str], month: OneOrMore[str], variable: str): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], sensor_and_algorithm: str, version: OneOrMore[str], year: OneOrMore[str], processing_level: OneOrMore[str], month: OneOrMore[str], variable: str):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        sensor_and_algorithm_valid_values = ['airs_nlis', 'iasi_metop_a_nlis', 'iasi_metop_b_nlis', 'iasi_metop_c_nlis', 'sciamachy_wfmd', 'sciamachy_besd', 'tanso_fts_ocfp', 'tanso_fts_srfp', 'tanso2_fts_srfp', 'merged_emma', 'merged_obs4mips']
        assert sensor_and_algorithm in sensor_and_algorithm_valid_values

        version_valid_values = ['3_0', '4_5', '7_3', '10_1', '2_0_0', '2_3_8', '02_01_02', '3', '3_0', '3_1', '4_0', '4_1', '4_2', '4_3', '4_4', '4_5', '7_1', '7_2', '7_3', '8_0', '9_1', '10_1', '2_0_0', '2_3_8', '02_01_02']
        assert version in version_valid_values

        year_valid_values = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
        assert year in year_valid_values

        processing_level_valid_values = ['level_2', 'level_3']
        assert processing_level in processing_level_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['co2', 'xco2']
        assert variable in variable_valid_values

        return download_data(day=day, sensor_and_algorithm=sensor_and_algorithm, version=version, year=year, processing_level=processing_level, month=month, variable=variable)

class Collection_insitu_observations_surface_land(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time_aggregation: str, usage_restrictions: OneOrMore[str], year: OneOrMore[str], data_quality: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time_aggregation: str, usage_restrictions: OneOrMore[str], year: OneOrMore[str], data_quality: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_aggregation_valid_values = ['daily', 'monthly', 'sub_daily']
        assert time_aggregation in time_aggregation_valid_values

        usage_restrictions_valid_values = ['non_commercial', 'open']
        assert usage_restrictions in usage_restrictions_valid_values

        year_valid_values = ['1755', '1756', '1757', '1758', '1759', '1760', '1761', '1762', '1763', '1764', '1765', '1766', '1767', '1768', '1769', '1770', '1771', '1772', '1773', '1774', '1775', '1776', '1777', '1778', '1779', '1780', '1781', '1782', '1783', '1784', '1785', '1786', '1787', '1788', '1789', '1790', '1791', '1792', '1793', '1794', '1795', '1796', '1797', '1798', '1799', '1800', '1801', '1802', '1803', '1804', '1805', '1806', '1807', '1808', '1809', '1810', '1811', '1812', '1813', '1814', '1815', '1816', '1817', '1818', '1819', '1820', '1821', '1822', '1823', '1824', '1825', '1826', '1827', '1828', '1829', '1830', '1831', '1832', '1833', '1834', '1835', '1836', '1837', '1838', '1839', '1840', '1841', '1842', '1843', '1844', '1845', '1846', '1847', '1848', '1849', '1850', '1851', '1852', '1853', '1854', '1855', '1856', '1857', '1858', '1859', '1860', '1861', '1862', '1863', '1864', '1865', '1866', '1867', '1868', '1869', '1870', '1871', '1872', '1873', '1874', '1875', '1876', '1877', '1878', '1879', '1880', '1881', '1882', '1883', '1884', '1885', '1886', '1887', '1888', '1889', '1890', '1891', '1892', '1893', '1894', '1895', '1896', '1897', '1898', '1899', '1900', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909', '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
        assert year in year_valid_values

        data_quality_valid_values = ['failed', 'passed']
        assert data_quality in data_quality_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['accumulated_precipitation', 'air_pressure', 'air_pressure_at_sea_level', 'air_temperature', 'dew_point_temperature', 'fresh_snow', 'snow_depth', 'snow_water_equivalent', 'wind_from_direction', 'wind_speed']
        assert variable in variable_valid_values

        return download_data(day=day, time_aggregation=time_aggregation, usage_restrictions=usage_restrictions, year=year, data_quality=data_quality, month=month, variable=variable, area_group=area_group)

class Collection_projections_cmip5_monthly_single_levels(Collection):

    @Collection.wrapper
    def download(cls, period: OneOrMore[str], model: str, variable: OneOrMore[str], experiment: str, ensemble_member: str = 'r1i1p1'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, period: OneOrMore[str], model: str, variable: OneOrMore[str], experiment: str, ensemble_member: str = 'r1i1p1'):
        period_valid_values = ['188001-195012', '195001-199912', '195001-200912', '195101-200512', '195101-200812', '195101-201012', '197801-200812', '197804-197812', '197809-200811', '197809-200812', '197901-198312', '197901-198812', '197901-200512', '197901-200812', '197901-200912', '197901-201012', '198401-198812', '198901-199312', '198901-199812', '199401-199812', '199901-200312', '199901-200812', '200001-200912', '200401-200812', '200601-200812', '200812-200812', '200901-200912', '185001-185412', '185001-185512', '185001-185912', '185001-187512', '185001-189912', '185001-190012', '185001-195012', '185001-199012', '185001-200512', '185001-201212', '185101-187512', '185101-190012', '185501-185912', '185601-186112', '185912-185912', '185912-188411', '185912-195911', '186001-186412', '186001-186912', '186001-188412', '186101-186512', '186201-186712', '186501-186912', '186601-187012', '186801-187312', '187001-187412', '187001-187912', '187101-187512', '187401-187912', '187501-187912', '187601-188012', '187601-190012', '188001-188412', '188001-188512', '188001-188912', '188101-188512', '188101-200512', '188412-190911', '188501-188912', '188501-190912', '188601-189012', '188601-189112', '189001-189412', '189001-189912', '189101-189512', '189201-189712', '189501-189912', '189601-190012', '189801-190312', '190001-190412', '190001-190912', '190001-194912', '190001-199912', '190101-190512', '190101-192512', '190101-195012', '190401-190912', '190501-190912', '190601-191012', '190912-193411', '191001-191412', '191001-191512', '191001-191912', '191001-193412', '191101-191512', '191501-191912', '191601-192012', '191601-192112', '192001-192412', '192001-192912', '192101-192512', '192201-192712', '192501-192912', '192601-193012', '192601-195012', '192801-193312', '193001-193412', '193001-193912', '193101-193512', '193401-193912', '193412-195911', '193501-193912', '193501-195912', '193601-194012', '194001-194412', '194001-194512', '194001-194912', '194101-194512', '194501-194912', '194601-195012', '194601-195112', '195001-195012', '195001-195412', '195001-195912', '195001-199912', '195001-200512', '195001-201212', '195101-195112', '195101-195512', '195101-197512', '195101-200012', '195101-200512', '195101-201012', '195201-195212', '195201-195712', '195301-195312', '195401-195412', '195501-195512', '195501-195912', '195501-200512', '195601-195612', '195601-196012', '195701-195712', '195801-195812', '195801-196312', '195901-195912', '195912-198411', '195912-200110', '195912-200511', '195912-200512', '196001-196012', '196001-196412', '196001-196912', '196001-198412', '196101-196112', '196101-196512', '196101-200512', '196201-196212', '196301-196312', '196401-196412', '196401-196912', '196501-196512', '196501-196912', '196601-196612', '196601-197012', '196701-196712', '196801-196812', '196901-196912', '197001-197012', '197001-197412', '197001-197512', '197001-197912', '197101-197112', '197101-197512', '197201-197212', '197301-197312', '197401-197412', '197501-197512', '197501-197912', '197601-197612', '197601-198012', '197601-198112', '197601-200012', '197701-197712', '197801-197812', '197901-197912', '198001-198012', '198001-198412', '198001-198912', '198101-198112', '198101-198512', '198201-198212', '198201-198712', '198301-198312', '198401-198412', '198412-200511', '198412-200512', '198501-198512', '198501-198912', '198501-200512', '198601-198612', '198601-199012', '198701-198712', '198801-198812', '198801-199312', '198901-198912', '199001-199012', '199001-199412', '199001-199912', '199101-199112', '199101-199512', '199101-200512', '199201-199212', '199301-199312', '199401-199412', '199401-199912', '199501-199512', '199501-199912', '199601-199612', '199601-200012', '199701-199712', '199801-199812', '199901-199912', '200001-200012', '200001-200412', '200001-200512', '200001-200612', '200001-200912', '200001-201212', '200101-200112', '200101-200512', '200101-201012', '200112-200512', '200201-200212', '200301-200312', '200401-200412', '200501-200512', '200601-200612', '200601-201012', '200701-200712', '200801-200812', '200901-200911', '200901-200912', '201001-201412', '201101-201512', '201601-202012', '202101-202512', '202601-203012', '203101-203512', '203601-204012', '200501-200912', '200501-206512', '200501-209912', '200501-210012', '200512-201111', '200512-203011', '200512-209911', '200512-209912', '200512-210012', '200601-200612', '200601-200912', '200601-201012', '200601-201512', '200601-202512', '200601-203012', '200601-203512', '200601-204412', '200601-205012', '200601-205412', '200601-205512', '200601-206012', '200601-206512', '200601-209912', '200601-210012', '200601-210212', '200601-215012', '200601-220012', '200601-230012', '200701-200712', '200801-200812', '200901-200912', '201001-201012', '201001-201912', '201101-201112', '201101-201512', '201101-202012', '201112-203611', '201201-201212', '201301-201312', '201401-201412', '201501-201512', '201601-201612', '201601-202012', '201601-202512', '201701-201712', '201801-201812', '201901-201912', '202001-202012', '202001-202912', '202101-202112', '202101-202512', '202101-203012', '202201-202212', '202301-202312', '202401-202412', '202501-202512', '202601-202612', '202601-203012', '202601-203512', '202601-205012', '202701-202712', '202801-202812', '202901-202912', '203001-203012', '203001-203912', '203012-205511', '203101-203112', '203101-203512', '203101-204012', '203201-203212', '203301-203312', '203401-203412', '203501-203512', '203601-203612', '203601-204012', '203601-204512', '203612-206111', '203701-203712', '203801-203812', '203901-203912', '204001-204012', '204001-204912', '204101-204112', '204101-204512', '204101-205012', '204201-204212', '204301-204312', '204401-204412', '204501-204512', '204501-210012', '204601-204612', '204601-205012', '204601-205512', '204701-204712', '204801-204812', '204901-204912', '205001-205012', '205001-205912', '205101-205112', '205101-205512', '205101-206012', '205101-207512', '205101-209912', '205101-210012', '205101-210112', '205201-205207', '205201-205212', '205301-205311', '205301-205312', '205401-205406', '205401-205412', '205501-205507', '205501-205512', '205512-208011', '205601-205612', '205601-206012', '205601-206512', '205601-209912', '205601-210012', '205701-205712', '205801-205812', '205901-205912', '206001-206012', '206001-206912', '206101-206112', '206101-206512', '206101-207012', '206101-210112', '206112-208611', '206201-206212', '206301-206312', '206401-206412', '206501-206512', '206601-206612', '206601-207012', '206601-207512', '206601-209912', '206701-206712', '206801-206812', '206901-206912', '207001-207012', '207001-207912', '207101-207112', '207101-207512', '207101-208012', '207201-207212', '207301-207312', '207401-207412', '207501-207512', '207601-207612', '207601-208012', '207601-208512', '207601-210012', '207701-207712', '207801-207812', '207901-207912', '208001-208012', '208001-208912', '208012-209511', '208012-209910', '208012-209911', '208012-209912', '208012-210011', '208012-210012', '208101-208112', '208101-208512', '208101-209012', '208201-208212', '208301-208312', '208401-208412', '208501-208512', '208601-208612', '208601-209012', '208601-209512', '208612-209911', '208612-209912', '208701-208712', '208801-208812', '208901-208912', '209001-209012', '209001-209912', '209001-210012', '209101-209112', '209101-209412', '209101-209512', '209101-210012', '209201-209212', '209301-209312', '209401-209412', '209501-209512', '209512-209912', '209601-209612', '209601-209912', '209601-210012', '209601-210112', '209601-210512', '209701-209712', '209801-209812', '209901-209902', '209901-209912', '209911-209912', '209912-210012', '209912-212411', '209912-219911', '210001-210012', '210001-230012', '210012-210012', '210101-211012', '210101-212512', '210101-215012', '210101-229912', '210101-230012', '210601-211512', '211101-212012', '211601-212512', '212101-213012', '212412-214911', '212601-213512', '212601-215012', '213101-214012', '213601-214512', '214101-215012', '214601-215512', '214912-217411', '215101-216012', '215101-217512', '215101-220012', '215601-216512', '216101-217012', '216601-217512', '217101-218012', '217412-219911', '217601-218512', '217601-220012', '218101-219012', '218601-219512', '219101-220012', '219601-220512', '219912-222411', '219912-229911', '220101-221012', '220101-222512', '220101-225012', '220601-221512', '221101-222012', '221601-222512', '222101-223012', '222412-224911', '222601-223512', '222601-225012', '223101-224012', '223601-224512', '224101-225012', '224601-225512', '224912-227411', '225101-226012', '225101-227512', '225101-230012', '225601-226512', '226101-227012', '226601-227512', '227101-228012', '227412-229911', '227601-230012', '228101-229012', '229101-230012', '229912-229912']
        assert period in period_valid_values

        model_valid_values = ['access1_0', 'access1_3', 'bcc_csm1_1', 'bcc_csm1_1_m', 'bnu_esm', 'ccsm4', 'cesm1_bgc', 'cesm1_cam5', 'cesm1_fastchem', 'cesm1_waccm', 'cmcc_cesm', 'cmcc_cm', 'cmcc_cms', 'cnrm_cm5', 'cnrm_cm5_2', 'csiro_mk3_6_0', 'canam4', 'cancm4', 'canesm2', 'ec_earth', 'fgoals_g2', 'fgoals_s2', 'fio_esm', 'gfdl_cm2p1', 'gfdl_cm3', 'gfdl_esm2g', 'gfdl_esm2m', 'gfdl_hiram_c180', 'gfdl_hiram_c360', 'giss_e2_h', 'giss_e2_h_cc', 'giss_e2_r', 'giss_e2_r_cc', 'hadcem3', 'hadgem2_a', 'hadgem2_cc', 'hadgem2_es', 'inmcm4', 'ipsl_cm5a_lr', 'ipsl_cm5a_mr', 'ipsl_cm5b_lr', 'mpi_esm_lr', 'mpi_esm_mr', 'mpi_esm_p', 'noresm1_m', 'noresm1_me']
        assert model in model_valid_values

        variable_valid_values = ['10m_wind_speed', '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_temperature', 'eastward_turbulent_surface_stress', 'evaporation', 'maximum_2m_temperature_in_the_last_24_hours', 'mean_precipitation_flux', 'mean_sea_level_pressure', 'minimum_2m_temperature_in_the_last_24_hours', 'near_surface_relative_humidity', 'near_surface_specific_humidity', 'northward_turbulent_surface_stress', 'runoff', 'sea_ice_fraction', 'sea_ice_plus_snow_amount', 'sea_ice_thickness', 'sea_surface_salinity', 'sea_surface_temperature', 'sea_ice_surface_temperature', 'sea_surface_height_above_geoid', 'skin_temperature', 'snow_depth_over_sea_ice', 'snowfall', 'soil_moisture_content', 'surface_latent_heat_flux', 'surface_sensible_heat_flux', 'surface_pressure', 'surface_thermal_radiation_downwards', 'surface_upwelling_longwave_radiat_ion', 'surface_solar_radiation_downwards', 'surface_upwelling_shortwave_radiation', 'surface_snow_amount', 'toa_outgoing_longwave_radiation', 'toa_outgoing_clear_sky_longwave_radiation', 'toa_incident_solar_radiation', 'toa_outgoing_shortwave_radiation', 'toa_outgoing_clear_sky_short_wave_radiation', 'total_cloud_cover']
        assert variable in variable_valid_values

        experiment_valid_values = ['amip', 'historical', 'rcp_2_6', 'rcp_4_5', 'rcp_6_0', 'rcp_8_5']
        assert experiment in experiment_valid_values

        ensemble_member_valid_values = ['r10i1p1', 'r11i1p1', 'r12i1p1', 'r13i1p1', 'r14i1p1', 'r1i1p1', 'r1i1p121', 'r1i1p124', 'r1i1p125', 'r1i1p126', 'r1i1p127', 'r1i1p128', 'r1i1p2', 'r1i1p3', 'r1i2p1', 'r1i2p2', 'r2i1p1', 'r2i1p2', 'r2i1p3', 'r2i3p1', 'r3i1p1', 'r3i1p2', 'r3i1p3', 'r3i2p1', 'r4i1p1', 'r4i1p2', 'r4i1p3', 'r4i3p1', 'r5i1p1', 'r5i1p2', 'r5i1p3', 'r5i3p1', 'r6i1p1', 'r6i1p2', 'r6i1p3', 'r7i1p1', 'r8i1p1', 'r9i1p1']
        assert ensemble_member in ensemble_member_valid_values

        return download_data(period=period, model=model, variable=variable, experiment=experiment, ensemble_member=ensemble_member)

class Collection_insitu_observations_surface_marine(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], year: OneOrMore[str], data_quality: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], year: OneOrMore[str], data_quality: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        year_valid_values = ['1851', '1852', '1853', '1854', '1855', '1856', '1857', '1858', '1859', '1860', '1861', '1862', '1863', '1864', '1865', '1866', '1867', '1868', '1869', '1870', '1871', '1872', '1873', '1874', '1875', '1876', '1877', '1878', '1879', '1880', '1881', '1882', '1883', '1884', '1885', '1886', '1887', '1888', '1889', '1890', '1891', '1892', '1893', '1894', '1895', '1896', '1897', '1898', '1899', '1900', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909', '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010']
        assert year in year_valid_values

        data_quality_valid_values = ['failed', 'passed']
        assert data_quality in data_quality_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['air_pressure_at_sea_level', 'air_temperature', 'dew_point_temperature', 'water_temperature', 'wind_from_direction', 'wind_speed']
        assert variable in variable_valid_values

        return download_data(day=day, year=year, data_quality=data_quality, month=month, variable=variable, area_group=area_group)

class Collection_seasonal_monthly_ocean(Collection):

    @Collection.wrapper
    def download(cls, system: str, originating_centre: str, year: OneOrMore[str], month: OneOrMore[str], forecast_type: OneOrMore[str], variable: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, system: str, originating_centre: str, year: OneOrMore[str], month: OneOrMore[str], forecast_type: OneOrMore[str], variable: OneOrMore[str]):
        system_valid_values = ['8', '21', '35', '51', '602', '603']
        assert system in system_valid_values

        originating_centre_valid_values = ['ecmwf', 'ukmo', 'meteo_france', 'dwd', 'cmcc']
        assert originating_centre in originating_centre_valid_values

        year_valid_values = ['1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        forecast_type_valid_values = ['forecast', 'hindcast']
        assert forecast_type in forecast_type_valid_values

        variable_valid_values = ['mixed_layer_depth_0_01', 'sea_ice_thickness', 'depth_average_salinity_of_upper_300m', 'depth_average_potential_temperature_of_upper_300m', 'mixed_layer_depth_0_03', 'sea_surface_salinity', 'depth_of_14_c_isotherm', 'depth_of_17_c_isotherm', 'depth_of_20_c_isotherm', 'depth_of_26_c_isotherm', 'depth_of_28_c_isotherm', 'sea_surface_height_above_geoid']
        assert variable in variable_valid_values

        return download_data(system=system, originating_centre=originating_centre, year=year, month=month, forecast_type=forecast_type, variable=variable)

class Collection_seasonal_monthly_single_levels(Collection):

    @Collection.wrapper
    def download(cls, system: str, leadtime_month: OneOrMore[str], originating_centre: str, year: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, system: str, leadtime_month: OneOrMore[str], originating_centre: str, year: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        system_valid_values = ['1', '2', '3', '4', '5', '6', '7', '8', '12', '13', '14', '15', '21', '35', '51', '600', '601', '602', '603']
        assert system in system_valid_values

        leadtime_month_valid_values = ['1', '2', '3', '4', '5', '6']
        assert leadtime_month in leadtime_month_valid_values

        originating_centre_valid_values = ['ecmwf', 'ukmo', 'meteo_france', 'dwd', 'cmcc', 'ncep', 'jma', 'eccc']
        assert originating_centre in originating_centre_valid_values

        year_valid_values = ['1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        product_type_valid_values = ['ensemble_mean', 'hindcast_climate_mean', 'monthly_mean', 'monthly_minimum', 'monthly_maximum', 'monthly_standard_deviation']
        assert product_type in product_type_valid_values

        variable_valid_values = ['10m_u_component_of_wind', '10m_v_component_of_wind', '10m_wind_gust_since_previous_post_processing', '10m_wind_speed', '2m_dewpoint_temperature', '2m_temperature', 'east_west_surface_stress_rate_of_accumulation', 'evaporation', 'maximum_2m_temperature_in_the_last_24_hours', 'mean_sea_level_pressure', 'mean_sub_surface_runoff_rate', 'mean_surface_runoff_rate', 'minimum_2m_temperature_in_the_last_24_hours', 'north_south_surface_stress_rate_of_accumulation', 'runoff', 'sea_surface_temperature', 'sea_ice_cover', 'snow_density', 'snow_depth', 'snowfall', 'soil_temperature_level_1', 'solar_insolation_rate_of_accumulation', 'surface_latent_heat_flux', 'surface_sensible_heat_flux', 'surface_solar_radiation', 'surface_solar_radiation_downwards', 'surface_thermal_radiation', 'surface_thermal_radiation_downwards', 'top_solar_radiation', 'top_thermal_radiation', 'total_cloud_cover', 'total_column_cloud_ice_water', 'total_column_cloud_liquid_water', 'total_column_water_vapour', 'total_precipitation']
        assert variable in variable_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(system=system, leadtime_month=leadtime_month, originating_centre=originating_centre, year=year, month=month, product_type=product_type, variable=variable, data_format=data_format, area_group=area_group)

class Collection_satellite_greenland_ice_sheet_velocity(Collection):

    @Collection.wrapper
    def download(cls, period: OneOrMore[str], version: OneOrMore[str], variable: str = 'all'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, period: OneOrMore[str], version: OneOrMore[str], variable: str = 'all'):
        period_valid_values = ['2017_2018', '2018_2019', '2019_2020', '2020_2021']
        assert period in period_valid_values

        version_valid_values = ['1_2', '1_3', '1_4']
        assert version in version_valid_values

        variable_valid_values = ['all']
        assert variable in variable_valid_values

        return download_data(period=period, version=version, variable=variable)

class Collection_satellite_ozone_v1(Collection):

    @Collection.wrapper
    def download(cls, version: OneOrMore[str], year: OneOrMore[str], sensor: OneOrMore[str], processing_level: str, month: OneOrMore[str], vertical_aggregation: str, algorithm: str, variable: str): UNREACHABLE()
    
    @classmethod
    def __download__(cls, version: OneOrMore[str], year: OneOrMore[str], sensor: OneOrMore[str], processing_level: str, month: OneOrMore[str], vertical_aggregation: str, algorithm: str, variable: str):
        version_valid_values = ['v0001', 'v0002', 'v0003', 'v0004', 'v0005', 'v0006', 'v0007', 'v0008', 'v0009', 'v0020', 'v0021', 'v0022', 'v0023', 'v0024', 'v0025', 'v0100', 'v0101', 'v0200', 'v0300', 'v0400', 'v0500', 'v0600', 'v0700', 'v0800', 'v0900', 'v1000', 'v1100', 'v2000']
        assert version in version_valid_values

        year_valid_values = ['1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
        assert year in year_valid_values

        sensor_valid_values = ['msr', 'merged_uv', 'merged_np', 'allg', 'cllg', 'amzm', 'cmzm', 'ace', 'gome', 'gome2_a', 'gome2_b', 'gome2_c', 'gomos', 'haloe', 'iasi_a_day_time', 'iasi_a_night_time', 'iasi_b_day_time', 'iasi_b_night_time', 'iasi_c_day_time', 'iasi_c_night_time', 'mipas', 'mls', 'omi', 'omps', 'osiris', 'saber', 'sage_2', 'sage_3', 'sciamachy', 'smr', 'tropomi']
        assert sensor in sensor_valid_values

        processing_level_valid_values = ['level_3', 'level_4']
        assert processing_level in processing_level_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        vertical_aggregation_valid_values = ['total_column', 'tropospheric_column_0_6_km', 'vertical_profiles_from_limb_sensors', 'vertical_profiles_from_nadir_sensors']
        assert vertical_aggregation in vertical_aggregation_valid_values

        algorithm_valid_values = ['ubr', 'usask']
        assert algorithm in algorithm_valid_values

        variable_valid_values = ['mole_concentration_of_ozone_in_air', 'mole_fraction_of_ozone_in_air', 'anomaly_of_mole_concentration_of_ozone_in_air', 'mole_content_of_ozone_in_atmosphere_layer', 'atmosphere_mole_content_of_ozone']
        assert variable in variable_valid_values

        return download_data(version=version, year=year, sensor=sensor, processing_level=processing_level, month=month, vertical_aggregation=vertical_aggregation, algorithm=algorithm, variable=variable)

class Collection_derived_era5_single_levels_daily_statistics(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], year: str, month: OneOrMore[str], variable: OneOrMore[str], time_zone: str = 'utc+00:00', area_group: Union[FreeEditionType, GeographicExtentType] = 'global', frequency: str = '1_hourly', product_type: str = 'reanalysis', daily_statistic: str = 'daily_mean'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], year: str, month: OneOrMore[str], variable: OneOrMore[str], time_zone: str = 'utc+00:00', area_group: Union[FreeEditionType, GeographicExtentType] = 'global', frequency: str = '1_hourly', product_type: str = 'reanalysis', daily_statistic: str = 'daily_mean'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        year_valid_values = ['1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['10m_u_component_of_wind', '10m_v_component_of_wind', '2m_dewpoint_temperature', '2m_temperature', 'mean_sea_level_pressure', 'mean_wave_direction', 'mean_wave_period', 'sea_surface_temperature', 'significant_height_of_combined_wind_waves_and_swell', 'surface_pressure', 'total_precipitation', '2m_dewpoint_temperature', '2m_temperature', 'ice_temperature_layer_1', 'ice_temperature_layer_2', 'ice_temperature_layer_3', 'ice_temperature_layer_4', 'maximum_2m_temperature_since_previous_post_processing', 'mean_sea_level_pressure', 'minimum_2m_temperature_since_previous_post_processing', 'sea_surface_temperature', 'skin_temperature', 'surface_pressure', '100m_u_component_of_wind', '100m_v_component_of_wind', '10m_u_component_of_neutral_wind', '10m_u_component_of_wind', '10m_v_component_of_neutral_wind', '10m_v_component_of_wind', '10m_wind_gust_since_previous_post_processing', 'instantaneous_10m_wind_gust', 'mean_boundary_layer_dissipation', 'mean_convective_precipitation_rate', 'mean_convective_snowfall_rate', 'mean_eastward_gravity_wave_surface_stress', 'mean_eastward_turbulent_surface_stress', 'mean_evaporation_rate', 'mean_gravity_wave_dissipation', 'mean_large_scale_precipitation_fraction', 'mean_large_scale_precipitation_rate', 'mean_large_scale_snowfall_rate', 'mean_northward_gravity_wave_surface_stress', 'mean_northward_turbulent_surface_stress', 'mean_potential_evaporation_rate', 'mean_runoff_rate', 'mean_snow_evaporation_rate', 'mean_snowfall_rate', 'mean_snowmelt_rate', 'mean_sub_surface_runoff_rate', 'mean_surface_direct_short_wave_radiation_flux', 'mean_surface_direct_short_wave_radiation_flux_clear_sky', 'mean_surface_downward_long_wave_radiation_flux', 'mean_surface_downward_long_wave_radiation_flux_clear_sky', 'mean_surface_downward_short_wave_radiation_flux', 'mean_surface_downward_short_wave_radiation_flux_clear_sky', 'mean_surface_downward_uv_radiation_flux', 'mean_surface_latent_heat_flux', 'mean_surface_net_long_wave_radiation_flux', 'mean_surface_net_long_wave_radiation_flux_clear_sky', 'mean_surface_net_short_wave_radiation_flux', 'mean_surface_net_short_wave_radiation_flux_clear_sky', 'mean_surface_runoff_rate', 'mean_surface_sensible_heat_flux', 'mean_top_downward_short_wave_radiation_flux', 'mean_top_net_long_wave_radiation_flux', 'mean_top_net_long_wave_radiation_flux_clear_sky', 'mean_top_net_short_wave_radiation_flux', 'mean_top_net_short_wave_radiation_flux_clear_sky', 'mean_total_precipitation_rate', 'mean_vertically_integrated_moisture_divergence', 'clear_sky_direct_solar_radiation_at_surface', 'downward_uv_radiation_at_the_surface', 'forecast_logarithm_of_surface_roughness_for_heat', 'instantaneous_surface_sensible_heat_flux', 'near_ir_albedo_for_diffuse_radiation', 'near_ir_albedo_for_direct_radiation', 'surface_latent_heat_flux', 'surface_net_solar_radiation', 'surface_net_solar_radiation_clear_sky', 'surface_net_thermal_radiation', 'surface_net_thermal_radiation_clear_sky', 'surface_sensible_heat_flux', 'surface_solar_radiation_downward_clear_sky', 'surface_solar_radiation_downwards', 'surface_thermal_radiation_downward_clear_sky', 'surface_thermal_radiation_downwards', 'toa_incident_solar_radiation', 'top_net_solar_radiation', 'top_net_solar_radiation_clear_sky', 'top_net_thermal_radiation', 'top_net_thermal_radiation_clear_sky', 'total_sky_direct_solar_radiation_at_surface', 'uv_visible_albedo_for_diffuse_radiation', 'uv_visible_albedo_for_direct_radiation', 'cloud_base_height', 'high_cloud_cover', 'low_cloud_cover', 'medium_cloud_cover', 'total_cloud_cover', 'total_column_cloud_ice_water', 'total_column_cloud_liquid_water', 'vertical_integral_of_divergence_of_cloud_frozen_water_flux', 'vertical_integral_of_divergence_of_cloud_liquid_water_flux', 'vertical_integral_of_eastward_cloud_frozen_water_flux', 'vertical_integral_of_eastward_cloud_liquid_water_flux', 'vertical_integral_of_northward_cloud_frozen_water_flux', 'vertical_integral_of_northward_cloud_liquid_water_flux', 'lake_bottom_temperature', 'lake_cover', 'lake_depth', 'lake_ice_depth', 'lake_ice_temperature', 'lake_mix_layer_depth', 'lake_mix_layer_temperature', 'lake_shape_factor', 'lake_total_layer_temperature', 'evaporation', 'potential_evaporation', 'runoff', 'sub_surface_runoff', 'surface_runoff', 'convective_precipitation', 'convective_rain_rate', 'instantaneous_large_scale_surface_precipitation_fraction', 'large_scale_rain_rate', 'large_scale_precipitation', 'large_scale_precipitation_fraction', 'maximum_total_precipitation_rate_since_previous_post_processing', 'minimum_total_precipitation_rate_since_previous_post_processing', 'precipitation_type', 'total_column_rain_water', 'total_precipitation', 'convective_snowfall', 'convective_snowfall_rate_water_equivalent', 'large_scale_snowfall_rate_water_equivalent', 'large_scale_snowfall', 'snow_albedo', 'snow_density', 'snow_depth', 'snow_evaporation', 'snowfall', 'snowmelt', 'temperature_of_snow_layer', 'total_column_snow_water', 'soil_temperature_level_1', 'soil_temperature_level_2', 'soil_temperature_level_3', 'soil_temperature_level_4', 'soil_type', 'volumetric_soil_water_layer_1', 'volumetric_soil_water_layer_2', 'volumetric_soil_water_layer_3', 'volumetric_soil_water_layer_4', 'vertical_integral_of_divergence_of_cloud_frozen_water_flux', 'vertical_integral_of_divergence_of_cloud_liquid_water_flux', 'vertical_integral_of_divergence_of_geopotential_flux', 'vertical_integral_of_divergence_of_kinetic_energy_flux', 'vertical_integral_of_divergence_of_mass_flux', 'vertical_integral_of_divergence_of_moisture_flux', 'vertical_integral_of_divergence_of_ozone_flux', 'vertical_integral_of_divergence_of_thermal_energy_flux', 'vertical_integral_of_divergence_of_total_energy_flux', 'vertical_integral_of_eastward_cloud_frozen_water_flux', 'vertical_integral_of_eastward_cloud_liquid_water_flux', 'vertical_integral_of_eastward_geopotential_flux', 'vertical_integral_of_eastward_heat_flux', 'vertical_integral_of_eastward_kinetic_energy_flux', 'vertical_integral_of_eastward_mass_flux', 'vertical_integral_of_eastward_ozone_flux', 'vertical_integral_of_eastward_total_energy_flux', 'vertical_integral_of_eastward_water_vapour_flux', 'vertical_integral_of_energy_conversion', 'vertical_integral_of_kinetic_energy', 'vertical_integral_of_mass_of_atmosphere', 'vertical_integral_of_mass_tendency', 'vertical_integral_of_northward_cloud_frozen_water_flux', 'vertical_integral_of_northward_cloud_liquid_water_flux', 'vertical_integral_of_northward_geopotential_flux', 'vertical_integral_of_northward_heat_flux', 'vertical_integral_of_northward_kinetic_energy_flux', 'vertical_integral_of_northward_mass_flux', 'vertical_integral_of_northward_ozone_flux', 'vertical_integral_of_northward_total_energy_flux', 'vertical_integral_of_northward_water_vapour_flux', 'vertical_integral_of_potential_and_internal_energy', 'vertical_integral_of_potential_internal_and_latent_energy', 'vertical_integral_of_temperature', 'vertical_integral_of_thermal_energy', 'vertical_integral_of_total_energy', 'vertically_integrated_moisture_divergence', 'high_vegetation_cover', 'leaf_area_index_high_vegetation', 'leaf_area_index_low_vegetation', 'low_vegetation_cover', 'type_of_high_vegetation', 'type_of_low_vegetation', 'air_density_over_the_oceans', 'coefficient_of_drag_with_waves', 'free_convective_velocity_over_the_oceans', 'maximum_individual_wave_height', 'mean_direction_of_total_swell', 'mean_direction_of_wind_waves', 'mean_period_of_total_swell', 'mean_period_of_wind_waves', 'mean_square_slope_of_waves', 'mean_wave_direction', 'mean_wave_direction_of_first_swell_partition', 'mean_wave_direction_of_second_swell_partition', 'mean_wave_direction_of_third_swell_partition', 'mean_wave_period', 'mean_wave_period_based_on_first_moment', 'mean_wave_period_based_on_first_moment_for_swell', 'mean_wave_period_based_on_first_moment_for_wind_waves', 'mean_wave_period_based_on_second_moment_for_swell', 'mean_wave_period_based_on_second_moment_for_wind_waves', 'mean_wave_period_of_first_swell_partition', 'mean_wave_period_of_second_swell_partition', 'mean_wave_period_of_third_swell_partition', 'mean_zero_crossing_wave_period', 'model_bathymetry', 'normalized_energy_flux_into_ocean', 'normalized_energy_flux_into_waves', 'normalized_stress_into_ocean', 'ocean_surface_stress_equivalent_10m_neutral_wind_direction', 'ocean_surface_stress_equivalent_10m_neutral_wind_speed', 'peak_wave_period', 'period_corresponding_to_maximum_individual_wave_height', 'significant_height_of_combined_wind_waves_and_swell', 'significant_height_of_total_swell', 'significant_height_of_wind_waves', 'significant_wave_height_of_first_swell_partition', 'significant_wave_height_of_second_swell_partition', 'significant_wave_height_of_third_swell_partition', 'wave_spectral_directional_width', 'wave_spectral_directional_width_for_swell', 'wave_spectral_directional_width_for_wind_waves', 'wave_spectral_kurtosis', 'wave_spectral_peakedness', 'wave_spectral_skewness', 'angle_of_sub_gridscale_orography', 'anisotropy_of_sub_gridscale_orography', 'benjamin_feir_index', 'boundary_layer_dissipation', 'boundary_layer_height', 'charnock', 'convective_available_potential_energy', 'convective_inhibition', 'duct_base_height', 'eastward_gravity_wave_surface_stress', 'eastward_turbulent_surface_stress', 'forecast_albedo', 'forecast_surface_roughness', 'friction_velocity', 'geopotential', 'gravity_wave_dissipation', 'instantaneous_eastward_turbulent_surface_stress', 'instantaneous_moisture_flux', 'instantaneous_northward_turbulent_surface_stress', 'k_index', 'land_sea_mask', 'mean_vertical_gradient_of_refractivity_inside_trapping_layer', 'minimum_vertical_gradient_of_refractivity_inside_trapping_layer', 'northward_gravity_wave_surface_stress', 'northward_turbulent_surface_stress', 'sea_ice_cover', 'skin_reservoir_content', 'slope_of_sub_gridscale_orography', 'standard_deviation_of_filtered_subgrid_orography', 'standard_deviation_of_orography', 'total_column_ozone', 'total_column_supercooled_liquid_water', 'total_column_water', 'total_column_water_vapour', 'total_totals_index', 'trapping_layer_base_height', 'trapping_layer_top_height', 'u_component_stokes_drift', 'v_component_stokes_drift', 'zero_degree_level']
        assert variable in variable_valid_values

        time_zone_valid_values = ['utc-12:00', 'utc-11:00', 'utc-10:00', 'utc-09:00', 'utc-08:00', 'utc-07:00', 'utc-06:00', 'utc-05:00', 'utc-04:00', 'utc-03:00', 'utc-02:00', 'utc-01:00', 'utc+00:00', 'utc+01:00', 'utc+02:00', 'utc+03:00', 'utc+04:00', 'utc+05:00', 'utc+06:00', 'utc+07:00', 'utc+08:00', 'utc+09:00', 'utc+10:00', 'utc+11:00', 'utc+12:00', 'utc+13:00', 'utc+14:00']
        assert time_zone in time_zone_valid_values

        frequency_valid_values = ['1_hourly', '3_hourly', '6_hourly']
        assert frequency in frequency_valid_values

        product_type_valid_values = ['reanalysis', 'ensemble_members', 'ensemble_mean']
        assert product_type in product_type_valid_values

        daily_statistic_valid_values = ['daily_mean', 'daily_minimum', 'daily_maximum', 'daily_sum']
        assert daily_statistic in daily_statistic_valid_values

        return download_data(day=day, year=year, month=month, variable=variable, time_zone=time_zone, area_group=area_group, frequency=frequency, product_type=product_type, daily_statistic=daily_statistic)

class Collection_seasonal_original_single_levels(Collection):

    @Collection.wrapper
    def download(cls, system: str, day: OneOrMore[str], originating_centre: str, year: OneOrMore[str], leadtime_hour: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, system: str, day: OneOrMore[str], originating_centre: str, year: OneOrMore[str], leadtime_hour: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        system_valid_values = ['1', '2', '3', '4', '5', '6', '7', '8', '12', '13', '14', '15', '21', '35', '51', '600', '601', '602', '603']
        assert system in system_valid_values

        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        originating_centre_valid_values = ['ecmwf', 'ukmo', 'meteo_france', 'dwd', 'cmcc', 'ncep', 'jma', 'eccc']
        assert originating_centre in originating_centre_valid_values

        year_valid_values = ['1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        leadtime_hour_valid_values = ['0', '6', '12', '18', '24', '30', '36', '42', '48', '54', '60', '66', '72', '78', '84', '90', '96', '102', '108', '114', '120', '126', '132', '138', '144', '150', '156', '162', '168', '174', '180', '186', '192', '198', '204', '210', '216', '222', '228', '234', '240', '246', '252', '258', '264', '270', '276', '282', '288', '294', '300', '306', '312', '318', '324', '330', '336', '342', '348', '354', '360', '366', '372', '378', '384', '390', '396', '402', '408', '414', '420', '426', '432', '438', '444', '450', '456', '462', '468', '474', '480', '486', '492', '498', '504', '510', '516', '522', '528', '534', '540', '546', '552', '558', '564', '570', '576', '582', '588', '594', '600', '606', '612', '618', '624', '630', '636', '642', '648', '654', '660', '666', '672', '678', '684', '690', '696', '702', '708', '714', '720', '726', '732', '738', '744', '750', '756', '762', '768', '774', '780', '786', '792', '798', '804', '810', '816', '822', '828', '834', '840', '846', '852', '858', '864', '870', '876', '882', '888', '894', '900', '906', '912', '918', '924', '930', '936', '942', '948', '954', '960', '966', '972', '978', '984', '990', '996', '1002', '1008', '1014', '1020', '1026', '1032', '1038', '1044', '1050', '1056', '1062', '1068', '1074', '1080', '1086', '1092', '1098', '1104', '1110', '1116', '1122', '1128', '1134', '1140', '1146', '1152', '1158', '1164', '1170', '1176', '1182', '1188', '1194', '1200', '1206', '1212', '1218', '1224', '1230', '1236', '1242', '1248', '1254', '1260', '1266', '1272', '1278', '1284', '1290', '1296', '1302', '1308', '1314', '1320', '1326', '1332', '1338', '1344', '1350', '1356', '1362', '1368', '1374', '1380', '1386', '1392', '1398', '1404', '1410', '1416', '1422', '1428', '1434', '1440', '1446', '1452', '1458', '1464', '1470', '1476', '1482', '1488', '1494', '1500', '1506', '1512', '1518', '1524', '1530', '1536', '1542', '1548', '1554', '1560', '1566', '1572', '1578', '1584', '1590', '1596', '1602', '1608', '1614', '1620', '1626', '1632', '1638', '1644', '1650', '1656', '1662', '1668', '1674', '1680', '1686', '1692', '1698', '1704', '1710', '1716', '1722', '1728', '1734', '1740', '1746', '1752', '1758', '1764', '1770', '1776', '1782', '1788', '1794', '1800', '1806', '1812', '1818', '1824', '1830', '1836', '1842', '1848', '1854', '1860', '1866', '1872', '1878', '1884', '1890', '1896', '1902', '1908', '1914', '1920', '1926', '1932', '1938', '1944', '1950', '1956', '1962', '1968', '1974', '1980', '1986', '1992', '1998', '2004', '2010', '2016', '2022', '2028', '2034', '2040', '2046', '2052', '2058', '2064', '2070', '2076', '2082', '2088', '2094', '2100', '2106', '2112', '2118', '2124', '2130', '2136', '2142', '2148', '2154', '2160', '2166', '2172', '2178', '2184', '2190', '2196', '2202', '2208', '2214', '2220', '2226', '2232', '2238', '2244', '2250', '2256', '2262', '2268', '2274', '2280', '2286', '2292', '2298', '2304', '2310', '2316', '2322', '2328', '2334', '2340', '2346', '2352', '2358', '2364', '2370', '2376', '2382', '2388', '2394', '2400', '2406', '2412', '2418', '2424', '2430', '2436', '2442', '2448', '2454', '2460', '2466', '2472', '2478', '2484', '2490', '2496', '2502', '2508', '2514', '2520', '2526', '2532', '2538', '2544', '2550', '2556', '2562', '2568', '2574', '2580', '2586', '2592', '2598', '2604', '2610', '2616', '2622', '2628', '2634', '2640', '2646', '2652', '2658', '2664', '2670', '2676', '2682', '2688', '2694', '2700', '2706', '2712', '2718', '2724', '2730', '2736', '2742', '2748', '2754', '2760', '2766', '2772', '2778', '2784', '2790', '2796', '2802', '2808', '2814', '2820', '2826', '2832', '2838', '2844', '2850', '2856', '2862', '2868', '2874', '2880', '2886', '2892', '2898', '2904', '2910', '2916', '2922', '2928', '2934', '2940', '2946', '2952', '2958', '2964', '2970', '2976', '2982', '2988', '2994', '3000', '3006', '3012', '3018', '3024', '3030', '3036', '3042', '3048', '3054', '3060', '3066', '3072', '3078', '3084', '3090', '3096', '3102', '3108', '3114', '3120', '3126', '3132', '3138', '3144', '3150', '3156', '3162', '3168', '3174', '3180', '3186', '3192', '3198', '3204', '3210', '3216', '3222', '3228', '3234', '3240', '3246', '3252', '3258', '3264', '3270', '3276', '3282', '3288', '3294', '3300', '3306', '3312', '3318', '3324', '3330', '3336', '3342', '3348', '3354', '3360', '3366', '3372', '3378', '3384', '3390', '3396', '3402', '3408', '3414', '3420', '3426', '3432', '3438', '3444', '3450', '3456', '3462', '3468', '3474', '3480', '3486', '3492', '3498', '3504', '3510', '3516', '3522', '3528', '3534', '3540', '3546', '3552', '3558', '3564', '3570', '3576', '3582', '3588', '3594', '3600', '3606', '3612', '3618', '3624', '3630', '3636', '3642', '3648', '3654', '3660', '3666', '3672', '3678', '3684', '3690', '3696', '3702', '3708', '3714', '3720', '3726', '3732', '3738', '3744', '3750', '3756', '3762', '3768', '3774', '3780', '3786', '3792', '3798', '3804', '3810', '3816', '3822', '3828', '3834', '3840', '3846', '3852', '3858', '3864', '3870', '3876', '3882', '3888', '3894', '3900', '3906', '3912', '3918', '3924', '3930', '3936', '3942', '3948', '3954', '3960', '3966', '3972', '3978', '3984', '3990', '3996', '4002', '4008', '4014', '4020', '4026', '4032', '4038', '4044', '4050', '4056', '4062', '4068', '4074', '4080', '4086', '4092', '4098', '4104', '4110', '4116', '4122', '4128', '4134', '4140', '4146', '4152', '4158', '4164', '4170', '4176', '4182', '4188', '4194', '4200', '4206', '4212', '4218', '4224', '4230', '4236', '4242', '4248', '4254', '4260', '4266', '4272', '4278', '4284', '4290', '4296', '4302', '4308', '4314', '4320', '4326', '4332', '4338', '4344', '4350', '4356', '4362', '4368', '4374', '4380', '4386', '4392', '4398', '4404', '4410', '4416', '4422', '4428', '4434', '4440', '4446', '4452', '4458', '4464', '4470', '4476', '4482', '4488', '4494', '4500', '4506', '4512', '4518', '4524', '4530', '4536', '4542', '4548', '4554', '4560', '4566', '4572', '4578', '4584', '4590', '4596', '4602', '4608', '4614', '4620', '4626', '4632', '4638', '4644', '4650', '4656', '4662', '4668', '4674', '4680', '4686', '4692', '4698', '4704', '4710', '4716', '4722', '4728', '4734', '4740', '4746', '4752', '4758', '4764', '4770', '4776', '4782', '4788', '4794', '4800', '4806', '4812', '4818', '4824', '4830', '4836', '4842', '4848', '4854', '4860', '4866', '4872', '4878', '4884', '4890', '4896', '4902', '4908', '4914', '4920', '4926', '4932', '4938', '4944', '4950', '4956', '4962', '4968', '4974', '4980', '4986', '4992', '4998', '5004', '5010', '5016', '5022', '5028', '5034', '5040', '5046', '5052', '5058', '5064', '5070', '5076', '5082', '5088', '5094', '5100', '5106', '5112', '5118', '5124', '5130', '5136', '5142', '5148', '5154', '5160']
        assert leadtime_hour in leadtime_hour_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['10m_u_component_of_wind', '10m_v_component_of_wind', '10m_wind_gust_since_previous_post_processing', '2m_dewpoint_temperature', '2m_temperature', 'eastward_turbulent_surface_stress', 'evaporation', 'land_sea_mask', 'maximum_2m_temperature_in_the_last_24_hours', 'mean_sea_level_pressure', 'minimum_2m_temperature_in_the_last_24_hours', 'northward_turbulent_surface_stress', 'orography', 'runoff', 'sea_surface_temperature', 'sea_ice_cover', 'snow_density', 'snow_depth', 'snowfall', 'soil_temperature_level_1', 'sub_surface_runoff', 'surface_latent_heat_flux', 'surface_net_solar_radiation', 'surface_net_thermal_radiation', 'surface_runoff', 'surface_sensible_heat_flux', 'surface_solar_radiation_downwards', 'surface_thermal_radiation_downwards', 'toa_incident_solar_radiation', 'top_net_solar_radiation', 'top_net_thermal_radiation', 'total_cloud_cover', 'total_column_cloud_ice_water', 'total_column_cloud_liquid_water', 'total_column_water_vapour', 'total_precipitation', 'volumetric_soil_moisture']
        assert variable in variable_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(system=system, day=day, originating_centre=originating_centre, year=year, leadtime_hour=leadtime_hour, month=month, variable=variable, data_format=data_format, area_group=area_group)

class Collection_reanalysis_cerra_single_levels(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], data_type: OneOrMore[str], leadtime_hour: OneOrMore[str], soil_layer: OneOrMore[str], month: OneOrMore[str], product_type: str, variable: OneOrMore[str], level_type: str, data_format: str = 'grib'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], data_type: OneOrMore[str], leadtime_hour: OneOrMore[str], soil_layer: OneOrMore[str], month: OneOrMore[str], product_type: str, variable: OneOrMore[str], level_type: str, data_format: str = 'grib'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_valid_values = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
        assert time in time_valid_values

        year_valid_values = ['1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
        assert year in year_valid_values

        data_type_valid_values = ['ensemble_members', 'reanalysis']
        assert data_type in data_type_valid_values

        leadtime_hour_valid_values = ['1', '2', '3', '4', '5', '6', '9', '12', '15', '18', '21', '24', '27', '30']
        assert leadtime_hour in leadtime_hour_valid_values

        soil_layer_valid_values = ['top_layer']
        assert soil_layer in soil_layer_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        product_type_valid_values = ['analysis', 'forecast']
        assert product_type in product_type_valid_values

        variable_valid_values = ['10m_wind_direction', '10m_wind_gust_since_previous_post_processing', '10m_wind_speed', '2m_relative_humidity', '2m_temperature', 'albedo', 'evaporation', 'high_cloud_cover', 'land_sea_mask', 'liquid_volumetric_soil_moisture', 'low_cloud_cover', 'maximum_2m_temperature_since_previous_post_processing', 'mean_sea_level_pressure', 'medium_cloud_cover', 'minimum_2m_temperature_since_previous_post_processing', 'momentum_flux_at_the_surface_u_component', 'momentum_flux_at_the_surface_v_component', 'orography', 'skin_temperature', 'snow_density', 'snow_depth', 'snow_depth_water_equivalent', 'snow_fall_water_equivalent', 'soil_temperature', 'surface_latent_heat_flux', 'surface_net_solar_radiation', 'surface_net_solar_radiation_clear_sky', 'surface_net_thermal_radiation', 'surface_net_thermal_radiation_clear_sky', 'surface_pressure', 'surface_roughness', 'surface_sensible_heat_flux', 'surface_solar_radiation_downwards', 'surface_thermal_radiation_downwards', 'time_integrated_surface_direct_short_wave_radiation_flux', 'total_cloud_cover', 'total_column_integrated_water_vapour', 'total_precipitation', 'volumetric_soil_moisture']
        assert variable in variable_valid_values

        level_type_valid_values = ['surface_or_atmosphere', 'soil']
        assert level_type in level_type_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(day=day, time=time, year=year, data_type=data_type, leadtime_hour=leadtime_hour, soil_layer=soil_layer, month=month, product_type=product_type, variable=variable, level_type=level_type, data_format=data_format)

class Collection_satellite_precipitation_microwave(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time_aggregation: str, year: OneOrMore[str], month: OneOrMore[str], version: OneOrMore[str] = 'v1.0', variable: str = 'all'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time_aggregation: str, year: OneOrMore[str], month: OneOrMore[str], version: OneOrMore[str] = 'v1.0', variable: str = 'all'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_aggregation_valid_values = ['daily', 'monthly']
        assert time_aggregation in time_aggregation_valid_values

        year_valid_values = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        version_valid_values = ['v1_0']
        assert version in version_valid_values

        variable_valid_values = ['all']
        assert variable in variable_valid_values

        return download_data(day=day, time_aggregation=time_aggregation, year=year, month=month, version=version, variable=variable)

class Collection_sis_ocean_wave_indicators(Collection):

    @Collection.wrapper
    def download(cls, statistic: OneOrMore[str], period: OneOrMore[str], variable: OneOrMore[str], experiment: str): UNREACHABLE()
    
    @classmethod
    def __download__(cls, statistic: OneOrMore[str], period: OneOrMore[str], variable: OneOrMore[str], experiment: str):
        statistic_valid_values = ['90th_percentile', '90th_100th_percentile_average', '95th_percentile', '99th_percentile', '100_year_return_period']
        assert statistic in statistic_valid_values

        period_valid_values = ['1976_2005', '2001_2017', '2041_2070', '2071_2100']
        assert period in period_valid_values

        variable_valid_values = ['peak_wave_period', 'significant_wave_height']
        assert variable in variable_valid_values

        experiment_valid_values = ['historical', 'era5_reanalysis', 'rcp4_5', 'rcp8_5']
        assert experiment in experiment_valid_values

        return download_data(statistic=statistic, period=period, variable=variable, experiment=experiment)

class Collection_sis_european_wind_storm_synthetic_events(Collection):

    @Collection.wrapper
    def download(cls, version_id: OneOrMore[str], year: OneOrMore[str], variable: OneOrMore[str], month: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, version_id: OneOrMore[str], year: OneOrMore[str], variable: OneOrMore[str], month: OneOrMore[str]):
        version_id_valid_values = ['synthetic_set_1_2', 'synthetic_set_2_0', 'synthetic_set_3_0']
        assert version_id in version_id_valid_values

        year_valid_values = ['1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011']
        assert year in year_valid_values

        variable_valid_values = ['wind_speed_of_gusts']
        assert variable in variable_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '09', '10', '11', '12']
        assert month in month_valid_values

        return download_data(version_id=version_id, year=year, variable=variable, month=month)

class Collection_reanalysis_era5_single_levels_monthly_means(Collection):

    @Collection.wrapper
    def download(cls, time: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], download_format: str = 'unarchived', data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, time: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], download_format: str = 'unarchived', data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        time_valid_values = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
        assert time in time_valid_values

        year_valid_values = ['1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        product_type_valid_values = ['monthly_averaged_reanalysis', 'monthly_averaged_reanalysis_by_hour_of_day', 'monthly_averaged_ensemble_members', 'monthly_averaged_ensemble_members_by_hour_of_day']
        assert product_type in product_type_valid_values

        variable_valid_values = ['10m_u_component_of_wind', '10m_v_component_of_wind', '2m_dewpoint_temperature', '2m_temperature', 'mean_sea_level_pressure', 'mean_wave_direction', 'mean_wave_period', 'sea_surface_temperature', 'significant_height_of_combined_wind_waves_and_swell', 'surface_pressure', 'total_precipitation', '2m_dewpoint_temperature', '2m_temperature', 'ice_temperature_layer_1', 'ice_temperature_layer_2', 'ice_temperature_layer_3', 'ice_temperature_layer_4', 'mean_sea_level_pressure', 'sea_surface_temperature', 'skin_temperature', 'surface_pressure', '100m_u_component_of_wind', '100m_v_component_of_wind', '10m_u_component_of_neutral_wind', '10m_u_component_of_wind', '10m_v_component_of_neutral_wind', '10m_v_component_of_wind', '10m_wind_speed', 'instantaneous_10m_wind_gust', 'mean_boundary_layer_dissipation', 'mean_convective_precipitation_rate', 'mean_convective_snowfall_rate', 'mean_eastward_gravity_wave_surface_stress', 'mean_eastward_turbulent_surface_stress', 'mean_evaporation_rate', 'mean_gravity_wave_dissipation', 'mean_large_scale_precipitation_fraction', 'mean_large_scale_precipitation_rate', 'mean_large_scale_snowfall_rate', 'mean_northward_gravity_wave_surface_stress', 'mean_northward_turbulent_surface_stress', 'mean_potential_evaporation_rate', 'mean_runoff_rate', 'mean_snow_evaporation_rate', 'mean_snowfall_rate', 'mean_snowmelt_rate', 'mean_sub_surface_runoff_rate', 'mean_surface_direct_short_wave_radiation_flux', 'mean_surface_direct_short_wave_radiation_flux_clear_sky', 'mean_surface_downward_long_wave_radiation_flux', 'mean_surface_downward_long_wave_radiation_flux_clear_sky', 'mean_surface_downward_short_wave_radiation_flux', 'mean_surface_downward_short_wave_radiation_flux_clear_sky', 'mean_surface_downward_uv_radiation_flux', 'mean_surface_latent_heat_flux', 'mean_surface_net_long_wave_radiation_flux', 'mean_surface_net_long_wave_radiation_flux_clear_sky', 'mean_surface_net_short_wave_radiation_flux', 'mean_surface_net_short_wave_radiation_flux_clear_sky', 'mean_surface_runoff_rate', 'mean_surface_sensible_heat_flux', 'mean_top_downward_short_wave_radiation_flux', 'mean_top_net_long_wave_radiation_flux', 'mean_top_net_long_wave_radiation_flux_clear_sky', 'mean_top_net_short_wave_radiation_flux', 'mean_top_net_short_wave_radiation_flux_clear_sky', 'mean_total_precipitation_rate', 'mean_vertically_integrated_moisture_divergence', 'clear_sky_direct_solar_radiation_at_surface', 'downward_uv_radiation_at_the_surface', 'forecast_logarithm_of_surface_roughness_for_heat', 'instantaneous_surface_sensible_heat_flux', 'near_ir_albedo_for_diffuse_radiation', 'near_ir_albedo_for_direct_radiation', 'surface_latent_heat_flux', 'surface_net_solar_radiation', 'surface_net_solar_radiation_clear_sky', 'surface_net_thermal_radiation', 'surface_net_thermal_radiation_clear_sky', 'surface_sensible_heat_flux', 'surface_solar_radiation_downward_clear_sky', 'surface_solar_radiation_downwards', 'surface_thermal_radiation_downward_clear_sky', 'surface_thermal_radiation_downwards', 'toa_incident_solar_radiation', 'top_net_solar_radiation', 'top_net_solar_radiation_clear_sky', 'top_net_thermal_radiation', 'top_net_thermal_radiation_clear_sky', 'total_sky_direct_solar_radiation_at_surface', 'uv_visible_albedo_for_diffuse_radiation', 'uv_visible_albedo_for_direct_radiation', 'cloud_base_height', 'high_cloud_cover', 'low_cloud_cover', 'medium_cloud_cover', 'total_cloud_cover', 'total_column_cloud_ice_water', 'total_column_cloud_liquid_water', 'vertical_integral_of_divergence_of_cloud_frozen_water_flux', 'vertical_integral_of_divergence_of_cloud_liquid_water_flux', 'vertical_integral_of_eastward_cloud_frozen_water_flux', 'vertical_integral_of_eastward_cloud_liquid_water_flux', 'vertical_integral_of_northward_cloud_frozen_water_flux', 'vertical_integral_of_northward_cloud_liquid_water_flux', 'lake_bottom_temperature', 'lake_cover', 'lake_depth', 'lake_ice_depth', 'lake_ice_temperature', 'lake_mix_layer_depth', 'lake_mix_layer_temperature', 'lake_shape_factor', 'lake_total_layer_temperature', 'evaporation', 'potential_evaporation', 'runoff', 'sub_surface_runoff', 'surface_runoff', 'convective_precipitation', 'convective_rain_rate', 'instantaneous_large_scale_surface_precipitation_fraction', 'large_scale_rain_rate', 'large_scale_precipitation', 'large_scale_precipitation_fraction', 'precipitation_type', 'total_column_rain_water', 'total_precipitation', 'convective_snowfall', 'convective_snowfall_rate_water_equivalent', 'large_scale_snowfall_rate_water_equivalent', 'large_scale_snowfall', 'snow_albedo', 'snow_density', 'snow_depth', 'snow_evaporation', 'snowfall', 'snowmelt', 'temperature_of_snow_layer', 'total_column_snow_water', 'soil_temperature_level_1', 'soil_temperature_level_2', 'soil_temperature_level_3', 'soil_temperature_level_4', 'soil_type', 'volumetric_soil_water_layer_1', 'volumetric_soil_water_layer_2', 'volumetric_soil_water_layer_3', 'volumetric_soil_water_layer_4', 'vertical_integral_of_divergence_of_cloud_frozen_water_flux', 'vertical_integral_of_divergence_of_cloud_liquid_water_flux', 'vertical_integral_of_divergence_of_geopotential_flux', 'vertical_integral_of_divergence_of_kinetic_energy_flux', 'vertical_integral_of_divergence_of_mass_flux', 'vertical_integral_of_divergence_of_moisture_flux', 'vertical_integral_of_divergence_of_ozone_flux', 'vertical_integral_of_divergence_of_thermal_energy_flux', 'vertical_integral_of_divergence_of_total_energy_flux', 'vertical_integral_of_eastward_cloud_frozen_water_flux', 'vertical_integral_of_eastward_cloud_liquid_water_flux', 'vertical_integral_of_eastward_geopotential_flux', 'vertical_integral_of_eastward_heat_flux', 'vertical_integral_of_eastward_kinetic_energy_flux', 'vertical_integral_of_eastward_mass_flux', 'vertical_integral_of_eastward_ozone_flux', 'vertical_integral_of_eastward_total_energy_flux', 'vertical_integral_of_eastward_water_vapour_flux', 'vertical_integral_of_energy_conversion', 'vertical_integral_of_kinetic_energy', 'vertical_integral_of_mass_of_atmosphere', 'vertical_integral_of_mass_tendency', 'vertical_integral_of_northward_cloud_frozen_water_flux', 'vertical_integral_of_northward_cloud_liquid_water_flux', 'vertical_integral_of_northward_geopotential_flux', 'vertical_integral_of_northward_heat_flux', 'vertical_integral_of_northward_kinetic_energy_flux', 'vertical_integral_of_northward_mass_flux', 'vertical_integral_of_northward_ozone_flux', 'vertical_integral_of_northward_total_energy_flux', 'vertical_integral_of_northward_water_vapour_flux', 'vertical_integral_of_potential_and_internal_energy', 'vertical_integral_of_potential_internal_and_latent_energy', 'vertical_integral_of_temperature', 'vertical_integral_of_thermal_energy', 'vertical_integral_of_total_energy', 'vertically_integrated_moisture_divergence', 'high_vegetation_cover', 'leaf_area_index_high_vegetation', 'leaf_area_index_low_vegetation', 'low_vegetation_cover', 'type_of_high_vegetation', 'type_of_low_vegetation', 'air_density_over_the_oceans', 'coefficient_of_drag_with_waves', 'free_convective_velocity_over_the_oceans', 'maximum_individual_wave_height', 'mean_direction_of_total_swell', 'mean_direction_of_wind_waves', 'mean_period_of_total_swell', 'mean_period_of_wind_waves', 'mean_square_slope_of_waves', 'mean_wave_direction', 'mean_wave_direction_of_first_swell_partition', 'mean_wave_direction_of_second_swell_partition', 'mean_wave_direction_of_third_swell_partition', 'mean_wave_period', 'mean_wave_period_based_on_first_moment', 'mean_wave_period_based_on_first_moment_for_swell', 'mean_wave_period_based_on_first_moment_for_wind_waves', 'mean_wave_period_based_on_second_moment_for_swell', 'mean_wave_period_based_on_second_moment_for_wind_waves', 'mean_wave_period_of_first_swell_partition', 'mean_wave_period_of_second_swell_partition', 'mean_wave_period_of_third_swell_partition', 'mean_zero_crossing_wave_period', 'model_bathymetry', 'normalized_energy_flux_into_ocean', 'normalized_energy_flux_into_waves', 'normalized_stress_into_ocean', 'ocean_surface_stress_equivalent_10m_neutral_wind_direction', 'ocean_surface_stress_equivalent_10m_neutral_wind_speed', 'peak_wave_period', 'period_corresponding_to_maximum_individual_wave_height', 'significant_height_of_combined_wind_waves_and_swell', 'significant_height_of_total_swell', 'significant_height_of_wind_waves', 'significant_wave_height_of_first_swell_partition', 'significant_wave_height_of_second_swell_partition', 'significant_wave_height_of_third_swell_partition', 'wave_spectral_directional_width', 'wave_spectral_directional_width_for_swell', 'wave_spectral_directional_width_for_wind_waves', 'wave_spectral_kurtosis', 'wave_spectral_peakedness', 'wave_spectral_skewness', 'angle_of_sub_gridscale_orography', 'anisotropy_of_sub_gridscale_orography', 'benjamin_feir_index', 'boundary_layer_dissipation', 'boundary_layer_height', 'charnock', 'convective_available_potential_energy', 'convective_inhibition', 'duct_base_height', 'eastward_gravity_wave_surface_stress', 'eastward_turbulent_surface_stress', 'forecast_albedo', 'forecast_surface_roughness', 'friction_velocity', 'geopotential', 'gravity_wave_dissipation', 'instantaneous_eastward_turbulent_surface_stress', 'instantaneous_moisture_flux', 'instantaneous_northward_turbulent_surface_stress', 'k_index', 'land_sea_mask', 'magnitude_of_turbulent_surface_stress', 'mean_magnitude_of_turbulent_surface_stress', 'mean_vertical_gradient_of_refractivity_inside_trapping_layer', 'minimum_vertical_gradient_of_refractivity_inside_trapping_layer', 'northward_gravity_wave_surface_stress', 'northward_turbulent_surface_stress', 'sea_ice_cover', 'skin_reservoir_content', 'slope_of_sub_gridscale_orography', 'standard_deviation_of_filtered_subgrid_orography', 'standard_deviation_of_orography', 'total_column_ozone', 'total_column_supercooled_liquid_water', 'total_column_water', 'total_column_water_vapour', 'total_totals_index', 'trapping_layer_base_height', 'trapping_layer_top_height', 'u_component_stokes_drift', 'v_component_stokes_drift', 'zero_degree_level']
        assert variable in variable_valid_values

        download_format_valid_values = ['unarchived', 'zip']
        assert download_format in download_format_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(time=time, year=year, month=month, product_type=product_type, variable=variable, download_format=download_format, data_format=data_format, area_group=area_group)

class Collection_reanalysis_cerra_height_levels(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time: OneOrMore[str], data_type: OneOrMore[str], year: OneOrMore[str], leadtime_hour: OneOrMore[str], height_level: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], data_format: str = 'grib'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time: OneOrMore[str], data_type: OneOrMore[str], year: OneOrMore[str], leadtime_hour: OneOrMore[str], height_level: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], data_format: str = 'grib'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_valid_values = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
        assert time in time_valid_values

        data_type_valid_values = ['ensemble_members', 'reanalysis']
        assert data_type in data_type_valid_values

        year_valid_values = ['1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
        assert year in year_valid_values

        leadtime_hour_valid_values = ['1', '2', '3', '4', '5', '6', '9', '12', '15', '18', '21', '24', '27', '30']
        assert leadtime_hour in leadtime_hour_valid_values

        height_level_valid_values = ['15_m', '30_m', '50_m', '75_m', '100_m', '150_m', '200_m', '250_m', '300_m', '400_m', '500_m']
        assert height_level in height_level_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        product_type_valid_values = ['analysis', 'forecast']
        assert product_type in product_type_valid_values

        variable_valid_values = ['pressure', 'relative_humidity', 'specific_cloud_ice_water_content', 'specific_cloud_liquid_water_content', 'specific_rain_water_content', 'specific_snow_water_content', 'temperature', 'turbulent_kinetic_energy', 'wind_direction', 'wind_speed']
        assert variable in variable_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(day=day, time=time, data_type=data_type, year=year, leadtime_hour=leadtime_hour, height_level=height_level, month=month, product_type=product_type, variable=variable, data_format=data_format)

class Collection_sis_agroproductivity_indicators(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], year: str, product_family: OneOrMore[str], harvest_year: str, month: OneOrMore[str], variable: OneOrMore[str], crop_type: OneOrMore[str], growing_season: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], year: str, product_family: OneOrMore[str], harvest_year: str, month: OneOrMore[str], variable: OneOrMore[str], crop_type: OneOrMore[str], growing_season: OneOrMore[str]):
        day_valid_values = ['01', '10', '11', '20', '21', '28', '29', '30', '31']
        assert day in day_valid_values

        year_valid_values = ['1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        product_family_valid_values = ['crop_productivity_indicators', 'evapotranspiration_indicators']
        assert product_family in product_family_valid_values

        harvest_year_valid_values = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert harvest_year in harvest_year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['actual_evaporation', 'potential_evaporation', 'crop_development_stage', 'total_above_ground_production', 'total_weight_storage_organs']
        assert variable in variable_valid_values

        crop_type_valid_values = ['maize', 'soybean', 'spring_wheat', 'winter_wheat', 'wet_rice']
        assert crop_type in crop_type_valid_values

        growing_season_valid_values = ['1st_season_per_campaign', '2nd_season_per_campaign']
        assert growing_season in growing_season_valid_values

        return download_data(day=day, year=year, product_family=product_family, harvest_year=harvest_year, month=month, variable=variable, crop_type=crop_type, growing_season=growing_season)

class Collection_derived_reanalysis_energy_moisture_budget(Collection):

    @Collection.wrapper
    def download(cls, year: OneOrMore[str], variable: str, month: OneOrMore[str], area_group: Optional[Union[LabelType, GeographicExtentMapType]] = None): UNREACHABLE()
    
    @classmethod
    def __download__(cls, year: OneOrMore[str], variable: str, month: OneOrMore[str], area_group: Optional[Union[LabelType, GeographicExtentMapType]] = None):
        year_valid_values = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
        assert year in year_valid_values

        variable_valid_values = ['divergence_of_vertical_integral_of_latent_heat_flux', 'divergence_of_vertical_integral_of_total_energy_flux', 'divergence_of_vertical_integral_of_water_vapour_flux', 'vertical_integral_of_eastward_latent_heat_flux', 'vertical_integral_of_eastward_total_energy_flux', 'vertical_integral_of_eastward_water_vapour_flux', 'vertical_integral_of_northward_latent_heat_flux', 'vertical_integral_of_northward_total_energy_flux', 'vertical_integral_of_northward_water_vapour_flux', 'tendency_of_vertical_integral_of_latent_heat', 'tendency_of_vertical_integral_of_water_vapour', 'tendency_of_vertical_integral_of_total_energy']
        assert variable in variable_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        return download_data(year=year, variable=variable, month=month, area_group=area_group)

class Collection_sis_hydrology_variables_derived_projections(Collection):

    @Collection.wrapper
    def download(cls, period: OneOrMore[str], time_aggregation: str, hydrological_model: OneOrMore[str], ensemble_member: OneOrMore[str], rcm: str, gcm: str, product_type: str, variable: OneOrMore[str], variable_type: str, experiment: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, period: OneOrMore[str], time_aggregation: str, hydrological_model: OneOrMore[str], ensemble_member: OneOrMore[str], rcm: str, gcm: str, product_type: str, variable: OneOrMore[str], variable_type: str, experiment: OneOrMore[str]):
        period_valid_values = ['1971_2000', '2011_2040', '2041_2070', '2071_2100', '1971_1980', '1981_1990', '1991_2000', '2001_2005', '2006_2010', '2011_2020', '2021_2030', '2031_2040', '2041_2050', '2051_2060', '2061_2070', '2071_2080', '2081_2090', '2091_2100', '1_5_c', '2_0_c', '3_0_c', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057', '2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065', '2066', '2067', '2068', '2069', '2070', '2071', '2072', '2073', '2074', '2075', '2076', '2077', '2078', '2079', '2080', '2081', '2082', '2083', '2084', '2085', '2086', '2087', '2088', '2089', '2090', '2091', '2092', '2093', '2094', '2095', '2096', '2097', '2098', '2099', '2100']
        assert period in period_valid_values

        time_aggregation_valid_values = ['daily', 'monthly_mean', 'annual_mean']
        assert time_aggregation in time_aggregation_valid_values

        hydrological_model_valid_values = ['e_hypecatch_m00', 'e_hypecatch_m01', 'e_hypecatch_m02', 'e_hypecatch_m03', 'e_hypecatch_m04', 'e_hypecatch_m05', 'e_hypecatch_m06', 'e_hypecatch_m07', 'e_hypegrid', 'vic_wur']
        assert hydrological_model in hydrological_model_valid_values

        ensemble_member_valid_values = ['r1i1p1', 'r12i1p1', 'r2i1p1']
        assert ensemble_member in ensemble_member_valid_values

        rcm_valid_values = ['cclm4_8_17', 'racmo22e', 'csc_remo2009', 'rca4']
        assert rcm in rcm_valid_values

        gcm_valid_values = ['hadgem2_es', 'mpi_esm_lr', 'ec_earth']
        assert gcm in gcm_valid_values

        product_type_valid_values = ['climate_impact_indicators', 'essential_climate_variables']
        assert product_type in product_type_valid_values

        variable_valid_values = ['river_discharge', 'mean_runoff', 'flood_recurrence_2_years_return_period', 'flood_recurrence_5_years_return_period', 'flood_recurrence_10_years_return_period', 'flood_recurrence_50_years_return_period', 'maximum_river_discharge', 'minimum_river_discharge', 'mean_soil_moisture', 'wetness_actual', 'wetness_potential', 'water_temperature_in_catchments', 'water_temperature_in_local_streams', 'aridity_potential', 'aridity_actual', 'total_nitrogen_concentration_in_catchments', 'total_nitrogen_load_in_catchments', 'total_nitrogen_concentration_in_local_streams', 'total_phosphorus_concentration_in_catchments', 'total_phosphorus_load_in_catchments', 'total_phosphorus_concentration_in_local_streams']
        assert variable in variable_valid_values

        variable_type_valid_values = ['relative_change_from_reference_period', 'absolute_change_from_reference_period', 'absolute_values']
        assert variable_type in variable_type_valid_values

        experiment_valid_values = ['historical', 'rcp_2_6', 'rcp_4_5', 'rcp_8_5', 'degree_scenario']
        assert experiment in experiment_valid_values

        return download_data(period=period, time_aggregation=time_aggregation, hydrological_model=hydrological_model, ensemble_member=ensemble_member, rcm=rcm, gcm=gcm, product_type=product_type, variable=variable, variable_type=variable_type, experiment=experiment)

class Collection_reanalysis_carra_model_levels(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], leadtime_hour: OneOrMore[str], month: OneOrMore[str], product_type: str, variable: OneOrMore[str], model_level: OneOrMore[str], domain: str, data_format: str = 'grib'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], leadtime_hour: OneOrMore[str], month: OneOrMore[str], product_type: str, variable: OneOrMore[str], model_level: OneOrMore[str], domain: str, data_format: str = 'grib'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_valid_values = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
        assert time in time_valid_values

        year_valid_values = ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        leadtime_hour_valid_values = ['1', '2']
        assert leadtime_hour in leadtime_hour_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        product_type_valid_values = ['analysis', 'forecast']
        assert product_type in product_type_valid_values

        variable_valid_values = ['cloud_cover', 'graupel', 'specific_cloud_ice_water_content', 'specific_cloud_liquid_water_content', 'specific_cloud_rain_water_content', 'specific_cloud_snow_water_content', 'specific_humidity', 'temperature', 'turbulent_kinetic_energy', 'u_component_of_wind', 'v_component_of_wind']
        assert variable in variable_valid_values

        model_level_valid_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65']
        assert model_level in model_level_valid_values

        domain_valid_values = ['east_domain', 'west_domain']
        assert domain in domain_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(day=day, time=time, year=year, leadtime_hour=leadtime_hour, month=month, product_type=product_type, variable=variable, model_level=model_level, domain=domain, data_format=data_format)

class Collection_projections_cmip6_decadal_prototype(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], base_year: str, model: str, year: OneOrMore[str], month: OneOrMore[str], temporal_resolution: str, variable: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], base_year: str, model: str, year: OneOrMore[str], month: OneOrMore[str], temporal_resolution: str, variable: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        base_year_valid_values = ['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
        assert base_year in base_year_valid_values

        model_valid_values = ['cmcc_cm2_sr5', 'ec_earth3', 'hadgem3_gc31_mm', 'mpi_esm1_2_hr', 'mpi_esm1_2_lr']
        assert model in model_valid_values

        year_valid_values = ['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        temporal_resolution_valid_values = ['monthly', 'daily']
        assert temporal_resolution in temporal_resolution_valid_values

        variable_valid_values = ['near_surface_air_temperature', 'daily_maximum_near_surface_air_temperature', 'precipitation', 'sea_level_pressure', 'daily_minimum_near_surface_air_temperature', '500_hpa_geopotential_height']
        assert variable in variable_valid_values

        return download_data(day=day, base_year=base_year, model=model, year=year, month=month, temporal_resolution=temporal_resolution, variable=variable, area_group=area_group)

class Collection_sis_ecv_cmip5_bias_corrected(Collection):

    @Collection.wrapper
    def download(cls, model: str, period: OneOrMore[str], variable: str, experiment: str): UNREACHABLE()
    
    @classmethod
    def __download__(cls, model: str, period: OneOrMore[str], variable: str, experiment: str):
        model_valid_values = ['access1_0', 'access1_3', 'bcc_csm1_1', 'bcc_csm1_1_m', 'bnu_esm', 'cnrm_cm5', 'ec_earth', 'gfdl_cm3', 'gfdl_esm2g', 'gfdl_esm2m', 'hadgem2_cc', 'hadgem2_es', 'ipsl_cm5a_lr', 'ipsl_cm5a_mr', 'ipsl_cm5b_lr', 'mpi_esm_lr', 'mpi_esm_mr', 'noresm1_m']
        assert model in model_valid_values

        period_valid_values = ['19500101_19741231', '19500101_19801231', '19500101_19991231', '19510101_19551231', '19560101_19601231', '19591201_19691130', '19600101_19641231', '19600101_19691231', '19610101_19651231', '19641201_19691130', '19650101_19691231', '19660101_19701231', '19691201_19741130', '19691201_19791130', '19700101_19741231', '19700101_19791231', '19710101_19751231', '19741201_19791130', '19750101_19791231', '19750101_19991231', '19750101_20051231', '19760101_19801231', '19791201_19841130', '19791201_19891130', '19800101_19841231', '19800101_19891231', '19810101_19851231', '19810101_20051231', '19841201_19891130', '19850101_19891231', '19860101_19901231', '19891201_19941130', '19891201_19991130', '19900101_19941231', '19900101_19991231', '19910101_19951231', '19941201_19991130', '19950101_19991231', '19960101_20001231', '19991201_20041130', '19991201_20051130', '20000101_20041231', '20000101_20051231', '20010101_20051231', '20041201_20051130', '20050101_20051231', '20051201_20101130', '20051201_20151130', '20060101_20091231', '20060101_20101231', '20060101_20301231', '20060101_20501231', '20060101_20551231', '20100101_20191231', '20101201_20151130', '20110101_20151231', '20151201_20201130', '20151201_20251130', '20160101_20201231', '20200101_20291231', '20201201_20251130', '20210101_20251231', '20251201_20301130', '20251201_20351130', '20260101_20301231', '20300101_20391231', '20301201_20351130', '20310101_20351231', '20310101_20551231', '20351201_20401130', '20351201_20451130', '20360101_20401231', '20400101_20491231', '20401201_20451130', '20410101_20451231', '20451201_20501130', '20451201_20551130', '20460101_20501231', '20500101_20591231', '20501201_20551130', '20510101_20551231', '20510101_20951231', '20551201_20601130', '20551201_20651130', '20560101_20601231', '20560101_20801231', '20560101_21001231', '20600101_20691231', '20601201_20651130', '20610101_20651231', '20651201_20701130', '20651201_20751130', '20660101_20701231', '20700101_20791231', '20701201_20751130', '20710101_20751231', '20751201_20801130', '20751201_20851130', '20760101_20801231', '20800101_20891231', '20801201_20851130', '20810101_20851231', '20810101_20991231', '20810101_21001231', '20851201_20901130', '20851201_20951130', '20860101_20901231', '20900101_21001231', '20901201_20951130', '20910101_20951231', '20951201_20991130', '20951201_20991231', '20960101_20991231', '20960101_21001231', '20991201_20991231', '21000101_21001231']
        assert period in period_valid_values

        variable_valid_values = ['precipitation_flux', 'mean_2m_temperature', 'maximum_2m_temperature', 'minimum_2m_temperature']
        assert variable in variable_valid_values

        experiment_valid_values = ['rcp_4_5', 'rcp_8_5']
        assert experiment in experiment_valid_values

        return download_data(model=model, period=period, variable=variable, experiment=experiment)

class Collection_satellite_surface_radiation_budget(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time_aggregation: str, origin: str, climate_data_record_type: str, year: OneOrMore[str], product_family: str, sensor_on_satellite: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time_aggregation: str, origin: str, climate_data_record_type: str, year: OneOrMore[str], product_family: str, sensor_on_satellite: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_aggregation_valid_values = ['monthly_mean', 'daily_mean']
        assert time_aggregation in time_aggregation_valid_values

        origin_valid_values = ['eumetsat', 'c3s', 'esa']
        assert origin in origin_valid_values

        climate_data_record_type_valid_values = ['interim_climate_data_record', 'thematic_climate_data_record']
        assert climate_data_record_type in climate_data_record_type_valid_values

        year_valid_values = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
        assert year in year_valid_values

        product_family_valid_values = ['clara_a2', 'clara_a3', 'cci']
        assert product_family in product_family_valid_values

        sensor_on_satellite_valid_values = ['aatsr_on_envisat', 'atsr2_on_ers2', 'slstr_on_sentinel_3a', 'slstr_on_sentinel_3b', 'slstr_on_sentinel_3a_3b']
        assert sensor_on_satellite in sensor_on_satellite_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['surface_upwelling_shortwave_flux', 'surface_upwelling_longwave_flux', 'surface_downwelling_shortwave_flux', 'surface_downwelling_longwave_flux', 'surface_net_downward_shortwave_flux', 'surface_net_downward_longwave_flux', 'surface_net_downward_radiative_flux', 'all_variables']
        assert variable in variable_valid_values

        return download_data(day=day, time_aggregation=time_aggregation, origin=origin, climate_data_record_type=climate_data_record_type, year=year, product_family=product_family, sensor_on_satellite=sensor_on_satellite, month=month, variable=variable, area_group=area_group)

class Collection_satellite_sea_ice_thickness(Collection):

    @Collection.wrapper
    def download(cls, cdr_type: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], satellite: OneOrMore[str], version: str = '3_0', variable: str = 'all'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, cdr_type: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], satellite: OneOrMore[str], version: str = '3_0', variable: str = 'all'):
        cdr_type_valid_values = ['cdr', 'icdr']
        assert cdr_type in cdr_type_valid_values

        year_valid_values = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '10', '11', '12']
        assert month in month_valid_values

        satellite_valid_values = ['envisat', 'cryosat_2']
        assert satellite in satellite_valid_values

        version_valid_values = ['1_0', '2_0', '3_0']
        assert version in version_valid_values

        variable_valid_values = ['all']
        assert variable in variable_valid_values

        return download_data(cdr_type=cdr_type, year=year, month=month, satellite=satellite, version=version, variable=variable)

class Collection_sis_extreme_indices_cmip6(Collection):

    @Collection.wrapper
    def download(cls, period: OneOrMore[str], model: OneOrMore[str], ensemble_member: OneOrMore[str], temporal_aggregation: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], experiment: OneOrMore[str], version: OneOrMore[str] = '2_0'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, period: OneOrMore[str], model: OneOrMore[str], ensemble_member: OneOrMore[str], temporal_aggregation: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], experiment: OneOrMore[str], version: OneOrMore[str] = '2_0'):
        period_valid_values = ['19510101_20101230', '19510101_20101231', '19510101_20141230', '19510101_20141231', '20110101_21001230', '20110101_21001231', '20150101_21001230', '20150101_21001231', '184901_201412', '185001_201412', '185001_201612', '195101_201412', '201501_203912', '201501_210012', '201501_218012', '201501_230012', '1849_2014', '1850_2014', '1850_2016', '1951_2014', '2015_2039', '2015_2100', '2015_2180', '2015_2300']
        assert period in period_valid_values

        model_valid_values = ['access_cm2', 'access_esm1_5', 'bcc_csm2_mr', 'cnrm_cm6_1', 'cnrm_cm6_1_hr', 'cnrm_esm2_1', 'canesm5', 'ec_earth3', 'ec_earth3_veg', 'fgoals_g3', 'gfdl_cm4', 'gfdl_esm4', 'hadgem3_gc31_ll', 'hadgem3_gc31_mm', 'inm_cm4_8', 'inm_cm5_0', 'kace_1_0_g', 'kiost_esm', 'miroc_es2l', 'miroc6', 'mpi_esm1_2_hr', 'mpi_esm1_2_lr', 'mri_esm2_0', 'nesm3', 'noresm2_lm', 'noresm2_mm', 'ukesm1_0_ll']
        assert model in model_valid_values

        ensemble_member_valid_values = ['r10i1p1f1', 'r10i1p2f1', 'r11i1p1f1', 'r11i1p2f1', 'r12i1p1f1', 'r12i1p2f1', 'r13i1p1f1', 'r13i1p2f1', 'r14i1p1f1', 'r14i1p2f1', 'r15i1p1f1', 'r15i1p2f1', 'r16i1p1f1', 'r16i1p2f1', 'r17i1p1f1', 'r17i1p2f1', 'r18i1p1f1', 'r18i1p2f1', 'r19i1p1f1', 'r19i1p2f1', 'r1i1p1f1', 'r1i1p1f2', 'r1i1p1f3', 'r1i1p2f1', 'r20i1p1f1', 'r20i1p2f1', 'r21i1p1f1', 'r21i1p2f1', 'r22i1p1f1', 'r22i1p2f1', 'r23i1p1f1', 'r23i1p2f1', 'r24i1p1f1', 'r24i1p2f1', 'r25i1p1f1', 'r25i1p2f1', 'r26i1p1f1', 'r27i1p1f1', 'r28i1p1f1', 'r29i1p1f1', 'r2i1p1f1', 'r2i1p2f1', 'r30i1p1f1', 'r31i1p1f1', 'r32i1p1f1', 'r33i1p1f1', 'r34i1p1f1', 'r35i1p1f1', 'r36i1p1f1', 'r37i1p1f1', 'r38i1p1f1', 'r39i1p1f1', 'r3i1p1f1', 'r3i1p2f1', 'r40i1p1f1', 'r41i1p1f1', 'r42i1p1f1', 'r43i1p1f1', 'r44i1p1f1', 'r45i1p1f1', 'r46i1p1f1', 'r47i1p1f1', 'r48i1p1f1', 'r49i1p1f1', 'r4i1p1f1', 'r4i1p2f1', 'r50i1p1f1', 'r5i1p1f1', 'r5i1p2f1', 'r6i1p1f1', 'r6i1p2f1', 'r7i1p1f1', 'r7i1p2f1', 'r8i1p1f1', 'r8i1p2f1', 'r9i1p1f1', 'r9i1p2f1']
        assert ensemble_member in ensemble_member_valid_values

        temporal_aggregation_valid_values = ['yearly', 'monthly', 'daily']
        assert temporal_aggregation in temporal_aggregation_valid_values

        product_type_valid_values = ['base_period_1961_1990', 'base_period_1981_2010', 'base_independent', 'bias_adjusted', 'non_bias_adjusted']
        assert product_type in product_type_valid_values

        variable_valid_values = ['cold_days', 'cold_nights', 'cold_spell_duration_index', 'consecutive_dry_days', 'consecutive_wet_days', 'diurnal_temperature_range', 'extremely_wet_day_precipitation', 'frost_days', 'growing_season_length', 'heavy_precipitation_days', 'ice_days', 'maximum_1_day_precipitation', 'maximum_5_day_precipitation', 'maximum_value_of_daily_maximum_temperature', 'minimum_value_of_daily_maximum_temperature', 'maximum_value_of_daily_minimum_temperature', 'minimum_value_of_daily_minimum_temperature', 'number_of_wet_days', 'simple_daily_intensity_index', 'summer_days', 'total_wet_day_precipitation', 'tropical_nights', 'very_heavy_precipitation_days', 'very_wet_day_precipitation', 'warm_days', 'warm_nights', 'warm_spell_duration_index', 'heat_index', 'humidex', 'universal_thermal_climate_index', 'wet_bulb_temperature_index', 'wet_bulb_globe_temperature_index']
        assert variable in variable_valid_values

        experiment_valid_values = ['historical', 'ssp1_2_6', 'ssp2_4_5', 'ssp3_7_0', 'ssp5_8_5']
        assert experiment in experiment_valid_values

        version_valid_values = ['1_0', '2_0']
        assert version in version_valid_values

        return download_data(period=period, model=model, ensemble_member=ensemble_member, temporal_aggregation=temporal_aggregation, product_type=product_type, variable=variable, experiment=experiment, version=version)

class Collection_satellite_aerosol_properties(Collection):

    @Collection.wrapper
    def download(cls, orbit: OneOrMore[str], day: OneOrMore[str], time_aggregation: str, version: OneOrMore[str], year: OneOrMore[str], sensor_on_satellite: str, month: OneOrMore[str], algorithm: str, variable: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, orbit: OneOrMore[str], day: OneOrMore[str], time_aggregation: str, version: OneOrMore[str], year: OneOrMore[str], sensor_on_satellite: str, month: OneOrMore[str], algorithm: str, variable: OneOrMore[str]):
        orbit_valid_values = ['ascending', 'descending', 'ascending_and_descending']
        assert orbit in orbit_valid_values

        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_aggregation_valid_values = ['daily_average', 'monthly_average', '5_daily_composite']
        assert time_aggregation in time_aggregation_valid_values

        version_valid_values = ['deprecated (v4.32)', 'v2_30', 'v2_6', 'v2_9', 'v3_0', 'v3_11', 'v4_0', 'v4_01', 'v4_02', 'v4_1', 'v4_3', 'v4_32_latest', 'v4_33', 'deprecated (v1.11)', 'v1_00', 'v1_10', 'v1_12', 'v2_00', 'v2_10', 'v2_20', 'v2_30', 'v0_08', 'v2_01', 'v2_10', 'v2_20', 'v1_0', 'v2_1', 'v2_3', 'v4_8a', 'v7_0a', 'v1_0', 'v1_1', 'v1_2', 'v1_3', 'v1_4', 'v2_1', 'v2_2', 'v3_51', 'v3_7', 'v4_0', 'v4_1', 'v5_0', 'v5_1', 'v5_2', 'v6_0', 'v7_0', 'v7_1', 'v8', 'v9', 'v1_0', 'v1_1', 'v2_0', 'deprecated (v5.00)', 'v3_00', 'v4_00', 'v4_01s', 'deprecated (v5.00)', 'v1_0', 'v1_1', 'v1_2', 'v1_3', 'v1_4', 'v2_1', 'v2_2', 'v2_3', 'v2_6', 'v2_9', 'v3_0', 'v3_1']
        assert version in version_valid_values

        year_valid_values = ['1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
        assert year in year_valid_values

        sensor_on_satellite_valid_values = ['aatsr_on_envisat', 'atsr2_on_ers2', 'slstr_on_sentinel_3a', 'slstr_on_sentinel_3b', 'polder_on_parasol', 'meris_on_envisat', 'iasi_on_metopa', 'iasi_on_metopb', 'iasi_on_metopc', 'olci_on_sentinel_3a', 'gomos_on_envisat']
        assert sensor_on_satellite in sensor_on_satellite_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        algorithm_valid_values = ['aergom', 'adv', 'ens', 'grasp', 'imars', 'lmd', 'mapir', 'orac', 'sdv', 'swansea', 's4m', 's4o', 'ulb', 'xbaer']
        assert algorithm in algorithm_valid_values

        variable_valid_values = ['aerosol_optical_depth', 'fine_mode_aerosol_optical_depth', 'dust_aerosol_optical_depth', 'single_scattering_albedo', 'aerosol_layer_height', 'dust_aerosol_layer_height', 'aerosol_extinction_coefficient']
        assert variable in variable_valid_values

        return download_data(orbit=orbit, day=day, time_aggregation=time_aggregation, version=version, year=year, sensor_on_satellite=sensor_on_satellite, month=month, algorithm=algorithm, variable=variable)

class Collection_insitu_observations_igra_baseline_network(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], archive: OneOrMore[str], year: OneOrMore[str], format: str, month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], archive: OneOrMore[str], year: OneOrMore[str], format: str, month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        archive_valid_values = ['global_radiosonde_archive', 'harmonised_global_radiosonde_archive']
        assert archive in archive_valid_values

        year_valid_values = ['1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
        assert year in year_valid_values

        format_valid_values = ['netcdf', 'csv']
        assert format in format_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['air_temperature', 'dew_point_depression', 'frost_point_temperature', 'relative_humidity', 'water_vapour_mixing_ratio', 'eastward_wind_speed', 'northward_wind_speed', 'wind_from_direction', 'wind_speed', 'geopotential_height', 'solar_zenith_angle', 'vertical_speed_of_radiosonde']
        assert variable in variable_valid_values

        return download_data(day=day, archive=archive, year=year, format=format, month=month, variable=variable, area_group=area_group)

class Collection_satellite_ocean_colour(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], version: str, projection: str, year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], version: str, projection: str, year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str]):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        version_valid_values = ['6_0', '5_0_1', '5_0']
        assert version in version_valid_values

        projection_valid_values = ['regular_latitude_longitude_grid', 'sinusoidal_grid']
        assert projection in projection_valid_values

        year_valid_values = ['1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['mass_concentration_of_chlorophyll_a', 'remote_sensing_reflectance']
        assert variable in variable_valid_values

        return download_data(day=day, version=version, projection=projection, year=year, month=month, variable=variable)

class Collection_reanalysis_oras5(Collection):

    @Collection.wrapper
    def download(cls, vertical_resolution: str, year: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, vertical_resolution: str, year: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str]):
        vertical_resolution_valid_values = ['single_level', 'all_levels']
        assert vertical_resolution in vertical_resolution_valid_values

        year_valid_values = ['1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        product_type_valid_values = ['consolidated', 'operational']
        assert product_type in product_type_valid_values

        variable_valid_values = ['depth_of_14_c_isotherm', 'depth_of_17_c_isotherm', 'depth_of_20_c_isotherm', 'depth_of_26_c_isotherm', 'depth_of_28_c_isotherm', 'meridional_velocity', 'meridional_wind_stress', 'mixed_layer_depth_0_01', 'mixed_layer_depth_0_03', 'net_downward_heat_flux', 'net_upward_water_flux', 'ocean_heat_content_for_the_total_water_column', 'ocean_heat_content_for_the_upper_300m', 'ocean_heat_content_for_the_upper_700m', 'potential_temperature', 'rotated_meridional_velocity', 'rotated_zonal_velocity', 'salinity', 'sea_ice_concentration', 'sea_ice_meridional_velocity', 'sea_ice_thickness', 'sea_ice_zonal_velocity', 'sea_surface_height', 'sea_surface_salinity', 'sea_surface_temperature', 'zonal_velocity', 'zonal_wind_stress']
        assert variable in variable_valid_values

        return download_data(vertical_resolution=vertical_resolution, year=year, month=month, product_type=product_type, variable=variable)

class Collection_sis_european_wind_storm_indicators(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time_aggregation: OneOrMore[str], product: OneOrMore[str], year: OneOrMore[str], spatial_aggregation: OneOrMore[str], month: OneOrMore[str], variable: str = 'all'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time_aggregation: OneOrMore[str], product: OneOrMore[str], year: OneOrMore[str], spatial_aggregation: OneOrMore[str], month: OneOrMore[str], variable: str = 'all'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_aggregation_valid_values = ['annual', 'decadal']
        assert time_aggregation in time_aggregation_valid_values

        product_valid_values = ['windstorm_tracks', 'windstorm_footprints', 'summary_indicators', 'risk_indicators', 'loss_indicators']
        assert product in product_valid_values

        year_valid_values = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2005', '2006', '2007', '2008', '2009', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2020', '2021']
        assert year in year_valid_values

        spatial_aggregation_valid_values = ['austria', 'belgium', 'switzerland', 'czech_republic', 'germany', 'denmark', 'estonia', 'spain', 'finland', 'france', 'ireland', 'italy', 'lithuania', 'luxemburg', 'latvia', 'netherlands', 'norway', 'poland', 'portugal', 'sweden', 'united_kingdom', 'agriculture', 'transport', 'residential', 'other', 'industry', 'europe', 'european_nuts1_region', 'european_nuts3_region']
        assert spatial_aggregation in spatial_aggregation_valid_values

        month_valid_values = ['01', '02', '03', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['all']
        assert variable in variable_valid_values

        return download_data(day=day, time_aggregation=time_aggregation, product=product, year=year, spatial_aggregation=spatial_aggregation, month=month, variable=variable)

class Collection_satellite_earth_radiation_budget(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time_aggregation: str, version: OneOrMore[str], origin: str, climate_data_record_type: str, year: OneOrMore[str], product_family: str, sensor_on_satellite: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time_aggregation: str, version: OneOrMore[str], origin: str, climate_data_record_type: str, year: OneOrMore[str], product_family: str, sensor_on_satellite: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_aggregation_valid_values = ['daily_mean', 'monthly_mean']
        assert time_aggregation in time_aggregation_valid_values

        version_valid_values = ['1_2_reprocessed', '2_7_reprocessed']
        assert version in version_valid_values

        origin_valid_values = ['nasa', 'noaa_ncei', 'eumetsat', 'esa', 'c3s', 'rmib']
        assert origin in origin_valid_values

        climate_data_record_type_valid_values = ['interim_climate_data_record', 'thematic_climate_data_record']
        assert climate_data_record_type in climate_data_record_type_valid_values

        year_valid_values = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        product_family_valid_values = ['ceres_ebaf', 'hirs', 'clara_a3', 'cci', 'tsi']
        assert product_family in product_family_valid_values

        sensor_on_satellite_valid_values = ['aatsr', 'atsr2', 'slstr_on_sentinel_3a', 'slstr_on_sentinel_3b', 'slstr_on_sentinel_3a_3b']
        assert sensor_on_satellite in sensor_on_satellite_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['incoming_shortwave_radiation', 'outgoing_longwave_radiation', 'outgoing_shortwave_radiation', 'total_solar_irradiance', 'all_variables']
        assert variable in variable_valid_values

        return download_data(day=day, time_aggregation=time_aggregation, version=version, origin=origin, climate_data_record_type=climate_data_record_type, year=year, product_family=product_family, sensor_on_satellite=sensor_on_satellite, month=month, variable=variable, area_group=area_group)

class Collection_sis_hydrology_variables_derived_seasonal_forecast(Collection):

    @Collection.wrapper
    def download(cls, hydrological_model: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], version: OneOrMore[str] = 1): UNREACHABLE()
    
    @classmethod
    def __download__(cls, hydrological_model: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], version: OneOrMore[str] = 1):
        hydrological_model_valid_values = ['e_hypecatch_m00', 'e_hypecatch_m01', 'e_hypecatch_m02', 'e_hypecatch_m05', 'e_hypecatch_m06', 'e_hypecatch_m07', 'e_hypecatch_m08', 'e_hypecatch_m09', 'e_hypegrid', 'lisflood_efas', 'vic_wur']
        assert hydrological_model in hydrological_model_valid_values

        year_valid_values = ['2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['river_discharge', 'reference_river_discharge_lower_tercile', 'reference_river_discharge_upper_tercile', 'brier_skill_score_above_normal_conditions', 'brier_skill_score_below_normal_conditions', 'continuous_ranked_probability_skill_score', 'fair_ranked_probability_skill_score']
        assert variable in variable_valid_values

        version_valid_values = ['1']
        assert version in version_valid_values

        return download_data(hydrological_model=hydrological_model, year=year, month=month, variable=variable, version=version)

class Collection_ecv_for_climate_change(Collection):

    @Collection.wrapper
    def download(cls, time_aggregation: OneOrMore[str], origin: OneOrMore[str], year: OneOrMore[str], climate_reference_period: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, time_aggregation: OneOrMore[str], origin: OneOrMore[str], year: OneOrMore[str], climate_reference_period: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str]):
        time_aggregation_valid_values = ['1_month_mean', '12_month_running_mean']
        assert time_aggregation in time_aggregation_valid_values

        origin_valid_values = ['era5', 'era5_land', 'era_interim']
        assert origin in origin_valid_values

        year_valid_values = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        climate_reference_period_valid_values = ['1981_2010', '1991_2020']
        assert climate_reference_period in climate_reference_period_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        product_type_valid_values = ['anomaly', 'climatology', 'monthly_mean']
        assert product_type in product_type_valid_values

        variable_valid_values = ['surface_air_temperature', 'surface_air_relative_humidity', '0_7cm_volumetric_soil_moisture', 'precipitation', 'sea_ice_cover']
        assert variable in variable_valid_values

        return download_data(time_aggregation=time_aggregation, origin=origin, year=year, climate_reference_period=climate_reference_period, month=month, product_type=product_type, variable=variable)

class Collection_sis_energy_pecd(Collection):

    @Collection.wrapper
    def download(cls, origin: OneOrMore[str], spatial_resolution: OneOrMore[str], year: OneOrMore[str], temporal_period: OneOrMore[str], month: OneOrMore[str], emissions: OneOrMore[str], technology: OneOrMore[str], variable: OneOrMore[str], area: Optional[str] = None, pecd_version: str = 'pecd4_1', area_group: Union[GeographicExtentType, FreeEditionType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, origin: OneOrMore[str], spatial_resolution: OneOrMore[str], year: OneOrMore[str], temporal_period: OneOrMore[str], month: OneOrMore[str], emissions: OneOrMore[str], technology: OneOrMore[str], variable: OneOrMore[str], area: Optional[str] = None, pecd_version: str = 'pecd4_1', area_group: Union[GeographicExtentType, FreeEditionType] = 'global'):
        origin_valid_values = ['era5_reanalysis', 'cmcc_cm2_sr5', 'ec_earth3', 'mpi_esm1_2_hr']
        assert origin in origin_valid_values

        spatial_resolution_valid_values = ['0_25_degree', 'nuts_0', 'nuts_2', 'peof', 'peon', 'szof', 'szon']
        assert spatial_resolution in spatial_resolution_valid_values

        year_valid_values = ['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057', '2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065']
        assert year in year_valid_values

        temporal_period_valid_values = ['historical', 'future_projections']
        assert temporal_period in temporal_period_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        emissions_valid_values = ['ssp2_4_5']
        assert emissions in emissions_valid_values

        technology_valid_values = ['20', '21', '22', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43']
        assert technology in technology_valid_values

        variable_valid_values = ['100m_wind_speed', '10m_wind_speed', '2m_temperature', 'population_weighted_temperature', 'surface_solar_radiation_downwards', 'total_precipitation', 'latitude_weights', 'nuts_0_regions_mask', 'nuts_2_regions_mask', 'peof_regions_mask', 'peon_regions_mask', 'population_density_mask', 'power_law_coefficients', 'solar_pv_mask', 'szof_regions_mask', 'szon_regions_mask', 'wind_power_regions_mask']
        assert variable in variable_valid_values

        pecd_version_valid_values = ['pecd4_1']
        assert pecd_version in pecd_version_valid_values

        return download_data(origin=origin, spatial_resolution=spatial_resolution, year=year, temporal_period=temporal_period, month=month, emissions=emissions, technology=technology, variable=variable, area=area, pecd_version=pecd_version, area_group=area_group)

class Collection_satellite_sea_ice_concentration(Collection):

    @Collection.wrapper
    def download(cls, region: OneOrMore[str], day: OneOrMore[str], cdr_type: OneOrMore[str], version: str, origin: str, year: OneOrMore[str], sensor: str, month: OneOrMore[str], temporal_aggregation: str, variable: str = 'all'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, region: OneOrMore[str], day: OneOrMore[str], cdr_type: OneOrMore[str], version: str, origin: str, year: OneOrMore[str], sensor: str, month: OneOrMore[str], temporal_aggregation: str, variable: str = 'all'):
        region_valid_values = ['northern_hemisphere', 'southern_hemisphere']
        assert region in region_valid_values

        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        cdr_type_valid_values = ['cdr', 'icdr']
        assert cdr_type in cdr_type_valid_values

        version_valid_values = ['v2', 'v3']
        assert version in version_valid_values

        origin_valid_values = ['esa_cci', 'eumetsat_osi_saf']
        assert origin in origin_valid_values

        year_valid_values = ['1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        sensor_valid_values = ['ssmis', 'amsr']
        assert sensor in sensor_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        temporal_aggregation_valid_values = ['daily', 'monthly']
        assert temporal_aggregation in temporal_aggregation_valid_values

        variable_valid_values = ['all']
        assert variable in variable_valid_values

        return download_data(region=region, day=day, cdr_type=cdr_type, version=version, origin=origin, year=year, sensor=sensor, month=month, temporal_aggregation=temporal_aggregation, variable=variable)

class Collection_derived_utci_historical(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], product_type: str, variable: OneOrMore[str], version: str = '1_1', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], product_type: str, variable: OneOrMore[str], version: str = '1_1', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        year_valid_values = ['1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        product_type_valid_values = ['consolidated_dataset', 'intermediate_dataset']
        assert product_type in product_type_valid_values

        variable_valid_values = ['universal_thermal_climate_index', 'mean_radiant_temperature']
        assert variable in variable_valid_values

        version_valid_values = ['1_1', '1_0']
        assert version in version_valid_values

        return download_data(day=day, year=year, month=month, product_type=product_type, variable=variable, version=version, area_group=area_group)

class Collection_sis_water_level_change_timeseries_cmip6(Collection):

    @Collection.wrapper
    def download(cls, model: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], temporal_aggregation: OneOrMore[str], variable: OneOrMore[str], experiment: str): UNREACHABLE()
    
    @classmethod
    def __download__(cls, model: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], temporal_aggregation: OneOrMore[str], variable: OneOrMore[str], experiment: str):
        model_valid_values = ['cmcc_cm2_vhr4', 'ec_earth3p_hr', 'gfdl_cm4c192_sst', 'hadgem3_gc31_hm', 'hadgem3_gc31_hm_sst']
        assert model in model_valid_values

        year_valid_values = ['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        temporal_aggregation_valid_values = ['10_min', 'daily_maximum', 'hourly', 'annual']
        assert temporal_aggregation in temporal_aggregation_valid_values

        variable_valid_values = ['mean_sea_level', 'storm_surge_residual', 'tidal_elevation', 'total_water_level']
        assert variable in variable_valid_values

        experiment_valid_values = ['future', 'historical', 'reanalysis']
        assert experiment in experiment_valid_values

        return download_data(model=model, year=year, month=month, temporal_aggregation=temporal_aggregation, variable=variable, experiment=experiment)

class Collection_satellite_lai_fapar(Collection):

    @Collection.wrapper
    def download(cls, product_version: str, year: OneOrMore[str], sensor: str, nominal_day: OneOrMore[str], month: OneOrMore[str], horizontal_resolution: OneOrMore[str], satellite: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, product_version: str, year: OneOrMore[str], sensor: str, nominal_day: OneOrMore[str], month: OneOrMore[str], horizontal_resolution: OneOrMore[str], satellite: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        product_version_valid_values = ['v0', 'v1', 'v2', 'v3', 'v4']
        assert product_version in product_version_valid_values

        year_valid_values = ['1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
        assert year in year_valid_values

        sensor_valid_values = ['avhrr', 'vgt', 'olci_and_slstr']
        assert sensor in sensor_valid_values

        nominal_day_valid_values = ['03', '10', '13', '20', '21', '22', '23', '24', '28', '29', '30', '31']
        assert nominal_day in nominal_day_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        horizontal_resolution_valid_values = ['300m', '1km', '4km']
        assert horizontal_resolution in horizontal_resolution_valid_values

        satellite_valid_values = ['proba', 'spot', 'noaa_7', 'noaa_9', 'noaa_11', 'noaa_14', 'noaa_16', 'noaa_17', 'sentinel_3']
        assert satellite in satellite_valid_values

        variable_valid_values = ['fapar', 'lai']
        assert variable in variable_valid_values

        return download_data(product_version=product_version, year=year, sensor=sensor, nominal_day=nominal_day, month=month, horizontal_resolution=horizontal_resolution, satellite=satellite, variable=variable, area_group=area_group)

class Collection_satellite_land_cover(Collection):

    @Collection.wrapper
    def download(cls, year: OneOrMore[str], version: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global', variable: str = 'all'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, year: OneOrMore[str], version: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global', variable: str = 'all'):
        year_valid_values = ['1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
        assert year in year_valid_values

        version_valid_values = ['v2_0_7cds', 'v2_1_1']
        assert version in version_valid_values

        variable_valid_values = ['all']
        assert variable in variable_valid_values

        return download_data(year=year, version=version, area_group=area_group, variable=variable)

class Collection_satellite_total_column_water_vapour_ocean(Collection):

    @Collection.wrapper
    def download(cls, origin: str, climate_data_record_type: str, year: OneOrMore[str], month: OneOrMore[str], temporal_aggregation: str, variable: str = 'all'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, origin: str, climate_data_record_type: str, year: OneOrMore[str], month: OneOrMore[str], temporal_aggregation: str, variable: str = 'all'):
        origin_valid_values = ['c3s', 'eumetsat']
        assert origin in origin_valid_values

        climate_data_record_type_valid_values = ['icdr', 'tcdr']
        assert climate_data_record_type in climate_data_record_type_valid_values

        year_valid_values = ['1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        temporal_aggregation_valid_values = ['monthly', '6_hourly']
        assert temporal_aggregation in temporal_aggregation_valid_values

        variable_valid_values = ['all']
        assert variable in variable_valid_values

        return download_data(origin=origin, climate_data_record_type=climate_data_record_type, year=year, month=month, temporal_aggregation=temporal_aggregation, variable=variable)

class Collection_projections_cmip5_monthly_pressure_levels(Collection):

    @Collection.wrapper
    def download(cls, period: OneOrMore[str], model: str, variable: OneOrMore[str], experiment: str, ensemble_member: str = 'r1i1p1'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, period: OneOrMore[str], model: str, variable: OneOrMore[str], experiment: str, ensemble_member: str = 'r1i1p1'):
        period_valid_values = ['185001-185412', '185001-185912', '185001-187512', '185001-187912', '185001-189912', '185001-190012', '185001-194912', '185001-195012', '185001-200512', '185001-201212', '185101-187512', '185101-190012', '185501-185912', '185912-188411', '186001-186412', '186001-186912', '186101-186512', '186501-186912', '186601-187012', '187001-187412', '187001-187912', '187101-187512', '187501-187912', '187601-188012', '187601-190012', '188001-188412', '188001-188912', '188001-190912', '188001-195012', '188101-188512', '188412-190911', '188501-188912', '188601-189012', '189001-189412', '189001-189912', '189101-189512', '189501-189912', '189601-190012', '190001-190412', '190001-190912', '190001-194912', '190001-199912', '190101-190512', '190101-192512', '190101-195012', '190501-190912', '190601-191012', '190912-193411', '191001-191412', '191001-191912', '191001-193912', '191101-191512', '191501-191912', '191601-192012', '192001-192412', '192001-192912', '192101-192512', '192501-192912', '192601-193012', '192601-195012', '193001-193412', '193001-193912', '193101-193512', '193412-195911', '193501-193912', '193601-194012', '194001-194412', '194001-194912', '194001-196912', '194101-194512', '194501-194912', '194601-195012', '195001-195412', '195001-195912', '195001-199912', '195001-200512', '195001-200912', '195001-201212', '195101-195512', '195101-197512', '195101-200012', '195101-200512', '195101-200812', '195101-201012', '195501-195912', '195501-200512', '195601-196012', '195912-198411', '196001-196412', '196001-196912', '196101-196512', '196101-200512', '196501-196912', '196601-197012', '197001-197412', '197001-197912', '197001-199912', '197101-197512', '197501-197912', '197601-198012', '197601-200012', '197804-197812', '197809-200811', '197901-198312', '197901-198812', '197901-200512', '197901-200812', '197901-200912', '197901-201012', '198001-198412', '198001-198912', '198101-198512', '198401-198812', '198412-200511', '198412-200512', '198501-198912', '198601-199012', '198901-199312', '198901-199812', '199001-199412', '199001-199912', '199101-199512', '199401-199812', '199501-199912', '199601-200012', '199901-200312', '199901-200812', '200001-200412', '200001-200512', '200001-200612', '200001-200912', '200001-201212', '200101-200512', '200101-201012', '200401-200812', '200501-200512', '200512-201111', '200512-203011', '200601-200812', '200601-200912', '200601-201012', '200601-201512', '200601-202512', '200601-203012', '200601-203512', '200601-204412', '200601-204512', '200601-204912', '200601-205012', '200601-205412', '200601-205512', '200601-206012', '200601-206512', '200601-209912', '200601-210012', '200601-210212', '200601-210512', '200812-200812', '200901-200912', '201001-201412', '201001-201912', '201101-201512', '201112-203611', '201601-202012', '201601-202512', '202001-202912', '202101-202512', '202601-203012', '202601-203512', '202601-205012', '203001-203912', '203012-205511', '203101-203512', '203601-204012', '203601-204512', '203601-206512', '203612-206111', '204001-204912', '204101-204512', '204501-210012', '204601-205012', '204601-205512', '204601-208512', '205001-205912', '205001-210012', '205101-205512', '205101-207512', '205101-209912', '205101-210012', '205101-210112', '205512-208011', '205601-206012', '205601-206512', '205601-209912', '205601-210012', '206001-206912', '206101-206512', '206101-210112', '206112-208611', '206601-207012', '206601-207512', '206601-209512', '206601-209912', '207001-207912', '207101-207512', '207601-208012', '207601-208512', '207601-210012', '208001-208912', '208012-209911', '208012-209912', '208012-210011', '208012-210012', '208101-208512', '208601-209012', '208601-209512', '208601-210012', '208612-209911', '209001-210012', '209101-209512', '209601-209912', '209601-210012', '209601-210112', '209601-210512', '209912-212411', '210001-210012', '210001-219912', '210012-210012', '210101-210912', '210101-212512', '210101-214912', '210101-215012', '210101-220012', '210101-230012', '210601-211512', '210601-220512', '211001-211912', '211601-212512', '212001-212912', '212412-214911', '212601-213512', '212601-215012', '213001-213912', '213601-214512', '214001-214912', '214601-215512', '214912-217411', '215001-215912', '215001-219912', '215101-217512', '215101-220012', '215601-216512', '216001-216912', '216601-217512', '217001-217912', '217412-219911', '217601-218512', '217601-220012', '218001-218912', '218601-219512', '219001-219912', '219601-220512', '219912-222411', '220001-220912', '220001-224912', '220001-230012', '220101-222512', '220101-225012', '220101-230012', '220601-221512', '220601-230012', '221001-221912', '221601-222512', '222001-222912', '222412-224911', '222601-223512', '222601-225012', '223001-223912', '223601-224512', '224001-224912', '224601-225512', '224912-227411', '225001-225912', '225001-229912', '225001-230012', '225101-227512', '225101-230012', '225601-226512', '226001-226912', '226601-227512', '227001-227912', '227412-229911', '227601-230012', '228001-228912', '229001-230012', '229912-229912']
        assert period in period_valid_values

        model_valid_values = ['access1_0', 'access1_3', 'bcc_csm1_1', 'bcc_csm1_1_m', 'bnu_esm', 'ccsm4', 'cesm1_bgc', 'cesm1_cam5', 'cesm1_fastchem', 'cesm1_waccm', 'cmcc_cesm', 'cmcc_cms', 'cnrm_cm5', 'cnrm_cm5_2', 'canam4', 'cancm4', 'canesm2', 'ec_earth', 'fgoals_g2', 'fgoals_s2', 'fio_esm', 'gfdl_cm2p1', 'gfdl_cm3', 'gfdl_esm2g', 'gfdl_esm2m', 'gfdl_hiram_c180', 'gfdl_hiram_c360', 'giss_e2_h', 'giss_e2_h_cc', 'giss_e2_r', 'giss_e2_r_cc', 'hadcem3', 'hadgem2_a', 'hadgem2_cc', 'hadgem2_es', 'inmcm4', 'ipsl_cm5a_lr', 'ipsl_cm5a_mr', 'ipsl_cm5b_lr', 'mpi_esm_lr', 'mpi_esm_mr', 'mpi_esm_p', 'noresm1_m', 'noresm1_me']
        assert model in model_valid_values

        variable_valid_values = ['geopotential_height', 'temperature', 'u_component_of_wind', 'v_component_of_wind', 'specific_humidity', 'relative_humidity']
        assert variable in variable_valid_values

        experiment_valid_values = ['amip', 'historical', 'rcp_2_6', 'rcp_4_5', 'rcp_6_0', 'rcp_8_5']
        assert experiment in experiment_valid_values

        ensemble_member_valid_values = ['r10i1p1', 'r12i1p1', 'r1i1p1', 'r1i1p121', 'r1i1p124', 'r1i1p125', 'r1i1p126', 'r1i1p127', 'r1i1p128', 'r1i1p2', 'r1i1p3', 'r1i2p1', 'r1i2p2', 'r2i1p1', 'r2i1p2', 'r2i1p3', 'r2i3p1', 'r3i1p1', 'r3i1p2', 'r3i1p3', 'r3i2p1', 'r4i1p1', 'r4i1p2', 'r4i1p3', 'r4i3p1', 'r5i1p1', 'r5i1p2', 'r5i1p3', 'r5i3p1', 'r6i1p1', 'r6i1p2', 'r6i1p3', 'r7i1p1', 'r8i1p1', 'r9i1p1']
        assert ensemble_member in ensemble_member_valid_values

        return download_data(period=period, model=model, variable=variable, experiment=experiment, ensemble_member=ensemble_member)

class Collection_sis_hydrology_meteorology_derived_projections(Collection):

    @Collection.wrapper
    def download(cls, period: OneOrMore[str], time_aggregation: OneOrMore[str], processing_type: str, ensemble_member: OneOrMore[str], rcm: str, horizontal_resolution: str, gcm: str, product_type: str, variable: OneOrMore[str], variable_type: str, experiment: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, period: OneOrMore[str], time_aggregation: OneOrMore[str], processing_type: str, ensemble_member: OneOrMore[str], rcm: str, horizontal_resolution: str, gcm: str, product_type: str, variable: OneOrMore[str], variable_type: str, experiment: OneOrMore[str]):
        period_valid_values = ['1971_2000', '2011_2040', '2041_2070', '2071_2100', '1_5_c', '2_0_c', '3_0_c', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057', '2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065', '2066', '2067', '2068', '2069', '2070', '2071', '2072', '2073', '2074', '2075', '2076', '2077', '2078', '2079', '2080', '2081', '2082', '2083', '2084', '2085', '2086', '2087', '2088', '2089', '2090', '2091', '2092', '2093', '2094', '2095', '2096', '2097', '2098', '2099', '2100']
        assert period in period_valid_values

        time_aggregation_valid_values = ['daily', 'monthly_mean', 'annual_mean']
        assert time_aggregation in time_aggregation_valid_values

        processing_type_valid_values = ['original', 'bias_corrected']
        assert processing_type in processing_type_valid_values

        ensemble_member_valid_values = ['r1i1p1', 'r12i1p1', 'r2i1p1']
        assert ensemble_member in ensemble_member_valid_values

        rcm_valid_values = ['cclm4_8_17', 'racmo22e', 'csc_remo2009', 'rca4']
        assert rcm in rcm_valid_values

        horizontal_resolution_valid_values = ['5_km', '0_11_degrees']
        assert horizontal_resolution in horizontal_resolution_valid_values

        gcm_valid_values = ['hadgem2_es', 'mpi_esm_lr', 'ec_earth']
        assert gcm in gcm_valid_values

        product_type_valid_values = ['climate_impact_indicators', 'essential_climate_variables']
        assert product_type in product_type_valid_values

        variable_valid_values = ['2m_air_temperature', 'precipitation', 'longest_dry_spells', 'number_of_dry_spells', 'highest_5_day_precipitation_amount']
        assert variable in variable_valid_values

        variable_type_valid_values = ['relative_change_from_reference_period', 'absolute_change_from_reference_period', 'absolute_values']
        assert variable_type in variable_type_valid_values

        experiment_valid_values = ['historical', 'rcp_2_6', 'rcp_4_5', 'rcp_8_5', 'degree_scenario']
        assert experiment in experiment_valid_values

        return download_data(period=period, time_aggregation=time_aggregation, processing_type=processing_type, ensemble_member=ensemble_member, rcm=rcm, horizontal_resolution=horizontal_resolution, gcm=gcm, product_type=product_type, variable=variable, variable_type=variable_type, experiment=experiment)

class Collection_sis_water_level_change_indicators_cmip6(Collection):

    @Collection.wrapper
    def download(cls, period: OneOrMore[str], multi_model_ensemble_statistic: OneOrMore[str], statistic: OneOrMore[str], model: OneOrMore[str], confidence_interval: OneOrMore[str], derived_variable: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], experiment: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, period: OneOrMore[str], multi_model_ensemble_statistic: OneOrMore[str], statistic: OneOrMore[str], model: OneOrMore[str], confidence_interval: OneOrMore[str], derived_variable: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], experiment: OneOrMore[str]):
        period_valid_values = ['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '1951_1980', '1985_2014', '2021_2050']
        assert period in period_valid_values

        multi_model_ensemble_statistic_valid_values = ['ensemble_mean', 'ensemble_median', 'ensemble_range', 'ensemble_standard_deviation', 'negative_ensemble_counts', 'positive_ensemble_counts']
        assert multi_model_ensemble_statistic in multi_model_ensemble_statistic_valid_values

        statistic_valid_values = ['1_year', '10_year', '100_year', '2_year', '25_year', '5_year', '50_year', '75_year', '10th', '25th', '5th', '50th', '75th', '90th', '95th']
        assert statistic in statistic_valid_values

        model_valid_values = ['cmcc_cm2_vhr4', 'ec_earth3p_hr', 'hadgem3_gc31_hm', 'hadgem3_gc31_hm_sst']
        assert model in model_valid_values

        confidence_interval_valid_values = ['best_fit', 'low_bound_confidence_interval', 'high_bound_confidence_interval']
        assert confidence_interval in confidence_interval_valid_values

        derived_variable_valid_values = ['absolute_change', 'absolute_value', 'percentage_change']
        assert derived_variable in derived_variable_valid_values

        product_type_valid_values = ['single_model', 'multi_model_ensemble', 'reanalysis']
        assert product_type in product_type_valid_values

        variable_valid_values = ['surge_level', 'total_water_level', 'mean_sea_level', 'tidal_range', 'highest_astronomical_tide', 'lowest_astronomical_tide', 'annual_mean_of_highest_high_water', 'annual_mean_of_lowest_low_water']
        assert variable in variable_valid_values

        experiment_valid_values = ['historical', 'future']
        assert experiment in experiment_valid_values

        return download_data(period=period, multi_model_ensemble_statistic=multi_model_ensemble_statistic, statistic=statistic, model=model, confidence_interval=confidence_interval, derived_variable=derived_variable, product_type=product_type, variable=variable, experiment=experiment)

class Collection_sis_agroclimatic_indicators(Collection):

    @Collection.wrapper
    def download(cls, period: OneOrMore[str], version: OneOrMore[str], origin: str, temporal_aggregation: str, variable: OneOrMore[str], experiment: str): UNREACHABLE()
    
    @classmethod
    def __download__(cls, period: OneOrMore[str], version: OneOrMore[str], origin: str, temporal_aggregation: str, variable: OneOrMore[str], experiment: str):
        period_valid_values = ['195101_198012', '198101_201012', '201101_204012', '204101_207012', '207101_209912']
        assert period in period_valid_values

        version_valid_values = ['1_0', '1_1']
        assert version in version_valid_values

        origin_valid_values = ['miroc_esm_chem_model', 'ipsl_cm5a_lr_model', 'noresm1_m_model', 'hadgem2_es_model', 'gfdl_esm2m_model', 'era_interim_reanalysis']
        assert origin in origin_valid_values

        temporal_aggregation_valid_values = ['10_day', 'season', 'annual']
        assert temporal_aggregation in temporal_aggregation_valid_values

        variable_valid_values = ['biologically_effective_degree_days', 'growing_season_length', 'maximum_number_of_consecutive_dry_days', 'maximum_number_of_consecutive_frost_days', 'cold_spell_duration_index', 'maximum_number_of_consecutive_summer_days', 'maximum_number_of_consecutive_wet_days', 'mean_of_diurnal_temperature_range', 'frost_days', 'ice_days', 'heavy_precipitation_days', 'very_heavy_precipitation_days', 'precipitation_sum', 'wet_days', 'simple_daily_intensity_index', 'summer_days', 'mean_of_daily_mean_temperature', 'mean_of_daily_minimum_temperature', 'minimum_of_daily_minimum_temperature', 'maximum_of_daily_minimum_temperature', 'tropical_nights', 'mean_of_daily_maximum_temperature', 'minimum_of_daily_maximum_temperature', 'maximum_of_daily_maximum_temperature', 'warm_spell_duration_index', 'warm_and_wet_days']
        assert variable in variable_valid_values

        experiment_valid_values = ['historical', 'rcp2_6', 'rcp4_5', 'rcp6_0', 'rcp8_5']
        assert experiment in experiment_valid_values

        return download_data(period=period, version=version, origin=origin, temporal_aggregation=temporal_aggregation, variable=variable, experiment=experiment)

class Collection_projections_climate_atlas(Collection):

    @Collection.wrapper
    def download(cls, period: str, origin: str, variable: str, domain: str, experiment: str): UNREACHABLE()
    
    @classmethod
    def __download__(cls, period: str, origin: str, variable: str, domain: str, experiment: str):
        period_valid_values = ['1850-2005', '1850-2014', '1950-2005', '1950-2014', '1970-2005', '2006-2098', '2006-2100', '2015-2100']
        assert period in period_valid_values

        origin_valid_values = ['cmip5', 'cmip6', 'cordex']
        assert origin in origin_valid_values

        variable_valid_values = ['monthly_mean_of_daily_accumulated_precipitation', 'monthly_mean_of_daily_accumulated_snowfall_precipitation', 'annual_cooling_degree_days', 'annual_consecutive_dry_days', 'monthly_count_of_frost_days', 'annual_heating_degree_days', 'monthly_mean_of_acidity_of_seawater', 'monthly_maximum_of_1_day_accumulated_precipitation', 'monthly_maximum_of_5_day_accumulated_precipitation', 'monthly_mean_of_daily_mean_wind_speed', 'monthly_mean_of_sea_ice_area_percentage', 'standardized_precipitation_index_for_6_months_cumulation_period', 'monthly_mean_of_sea_surface_temperature', 'monthly_mean_of_daily_mean_temperature', 'monthly_mean_of_daily_minimum_temperature', 'monthly_minimum_of_daily_minimum_temperature', 'monthly_mean_of_daily_maximum_temperature', 'monthly_count_of_days_with_maximum_temperature_above_35_c', 'bias_adjusted_monthly_count_of_days_with_maximum_temperature_above_35_c', 'monthly_count_of_days_with_maximum_temperature_above_40_c', 'bias_adjusted_monthly_count_of_days_with_maximum_temperature_above_40_c', 'monthly_maximum_of_daily_maximum_temperature']
        assert variable in variable_valid_values

        domain_valid_values = ['global', 'africa', 'antarctica', 'arctic', 'australasia', 'central_america', 'east_asia', 'europe', 'north_america', 'south_america', 'southeast_asia', 'south_asia']
        assert domain in domain_valid_values

        experiment_valid_values = ['historical', 'rcp_2_6', 'rcp_4_5', 'rcp_8_5', 'ssp1_2_6', 'ssp2_4_5', 'ssp3_7_0', 'ssp5_8_5']
        assert experiment in experiment_valid_values

        return download_data(period=period, origin=origin, variable=variable, domain=domain, experiment=experiment)

class Collection_reanalysis_carra_pressure_levels(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], leadtime_hour: OneOrMore[str], month: OneOrMore[str], product_type: str, variable: OneOrMore[str], pressure_level: OneOrMore[str], domain: str, data_format: str = 'grib'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], leadtime_hour: OneOrMore[str], month: OneOrMore[str], product_type: str, variable: OneOrMore[str], pressure_level: OneOrMore[str], domain: str, data_format: str = 'grib'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_valid_values = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
        assert time in time_valid_values

        year_valid_values = ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        leadtime_hour_valid_values = ['1', '2', '3', '4', '5', '6', '9', '12', '15', '18', '21', '24', '27', '30']
        assert leadtime_hour in leadtime_hour_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        product_type_valid_values = ['analysis', 'forecast']
        assert product_type in product_type_valid_values

        variable_valid_values = ['cloud_cover', 'geometric_vertical_velocity', 'geopotential', 'graupel', 'potential_vorticity', 'pseudo_adiabatic_potential_temperature', 'relative_humidity', 'specific_cloud_ice_water_content', 'specific_cloud_liquid_water_content', 'specific_cloud_rain_water_content', 'specific_cloud_snow_water_content', 'temperature', 'u_component_of_wind', 'v_component_of_wind']
        assert variable in variable_valid_values

        pressure_level_valid_values = ['10', '20', '30', '50', '70', '100', '150', '200', '250', '300', '400', '500', '600', '700', '750', '800', '825', '850', '875', '900', '925', '950', '1000']
        assert pressure_level in pressure_level_valid_values

        domain_valid_values = ['east_domain', 'west_domain']
        assert domain in domain_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(day=day, time=time, year=year, leadtime_hour=leadtime_hour, month=month, product_type=product_type, variable=variable, pressure_level=pressure_level, domain=domain, data_format=data_format)

class Collection_sis_biodiversity_cmip5_global(Collection):

    @Collection.wrapper
    def download(cls, statistic: OneOrMore[str], model: OneOrMore[str], ensemble_member: OneOrMore[str], derived_variable: OneOrMore[str], temporal_aggregation: OneOrMore[str], variable: OneOrMore[str], experiment: OneOrMore[str], version: OneOrMore[str] = '1.0'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, statistic: OneOrMore[str], model: OneOrMore[str], ensemble_member: OneOrMore[str], derived_variable: OneOrMore[str], temporal_aggregation: OneOrMore[str], variable: OneOrMore[str], experiment: OneOrMore[str], version: OneOrMore[str] = '1.0'):
        statistic_valid_values = ['mean', 'median', '25th_quartile', '75th_quartile']
        assert statistic in statistic_valid_values

        model_valid_values = ['access1_0', 'bcc_csm1_1_m', 'csiro_mk3_6_0', 'gfdl_esm2m', 'hadgem2_cc', 'hadgem2_es', 'ipsl_cm5a_lr', 'ipsl_cm5a_mr', 'ipsl_cm5b_lr', 'noresm1_m']
        assert model in model_valid_values

        ensemble_member_valid_values = ['r1i1p1', 'r2i1p1']
        assert ensemble_member in ensemble_member_valid_values

        derived_variable_valid_values = ['annual_maximum', 'annual_maximum_of_daily_mean', 'annual_mean', 'annual_mean_of_daily_maximum', 'annual_mean_of_daily_minimum', 'annual_minimum', 'annual_sum', 'coldest_quarter', 'driest_quarter', 'end_of_season', 'length_of_season', 'maximum_length', 'mean_intensity', 'mean_length_with_minimum_5_days', 'monthly_mean', 'monthly_mean_of_daily_maximum', 'monthly_mean_of_daily_minimum', 'monthly_sum', 'number_of_occurrences', 'start_of_season', 'warmest_quarter', 'wettest_quarter']
        assert derived_variable in derived_variable_valid_values

        temporal_aggregation_valid_values = ['annual', 'climatology', 'monthly']
        assert temporal_aggregation in temporal_aggregation_valid_values

        variable_valid_values = ['annual_mean_temperature', 'mean_diurnal_range', 'isothermality', 'temperature_seasonality', 'maximum_temperature_of_warmest_month', 'minimum_temperature_of_coldest_month', 'temperature_annual_range', 'mean_temperature_of_wettest_quarter', 'mean_temperature_of_driest_quarter', 'mean_temperature_of_warmest_quarter', 'mean_temperature_of_coldest_quarter', 'annual_precipitation', 'precipitation_of_wettest_month', 'precipitation_of_driest_month', 'precipitation_seasonality', 'precipitation_of_wettest_quarter', 'precipitation_of_driest_quarter', 'precipitation_of_warmest_quarter', 'precipitation_of_coldest_quarter', 'aridity', 'dry_spells', 'dry_days', 'summer_days', 'surface_latent_heat_flux', 'surface_sensible_heat_flux', 'evaporative_fraction', 'frost_days', 'growing_season', 'growing_degree_days', 'growing_degree_days_during_growing_season_length', 'koeppen_geiger_class', 'potential_evaporation', 'sea_ice_concentration', 'sea_surface_temperature', '2m_temperature', 'precipitation', 'water_vapor_pressure', 'cloud_cover', 'volumetric_soil_water', 'wind_speed', 'zonal_wind_speed', 'meridional_wind_speed']
        assert variable in variable_valid_values

        experiment_valid_values = ['rcp4_5', 'rcp8_5']
        assert experiment in experiment_valid_values

        version_valid_values = ['1_0']
        assert version in version_valid_values

        return download_data(statistic=statistic, model=model, ensemble_member=ensemble_member, derived_variable=derived_variable, temporal_aggregation=temporal_aggregation, variable=variable, experiment=experiment, version=version)

class Collection_insitu_gridded_observations_nordic(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], version: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], spatial_interpolation_method: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], version: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], spatial_interpolation_method: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str]):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        version_valid_values = ['24_03', '23_03', '23_09', '24_03', '24_09']
        assert version in version_valid_values

        year_valid_values = ['1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        spatial_interpolation_method_valid_values = ['type_1', 'type_2']
        assert spatial_interpolation_method in spatial_interpolation_method_valid_values

        product_type_valid_values = ['consolidated', 'provisional']
        assert product_type in product_type_valid_values

        variable_valid_values = ['precipitation', 'mean_temperature', 'maximum_temperature', 'minimum_temperature']
        assert variable in variable_valid_values

        return download_data(day=day, version=version, year=year, month=month, spatial_interpolation_method=spatial_interpolation_method, product_type=product_type, variable=variable)

class Collection_reanalysis_era5_pressure_levels_monthly_means(Collection):

    @Collection.wrapper
    def download(cls, time: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], pressure_level: OneOrMore[str], download_format: str = 'unarchived', data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, time: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], variable: OneOrMore[str], pressure_level: OneOrMore[str], download_format: str = 'unarchived', data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        time_valid_values = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
        assert time in time_valid_values

        year_valid_values = ['1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        product_type_valid_values = ['monthly_averaged_reanalysis', 'monthly_averaged_reanalysis_by_hour_of_day', 'monthly_averaged_ensemble_members', 'monthly_averaged_ensemble_members_by_hour_of_day']
        assert product_type in product_type_valid_values

        variable_valid_values = ['divergence', 'fraction_of_cloud_cover', 'geopotential', 'ozone_mass_mixing_ratio', 'potential_vorticity', 'relative_humidity', 'specific_cloud_ice_water_content', 'specific_cloud_liquid_water_content', 'specific_humidity', 'specific_rain_water_content', 'specific_snow_water_content', 'temperature', 'u_component_of_wind', 'v_component_of_wind', 'vertical_velocity', 'vorticity']
        assert variable in variable_valid_values

        pressure_level_valid_values = ['1', '2', '3', '5', '7', '10', '20', '30', '50', '70', '100', '125', '150', '175', '200', '225', '250', '300', '350', '400', '450', '500', '550', '600', '650', '700', '750', '775', '800', '825', '850', '875', '900', '925', '950', '975', '1000']
        assert pressure_level in pressure_level_valid_values

        download_format_valid_values = ['unarchived', 'zip']
        assert download_format in download_format_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        return download_data(time=time, year=year, month=month, product_type=product_type, variable=variable, pressure_level=pressure_level, download_format=download_format, data_format=data_format, area_group=area_group)

class Collection_satellite_precipitation(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time_aggregation: str, year: OneOrMore[str], month: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global', variable: str = 'all'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time_aggregation: str, year: OneOrMore[str], month: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global', variable: str = 'all'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_aggregation_valid_values = ['monthly_mean', 'daily_mean']
        assert time_aggregation in time_aggregation_valid_values

        year_valid_values = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['all']
        assert variable in variable_valid_values

        return download_data(day=day, time_aggregation=time_aggregation, year=year, month=month, area_group=area_group, variable=variable)

class Collection_insitu_observations_gnss(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], year: str, format: str, network_type: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], year: str, format: str, network_type: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        year_valid_values = ['1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014']
        assert year in year_valid_values

        format_valid_values = ['netcdf', 'csv']
        assert format in format_valid_values

        network_type_valid_values = ['igs_daily', 'epn_repro2']
        assert network_type in network_type_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['total_column_water_vapour', 'total_column_water_vapour_era5']
        assert variable in variable_valid_values

        return download_data(day=day, year=year, format=format, network_type=network_type, month=month, variable=variable, area_group=area_group)

class Collection_sis_agrometeorological_indicators(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time: OneOrMore[str], statistic: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global', version: str = '1_1'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time: OneOrMore[str], statistic: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: str, area_group: Union[FreeEditionType, GeographicExtentType] = 'global', version: str = '1_1'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_valid_values = ['06_00', '09_00', '12_00', '15_00', '18_00']
        assert time in time_valid_values

        statistic_valid_values = ['24_hour_maximum', '24_hour_mean', '24_hour_minimum', 'day_time_maximum', 'day_time_mean', 'night_time_mean', 'night_time_minimum']
        assert statistic in statistic_valid_values

        year_valid_values = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['cloud_cover', 'precipitation_flux', 'liquid_precipitation_duration_fraction', 'solid_precipitation_duration_fraction', 'snow_thickness_lwe', 'snow_thickness', 'solar_radiation_flux', 'vapour_pressure', '2m_temperature', '10m_wind_speed', '2m_dewpoint_temperature', '2m_relative_humidity']
        assert variable in variable_valid_values

        version_valid_values = ['1_0', '1_1']
        assert version in version_valid_values

        return download_data(day=day, time=time, statistic=statistic, year=year, month=month, variable=variable, area_group=area_group, version=version)

class Collection_sis_tourism_fire_danger_indicators(Collection):

    @Collection.wrapper
    def download(cls, period: OneOrMore[str], time_aggregation: str, version: str, gcm_model: OneOrMore[str], product_type: str, variable: OneOrMore[str], experiment: str): UNREACHABLE()
    
    @classmethod
    def __download__(cls, period: OneOrMore[str], time_aggregation: str, version: str, gcm_model: OneOrMore[str], product_type: str, variable: OneOrMore[str], experiment: str):
        period_valid_values = ['1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057', '2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065', '2066', '2067', '2068', '2069', '2070', '2071', '2072', '2073', '2074', '2075', '2076', '2077', '2078', '2079', '2080', '2081', '2082', '2083', '2084', '2085', '2086', '2087', '2088', '2089', '2090', '2091', '2092', '2093', '2094', '2095', '2096', '2097', '2098', '1971_1975', '1976_1980', '1981_1982', '1981_1985', '1981_2000', '1981_2005', '1986_1990', '1991_1995', '1996_2000', '2001_2005', '2006_2010', '2011_2015', '2016_2020', '2021_2025', '2021_2040', '2026_2030', '2031_2035', '2036_2040', '2041_2045', '2041_2060', '2046_2050', '2051_2055', '2056_2060', '2061_2065', '2066_2070', '2071_2075', '2076_2080', '2078_2097', '2079_2098', '2081_2085', '2086_2090', '2091_2095', '2096_2098']
        assert period in period_valid_values

        time_aggregation_valid_values = ['daily_indicators', 'seasonal_indicators', 'annual_indicators']
        assert time_aggregation in time_aggregation_valid_values

        version_valid_values = ['v1_0', 'v2_0']
        assert version in version_valid_values

        gcm_model_valid_values = ['cnrm_cm5', 'ec_earth', 'ipsl_cm5a_mr', 'hadgem2_es', 'mpi_esm_lr', 'noresm1_m']
        assert gcm_model in gcm_model_valid_values

        product_type_valid_values = ['single_model', 'multi_model_mean_case', 'multi_model_best_case', 'multi_model_worst_case']
        assert product_type in product_type_valid_values

        variable_valid_values = ['daily_fire_weather_index', 'seasonal_fire_weather_index', 'number_of_days_with_moderate_fire_danger', 'number_of_days_with_high_fire_danger', 'number_of_days_with_very_high_fire_danger']
        assert variable in variable_valid_values

        experiment_valid_values = ['historical', 'rcp2_6', 'rcp4_5', 'rcp8_5']
        assert experiment in experiment_valid_values

        return download_data(period=period, time_aggregation=time_aggregation, version=version, gcm_model=gcm_model, product_type=product_type, variable=variable, experiment=experiment)

class Collection_sis_ecde_climate_indicators(Collection):

    @Collection.wrapper
    def download(cls, other_parameters: OneOrMore[str], origin: str, hydrological_model: OneOrMore[str], ensemble_member: OneOrMore[str], rcm: OneOrMore[str], regional_layer: OneOrMore[str], spatial_aggregation: str, temporal_aggregation: OneOrMore[str], gcm: OneOrMore[str], variable: OneOrMore[str], experiment: OneOrMore[str]): UNREACHABLE()
    
    @classmethod
    def __download__(cls, other_parameters: OneOrMore[str], origin: str, hydrological_model: OneOrMore[str], ensemble_member: OneOrMore[str], rcm: OneOrMore[str], regional_layer: OneOrMore[str], spatial_aggregation: str, temporal_aggregation: OneOrMore[str], gcm: OneOrMore[str], variable: OneOrMore[str], experiment: OneOrMore[str]):
        other_parameters_valid_values = ['max', 'mean', 'min', '30_c', '35_c', '40_c', '1_in_2_year', '1_in_5_year', '1_in_10_year', '1_in_50_year']
        assert other_parameters in other_parameters_valid_values

        origin_valid_values = ['reanalysis', 'projections']
        assert origin in origin_valid_values

        hydrological_model_valid_values = ['e_hype', 'vic_wur']
        assert hydrological_model in hydrological_model_valid_values

        ensemble_member_valid_values = ['r12i1p1', 'r1i1p1', 'r2i1p1', 'r3i1p1']
        assert ensemble_member in ensemble_member_valid_values

        rcm_valid_values = ['aladin53', 'cclm4_8_17', 'hirham5', 'racmo22e', 'rca4', 'this_is_another_remo2009', 'wrf331f', 'wrf381p', 'csc_remo2009']
        assert rcm in rcm_valid_values

        regional_layer_valid_values = ['nuts_level_0', 'nuts_level_1', 'nuts_level_2', 'nuts_level_3', 'non_nuts', 'adriatic_ionian', 'alpine_space', 'northern_periphery_and_arctic', 'atlantic_area', 'baltic_sea_region', 'central_europe', 'danube', 'mediterranean', 'north_sea', 'north_west_europe', 'south_west_europe', 'eu_27', 'eea_32', 'eea_38']
        assert regional_layer in regional_layer_valid_values

        spatial_aggregation_valid_values = ['gridded', 'regional_layer']
        assert spatial_aggregation in spatial_aggregation_valid_values

        temporal_aggregation_valid_values = ['monthly', 'seasonal', 'yearly']
        assert temporal_aggregation in temporal_aggregation_valid_values

        gcm_valid_values = ['cm2_vhr4', 'cm5a_mr', 'cnrm_cm5', 'ec_earth', 'ec_earth3p_hr', 'hadgem2_es', 'hadgem3_gc31_hm', 'hadgem3_gc31_hm_sst', 'ipsl_cm5a_mr', 'mpi_esm_lr', 'noresm1_m']
        assert gcm in gcm_valid_values

        variable_valid_values = ['mean_temperature', 'growing_degree_days', 'heating_degree_days', 'cooling_degree_days', 'tropical_nights', 'hot_days', 'warmest_three_day_period', 'heatwave_days', 'high_utci_days', 'frost_days', 'daily_maximum_temperature', 'daily_minimum_temperature', 'total_precipitation', 'maximum_consecutive_five_day_precipitation', 'extreme_precipitation_total', 'frequency_of_extreme_precipitation', 'flood_recurrence', 'mean_river_discharge', 'aridity_actual', 'consecutive_dry_days', 'duration_of_meteorological_droughts', 'magnitude_of_meteorological_droughts', 'mean_soil_moisture', 'days_with_high_fire_danger', 'mean_wind_speed', 'extreme_wind_speed_days', 'fire_weather_index', 'snowfall_amount', 'relative_sea_level_rise', 'extreme_sea_level']
        assert variable in variable_valid_values

        experiment_valid_values = ['historical', 'rcp4_5', 'rcp8_5', 'ssp5_8_5']
        assert experiment in experiment_valid_values

        return download_data(other_parameters=other_parameters, origin=origin, hydrological_model=hydrological_model, ensemble_member=ensemble_member, rcm=rcm, regional_layer=regional_layer, spatial_aggregation=spatial_aggregation, temporal_aggregation=temporal_aggregation, gcm=gcm, variable=variable, experiment=experiment)

class Collection_satellite_humidity_profiles(Collection):

    @Collection.wrapper
    def download(cls, product_type: str, year: OneOrMore[str], month: OneOrMore[str], variable: str = 'all'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, product_type: str, year: OneOrMore[str], month: OneOrMore[str], variable: str = 'all'):
        product_type_valid_values = ['radio_occultation_data', 'reanalysis_data']
        assert product_type in product_type_valid_values

        year_valid_values = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['all']
        assert variable in variable_valid_values

        return download_data(product_type=product_type, year=year, month=month, variable=variable)

class Collection_reanalysis_era5_pressure_levels(Collection):

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], pressure_level: OneOrMore[str], download_format: str = 'unarchived', data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global', product_type: OneOrMore[str] = 'reanalysis'): UNREACHABLE()
    
    @classmethod
    def __download__(cls, day: OneOrMore[str], time: OneOrMore[str], year: OneOrMore[str], month: OneOrMore[str], variable: OneOrMore[str], pressure_level: OneOrMore[str], download_format: str = 'unarchived', data_format: str = 'grib', area_group: Union[FreeEditionType, GeographicExtentType] = 'global', product_type: OneOrMore[str] = 'reanalysis'):
        day_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        assert day in day_valid_values

        time_valid_values = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
        assert time in time_valid_values

        year_valid_values = ['1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        assert year in year_valid_values

        month_valid_values = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        assert month in month_valid_values

        variable_valid_values = ['divergence', 'fraction_of_cloud_cover', 'geopotential', 'ozone_mass_mixing_ratio', 'potential_vorticity', 'relative_humidity', 'specific_cloud_ice_water_content', 'specific_cloud_liquid_water_content', 'specific_humidity', 'specific_rain_water_content', 'specific_snow_water_content', 'temperature', 'u_component_of_wind', 'v_component_of_wind', 'vertical_velocity', 'vorticity']
        assert variable in variable_valid_values

        pressure_level_valid_values = ['1', '2', '3', '5', '7', '10', '20', '30', '50', '70', '100', '125', '150', '175', '200', '225', '250', '300', '350', '400', '450', '500', '550', '600', '650', '700', '750', '775', '800', '825', '850', '875', '900', '925', '950', '975', '1000']
        assert pressure_level in pressure_level_valid_values

        download_format_valid_values = ['unarchived', 'zip']
        assert download_format in download_format_valid_values

        data_format_valid_values = ['grib', 'netcdf']
        assert data_format in data_format_valid_values

        product_type_valid_values = ['reanalysis', 'ensemble_members', 'ensemble_mean', 'ensemble_spread']
        assert product_type in product_type_valid_values

        return download_data(day=day, time=time, year=year, month=month, variable=variable, pressure_level=pressure_level, download_format=download_format, data_format=data_format, area_group=area_group, product_type=product_type)

