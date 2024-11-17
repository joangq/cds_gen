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

class Collection_insitu_gridded_observations_europe(Collection):
    collection_name = 'insitu-gridded-observations-europe'
    valid_values = dict(
        grid_resolution = ['0_1deg', '0_25deg'],
        period = ['full_period', '1950_1964', '1965_1979', '1980_1994', '1995_2010', '2011_2019', '2011_2020', '2011_2021', '2011_2022', '2011_2023', '2011_2024'],
        product_type = ['ensemble_mean', 'ensemble_spread', 'elevation'],
        variable = ['mean_temperature', 'minimum_temperature', 'maximum_temperature', 'precipitation_amount', 'sea_level_pressure', 'surface_shortwave_downwelling_radiation', 'relative_humidity', 'wind_speed', 'land_surface_elevation'],
        version = ['30_0e', '21_0e', '22_0e', '23_1e', '24_0e', '25_0e', '26_0e', '27_0e', '28_0e', '29_0e'],
    )

    @Collection.wrapper
    def download(cls, grid_resolution: str, period: str, product_type: str, variable: OneOrMore[str], version: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param grid_resolution:
        :type grid_resolution: str

        **Valid values:**
        
        - 0_1deg

        
        - 0_25deg

        ---

        :param period:
        :type period: str

        **Valid values:**
        
        - full_period

        
        - 1950_1964

        
        - 1965_1979

        
        - 1980_1994

        
        - 1995_2010

        
        - 2011_2019

        
        - 2011_2020

        
        - 2011_2021

        
        - 2011_2022

        
        - 2011_2023

        
        - 2011_2024

        ---

        :param product_type:
        :type product_type: str

        **Valid values:**
        
        - ensemble_mean

        
        - ensemble_spread

        
        - elevation

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - mean_temperature

        
        - minimum_temperature

        
        - maximum_temperature

        
        - precipitation_amount

        
        - sea_level_pressure

        
        - surface_shortwave_downwelling_radiation

        
        - relative_humidity

        
        - wind_speed

        
        - land_surface_elevation

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - 30_0e

        
        - 21_0e

        
        - 22_0e

        
        - 23_1e

        
        - 24_0e

        
        - 25_0e

        
        - 26_0e

        
        - 27_0e

        
        - 28_0e

        
        - 29_0e

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_insitu_gridded_observations_europe(grid_resolution: str, period: str, product_type: str, variable: OneOrMore[str], version: OneOrMore[str]):
    return Collection_insitu_gridded_observations_europe.download(grid_resolution=grid_resolution, period=period, product_type=product_type, variable=variable, version=version)

