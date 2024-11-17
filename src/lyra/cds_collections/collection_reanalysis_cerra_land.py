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

class Collection_reanalysis_cerra_land(Collection):
    collection_name = 'reanalysis-cerra-land'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        leadtime_hour = ['1', '2', '3'],
        level_type = ['surface', 'soil'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        product_type = ['analysis', 'forecast'],
        soil_layer = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'],
        time = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00'],
        variable = ['albedo', 'evaporation', 'fraction_of_snow_cover', 'lake_bottom_temperature', 'lake_depth', 'lake_ice_depth', 'lake_ice_temperature', 'lake_mix_layer_depth', 'lake_mix_layer_temperature', 'lake_shape_factor', 'lake_total_layer_temperature', 'land_sea_mask', 'liquid_volumetric_soil_moisture', 'orography', 'percolation', 'skin_temperature', 'snow_albedo', 'snow_density', 'snow_depth', 'snow_depth_water_equivalent', 'snow_melt', 'soil_heat_flux', 'soil_temperature', 'surface_latent_heat_flux', 'surface_net_solar_radiation', 'surface_net_thermal_radiation', 'surface_roughness', 'surface_runoff', 'surface_sensible_heat_flux', 'surface_solar_radiation_downwards', 'surface_thermal_radiation_downwards', 'temperature_of_snow_layer', 'total_precipitation', 'volumetric_soil_moisture', 'volumetric_transpiration_stress_onset', 'volumetric_wilting_point'],
        year = ['1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021'],
        data_format = ['grib', 'netcdf'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], leadtime_hour: OneOrMore[str], level_type: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], soil_layer: OneOrMore[str], time: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], data_format: str = 'grib'): 
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

        :param leadtime_hour:
        :type leadtime_hour: str

        **Valid values:**
        
        - 1

        
        - 2

        
        - 3

        ---

        :param level_type:
        :type level_type: str

        **Valid values:**
        
        - surface

        
        - soil

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

        :param product_type:
        :type product_type: str

        **Valid values:**
        
        - analysis

        
        - forecast

        ---

        :param soil_layer:
        :type soil_layer: str

        **Valid values:**
        
        - 1

        
        - 2

        
        - 3

        
        - 4

        
        - 5

        
        - 6

        
        - 7

        
        - 8

        
        - 9

        
        - 10

        
        - 11

        
        - 12

        
        - 13

        
        - 14

        ---

        :param time:
        :type time: str

        **Valid values:**
        
        - 00:00

        
        - 03:00

        
        - 06:00

        
        - 09:00

        
        - 12:00

        
        - 15:00

        
        - 18:00

        
        - 21:00

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - albedo

        
        - evaporation

        
        - fraction_of_snow_cover

        
        - lake_bottom_temperature

        
        - lake_depth

        
        - lake_ice_depth

        
        - lake_ice_temperature

        
        - lake_mix_layer_depth

        
        - lake_mix_layer_temperature

        
        - lake_shape_factor

        
        - lake_total_layer_temperature

        
        - land_sea_mask

        
        - liquid_volumetric_soil_moisture

        
        - orography

        
        - percolation

        
        - skin_temperature

        
        - snow_albedo

        
        - snow_density

        
        - snow_depth

        
        - snow_depth_water_equivalent

        
        - snow_melt

        
        - soil_heat_flux

        
        - soil_temperature

        
        - surface_latent_heat_flux

        
        - surface_net_solar_radiation

        
        - surface_net_thermal_radiation

        
        - surface_roughness

        
        - surface_runoff

        
        - surface_sensible_heat_flux

        
        - surface_solar_radiation_downwards

        
        - surface_thermal_radiation_downwards

        
        - temperature_of_snow_layer

        
        - total_precipitation

        
        - volumetric_soil_moisture

        
        - volumetric_transpiration_stress_onset

        
        - volumetric_wilting_point

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

        ---

        :param data_format:
        :type data_format: str

        **Valid values:**
        
        - grib

        
        - netcdf

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_reanalysis_cerra_land(day: OneOrMore[str], leadtime_hour: OneOrMore[str], level_type: OneOrMore[str], month: OneOrMore[str], product_type: OneOrMore[str], soil_layer: OneOrMore[str], time: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], data_format: str = 'grib'):
    return Collection_reanalysis_cerra_land.download(day=day, leadtime_hour=leadtime_hour, level_type=level_type, month=month, product_type=product_type, soil_layer=soil_layer, time=time, variable=variable, year=year, data_format=data_format)

