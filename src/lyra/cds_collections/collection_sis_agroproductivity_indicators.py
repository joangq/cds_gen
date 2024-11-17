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

class Collection_sis_agroproductivity_indicators(Collection):
    collection_name = 'sis-agroproductivity-indicators'
    valid_values = dict(
        crop_type = ['maize', 'soybean', 'spring_wheat', 'winter_wheat', 'wet_rice'],
        day = ['01', '10', '11', '20', '21', '28', '29', '30', '31'],
        growing_season = ['1st_season_per_campaign', '2nd_season_per_campaign'],
        harvest_year = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        product_family = ['crop_productivity_indicators', 'evapotranspiration_indicators'],
        variable = ['actual_evaporation', 'potential_evaporation', 'crop_development_stage', 'total_above_ground_production', 'total_weight_storage_organs'],
        year = ['1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
    )

    @Collection.wrapper
    def download(cls, crop_type: OneOrMore[str], day: OneOrMore[str], growing_season: OneOrMore[str], harvest_year: str, month: OneOrMore[str], product_family: OneOrMore[str], variable: OneOrMore[str], year: str): 
        """
        Parameters
        ----------
        :param crop_type:
        :type crop_type: str

        **Valid values:**
        
        - maize

        
        - soybean

        
        - spring_wheat

        
        - winter_wheat

        
        - wet_rice

        ---

        :param day:
        :type day: str

        **Valid values:**
        
        - 01

        
        - 10

        
        - 11

        
        - 20

        
        - 21

        
        - 28

        
        - 29

        
        - 30

        
        - 31

        ---

        :param growing_season:
        :type growing_season: str

        **Valid values:**
        
        - 1st_season_per_campaign

        
        - 2nd_season_per_campaign

        ---

        :param harvest_year:
        :type harvest_year: str

        **Valid values:**
        
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

        :param product_family:
        :type product_family: str

        **Valid values:**
        
        - crop_productivity_indicators

        
        - evapotranspiration_indicators

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - actual_evaporation

        
        - potential_evaporation

        
        - crop_development_stage

        
        - total_above_ground_production

        
        - total_weight_storage_organs

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_agroproductivity_indicators(crop_type: OneOrMore[str], day: OneOrMore[str], growing_season: OneOrMore[str], harvest_year: str, month: OneOrMore[str], product_family: OneOrMore[str], variable: OneOrMore[str], year: str):
    return Collection_sis_agroproductivity_indicators.download(crop_type=crop_type, day=day, growing_season=growing_season, harvest_year=harvest_year, month=month, product_family=product_family, variable=variable, year=year)

