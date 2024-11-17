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

class Collection_insitu_gridded_observations_global_and_regional(Collection):
    collection_name = 'insitu-gridded-observations-global-and-regional'
    valid_values = dict(
        horizontal_aggregation = ['0_25_x_0_25', '0_2_x_0_2', '0_5_x_0_5', '1_x_1', '2_5_x_2_5', 'horizontal_average'],
        origin = ['berkearth', 'chirps', 'cmorph', 'cpc', 'cpc_conus', 'cru', 'gistemp', 'gpcc', 'imerg'],
        region = ['africa', 'conus', 'global', 'quasi_global'],
        statistic = ['maximum', 'minimum', 'mean'],
        time_aggregation = ['daily', 'monthly'],
        variable = ['temperature', 'temperature_anomaly', 'precipitation'],
        version = ['v1_0', 'v2020_0', 'v2020_0_v6_0_fg', 'v2_0', 'v4_0', 'v4_03', 'v6_0'],
        year = ['1750', '1751', '1752', '1753', '1754', '1755', '1756', '1757', '1758', '1759', '1760', '1761', '1762', '1763', '1764', '1765', '1766', '1767', '1768', '1769', '1770', '1771', '1772', '1773', '1774', '1775', '1776', '1777', '1778', '1779', '1780', '1781', '1782', '1783', '1784', '1785', '1786', '1787', '1788', '1789', '1790', '1791', '1792', '1793', '1794', '1795', '1796', '1797', '1798', '1799', '1800', '1801', '1802', '1803', '1804', '1805', '1806', '1807', '1808', '1809', '1810', '1811', '1812', '1813', '1814', '1815', '1816', '1817', '1818', '1819', '1820', '1821', '1822', '1823', '1824', '1825', '1826', '1827', '1828', '1829', '1830', '1831', '1832', '1833', '1834', '1835', '1836', '1837', '1838', '1839', '1840', '1841', '1842', '1843', '1844', '1845', '1846', '1847', '1848', '1849', '1850', '1851', '1852', '1853', '1854', '1855', '1856', '1857', '1858', '1859', '1860', '1861', '1862', '1863', '1864', '1865', '1866', '1867', '1868', '1869', '1870', '1871', '1872', '1873', '1874', '1875', '1876', '1877', '1878', '1879', '1880', '1881', '1882', '1883', '1884', '1885', '1886', '1887', '1888', '1889', '1890', '1891', '1892', '1893', '1894', '1895', '1896', '1897', '1898', '1899', '1900', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909', '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021'],
    )

    @Collection.wrapper
    def download(cls, horizontal_aggregation: OneOrMore[str], origin: str, region: str, statistic: OneOrMore[str], time_aggregation: str, variable: OneOrMore[str], version: OneOrMore[str], year: OneOrMore[str]): 
        """
        Parameters
        ----------
        :param horizontal_aggregation:
        :type horizontal_aggregation: str

        **Valid values:**
        
        - 0_25_x_0_25

        
        - 0_2_x_0_2

        
        - 0_5_x_0_5

        
        - 1_x_1

        
        - 2_5_x_2_5

        
        - horizontal_average

        ---

        :param origin:
        :type origin: str

        **Valid values:**
        
        - berkearth

        
        - chirps

        
        - cmorph

        
        - cpc

        
        - cpc_conus

        
        - cru

        
        - gistemp

        
        - gpcc

        
        - imerg

        ---

        :param region:
        :type region: str

        **Valid values:**
        
        - africa

        
        - conus

        
        - global

        
        - quasi_global

        ---

        :param statistic:
        :type statistic: str

        **Valid values:**
        
        - maximum

        
        - minimum

        
        - mean

        ---

        :param time_aggregation:
        :type time_aggregation: str

        **Valid values:**
        
        - daily

        
        - monthly

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - temperature

        
        - temperature_anomaly

        
        - precipitation

        ---

        :param version:
        :type version: str

        **Valid values:**
        
        - v1_0

        
        - v2020_0

        
        - v2020_0_v6_0_fg

        
        - v2_0

        
        - v4_0

        
        - v4_03

        
        - v6_0

        ---

        :param year:
        :type year: str

        **Valid values:**
        
        - 1750

        
        - 1751

        
        - 1752

        
        - 1753

        
        - 1754

        
        - 1755

        
        - 1756

        
        - 1757

        
        - 1758

        
        - 1759

        
        - 1760

        
        - 1761

        
        - 1762

        
        - 1763

        
        - 1764

        
        - 1765

        
        - 1766

        
        - 1767

        
        - 1768

        
        - 1769

        
        - 1770

        
        - 1771

        
        - 1772

        
        - 1773

        
        - 1774

        
        - 1775

        
        - 1776

        
        - 1777

        
        - 1778

        
        - 1779

        
        - 1780

        
        - 1781

        
        - 1782

        
        - 1783

        
        - 1784

        
        - 1785

        
        - 1786

        
        - 1787

        
        - 1788

        
        - 1789

        
        - 1790

        
        - 1791

        
        - 1792

        
        - 1793

        
        - 1794

        
        - 1795

        
        - 1796

        
        - 1797

        
        - 1798

        
        - 1799

        
        - 1800

        
        - 1801

        
        - 1802

        
        - 1803

        
        - 1804

        
        - 1805

        
        - 1806

        
        - 1807

        
        - 1808

        
        - 1809

        
        - 1810

        
        - 1811

        
        - 1812

        
        - 1813

        
        - 1814

        
        - 1815

        
        - 1816

        
        - 1817

        
        - 1818

        
        - 1819

        
        - 1820

        
        - 1821

        
        - 1822

        
        - 1823

        
        - 1824

        
        - 1825

        
        - 1826

        
        - 1827

        
        - 1828

        
        - 1829

        
        - 1830

        
        - 1831

        
        - 1832

        
        - 1833

        
        - 1834

        
        - 1835

        
        - 1836

        
        - 1837

        
        - 1838

        
        - 1839

        
        - 1840

        
        - 1841

        
        - 1842

        
        - 1843

        
        - 1844

        
        - 1845

        
        - 1846

        
        - 1847

        
        - 1848

        
        - 1849

        
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

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_insitu_gridded_observations_global_and_regional(horizontal_aggregation: OneOrMore[str], origin: str, region: str, statistic: OneOrMore[str], time_aggregation: str, variable: OneOrMore[str], version: OneOrMore[str], year: OneOrMore[str]):
    return Collection_insitu_gridded_observations_global_and_regional.download(horizontal_aggregation=horizontal_aggregation, origin=origin, region=region, statistic=statistic, time_aggregation=time_aggregation, variable=variable, version=version, year=year)

