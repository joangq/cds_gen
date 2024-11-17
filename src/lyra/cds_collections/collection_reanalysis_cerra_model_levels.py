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

class Collection_reanalysis_cerra_model_levels(Collection):
    collection_name = 'reanalysis-cerra-model-levels'
    valid_values = dict(
        data_type = ['ensemble_members', 'reanalysis'],
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        model_level = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        time = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00'],
        variable = ['specific_humidity', 'temperature', 'u_component_of_wind', 'v_component_of_wind'],
        year = ['1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021'],
        data_format = ['grib', 'netcdf'],
    )

    @Collection.wrapper
    def download(cls, data_type: OneOrMore[str], day: OneOrMore[str], model_level: OneOrMore[str], month: OneOrMore[str], time: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], data_format: str = 'grib'): 
        """
        Parameters
        ----------
        :param data_type:
        :type data_type: str

        **Valid values:**
        
        - ensemble_members

        
        - reanalysis

        ---

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

        :param model_level:
        :type model_level: str

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

        
        - 32

        
        - 33

        
        - 34

        
        - 35

        
        - 36

        
        - 37

        
        - 38

        
        - 39

        
        - 40

        
        - 41

        
        - 42

        
        - 43

        
        - 44

        
        - 45

        
        - 46

        
        - 47

        
        - 48

        
        - 49

        
        - 50

        
        - 51

        
        - 52

        
        - 53

        
        - 54

        
        - 55

        
        - 56

        
        - 57

        
        - 58

        
        - 59

        
        - 60

        
        - 61

        
        - 62

        
        - 63

        
        - 64

        
        - 65

        
        - 66

        
        - 67

        
        - 68

        
        - 69

        
        - 70

        
        - 71

        
        - 72

        
        - 73

        
        - 74

        
        - 75

        
        - 76

        
        - 77

        
        - 78

        
        - 79

        
        - 80

        
        - 81

        
        - 82

        
        - 83

        
        - 84

        
        - 85

        
        - 86

        
        - 87

        
        - 88

        
        - 89

        
        - 90

        
        - 91

        
        - 92

        
        - 93

        
        - 94

        
        - 95

        
        - 96

        
        - 97

        
        - 98

        
        - 99

        
        - 100

        
        - 101

        
        - 102

        
        - 103

        
        - 104

        
        - 105

        
        - 106

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
        
        - specific_humidity

        
        - temperature

        
        - u_component_of_wind

        
        - v_component_of_wind

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

def download_reanalysis_cerra_model_levels(data_type: OneOrMore[str], day: OneOrMore[str], model_level: OneOrMore[str], month: OneOrMore[str], time: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], data_format: str = 'grib'):
    return Collection_reanalysis_cerra_model_levels.download(data_type=data_type, day=day, model_level=model_level, month=month, time=time, variable=variable, year=year, data_format=data_format)

