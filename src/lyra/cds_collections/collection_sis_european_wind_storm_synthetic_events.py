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

class Collection_sis_european_wind_storm_synthetic_events(Collection):
    collection_name = 'sis-european-wind-storm-synthetic-events'
    valid_values = dict(
        month = ['01', '02', '03', '04', '05', '09', '10', '11', '12'],
        variable = ['wind_speed_of_gusts'],
        version_id = ['synthetic_set_1_2', 'synthetic_set_2_0', 'synthetic_set_3_0'],
        year = ['1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011'],
    )

    @Collection.wrapper
    def download(cls, month: OneOrMore[str], variable: OneOrMore[str], version_id: OneOrMore[str], year: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param month:
        :type month: str

        **Valid values:**
        
        - 01

        
        - 02

        
        - 03

        
        - 04

        
        - 05

        
        - 09

        
        - 10

        
        - 11

        
        - 12

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - wind_speed_of_gusts

        ---

        :param version_id:
        :type version_id: str

        **Valid values:**
        
        - synthetic_set_1_2

        
        - synthetic_set_2_0

        
        - synthetic_set_3_0

        ---

        :param year:
        :type year: str

        **Valid values:**
        
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

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_sis_european_wind_storm_synthetic_events(month: OneOrMore[str], variable: OneOrMore[str], version_id: OneOrMore[str], year: OneOrMore[str]):
    return Collection_sis_european_wind_storm_synthetic_events.download(month=month, variable=variable, version_id=version_id, year=year)

