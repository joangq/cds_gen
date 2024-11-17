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

class Collection_derived_gridded_glacier_mass_change(Collection):
    collection_name = 'derived-gridded-glacier-mass-change'
    valid_values = dict(
        hydrological_year = ['1975_76', '1976_77', '1977_78', '1978_79', '1979_80', '1980_81', '1981_82', '1982_83', '1983_84', '1984_85', '1985_86', '1986_87', '1987_88', '1988_89', '1989_90', '1990_91', '1991_92', '1992_93', '1993_94', '1994_95', '1995_96', '1996_97', '1997_98', '1998_99', '1999_00', '2000_01', '2001_02', '2002_03', '2003_04', '2004_05', '2005_06', '2006_07', '2007_08', '2008_09', '2009_10', '2010_11', '2011_12', '2012_13', '2013_14', '2014_15', '2015_16', '2016_17', '2017_18', '2018_19', '2019_20', '2020_21', '2021_22'],
        product_version = ['wgms_fog_2022_09', 'wgms_fog_2023_09'],
        variable = ['glacier_mass_change'],
    )

    @Collection.wrapper
    def download(cls, hydrological_year: OneOrMore[str], product_version: str = 'wgms_fog_2023_09', variable: str = 'glacier_mass_change'): 
        """
        Parameters
        ----------
        :param hydrological_year:
        :type hydrological_year: str

        **Valid values:**
        
        - 1975_76

        
        - 1976_77

        
        - 1977_78

        
        - 1978_79

        
        - 1979_80

        
        - 1980_81

        
        - 1981_82

        
        - 1982_83

        
        - 1983_84

        
        - 1984_85

        
        - 1985_86

        
        - 1986_87

        
        - 1987_88

        
        - 1988_89

        
        - 1989_90

        
        - 1990_91

        
        - 1991_92

        
        - 1992_93

        
        - 1993_94

        
        - 1994_95

        
        - 1995_96

        
        - 1996_97

        
        - 1997_98

        
        - 1998_99

        
        - 1999_00

        
        - 2000_01

        
        - 2001_02

        
        - 2002_03

        
        - 2003_04

        
        - 2004_05

        
        - 2005_06

        
        - 2006_07

        
        - 2007_08

        
        - 2008_09

        
        - 2009_10

        
        - 2010_11

        
        - 2011_12

        
        - 2012_13

        
        - 2013_14

        
        - 2014_15

        
        - 2015_16

        
        - 2016_17

        
        - 2017_18

        
        - 2018_19

        
        - 2019_20

        
        - 2020_21

        
        - 2021_22

        ---

        :param product_version:
        :type product_version: str

        **Valid values:**
        
        - wgms_fog_2022_09

        
        - wgms_fog_2023_09

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - glacier_mass_change

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_derived_gridded_glacier_mass_change(hydrological_year: OneOrMore[str], product_version: str = 'wgms_fog_2023_09', variable: str = 'glacier_mass_change'):
    return Collection_derived_gridded_glacier_mass_change.download(hydrological_year=hydrological_year, product_version=product_version, variable=variable)

