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

class Collection_satellite_lake_water_level(Collection):
    collection_name = 'satellite-lake-water-level'
    valid_values = dict(
        lake = ['albert', 'bagre', 'bankim', 'bogoria', 'fitri', 'kainji', 'kossou', 'kyoga', 'lagdo', 'langano', 'mangbeto', 'nasser', 'roseires', 'shiroro', 'tana', 'tchad', 'turkana', 'volta', 'ziway', 'bangweulu', 'cahora_bassa', 'chishi', 'edouard', 'george', 'hendrik_verwoerd', 'kabele', 'kabwe', 'kariba', 'kisale', 'kinkony', 'kivu', 'mai_ndombe', 'malawi', 'mweru', 'naivasha', 'rukwa', 'tanganika', 'tumba', 'victoria', 'zimbambo', 'sulunga', 'amadjuak', 'athabasca', 'aylmer', 'baker', 'bienville', 'birch', 'big_trout', 'bluenose', 'caribou', 'cedar', 'claire', 'dubawnt', 'faber', 'gods', 'grande_trois', 'greatslave', 'hottah', 'iliamna', 'kamilukuak', 'kasba', 'manitoba', 'nueltin', 'old_wives', 'swan', 'williston', 'winnipegosis', 'winnipeg', 'atlin', 'churchill', 'teshekpuk', 'black', 'tustumena', 'cormorant', 'cumberland', 'american_falls', 'cayuga', 'cerros_colorados', 'chapala', 'des_bois', 'erie', 'fort_peck', 'hinojo', 'huron', 'michigan', 'mono', 'mullet', 'nezahualcoyoti', 'nicaragua', 'nipissing', 'oahe', 'ontario', 'saint_jean', 'sakakawea', 'san_martin', 'superior', 'tres_marias', 'viedma', 'walker', 'yellowstone', 'okeechobee', 'argentino', 'balbina', 'chocon', 'cienagachilloa', 'cochrane', 'fontana', 'guri', 'lagoa_dos_patos', 'ranco', 'sobradino', 'titicaca', 'todos_los_santos', 'valencia', 'brokopondo', 'cabaliana', 'cardiel', 'biarini', 'coari', 'azhibeksorkoli', 'hovsgol', 'tengiz', 'uvs', 'alakol', 'aydarkul', 'bairab', 'balkhash', 'beas', 'beysehir', 'biylikol', 'bugunskoye', 'caspian', 'chardarya', 'chagbo_co', 'chatyrkol', 'egridir', 'gyeze_caka', 'habbaniyah', 'hamrin', 'hawizeh_marshes', 'heishi_beihu', 'issykkul', 'iznik', 'jayakwadi', 'kairakum', 'kamyshlybas', 'kapchagayskoye', 'kara_bogaz_gol', 'karasor', 'langa_co', 'lumajangdong_co', 'luotuo', 'memar', 'mingacevir', 'mossoul', 'saksak', 'sarykamish', 'sasykkol', 'saysan', 'sevan', 'srisailam', 'tharthar', 'toktogul', 'van', 'achit', 'aqqikol_hu', 'ayakkum', 'bosten', 'cuodarima', 'dagze_co', 'dalai', 'danau_towuti', 'danausingkarak', 'dangqiong', 'dogaicoring_q', 'dorgon', 'dorsoidong_co', 'garkung', 'gyaring_co', 'hala', 'har', 'hoh_xil_hu', 'hongze', 'hulun', 'hyargas', 'kokonor', 'lano', 'lixiodain_co', 'migriggyangzham', 'namco', 'namngum', 'ngangze', 'ngoring_co', 'serbug', 'soungari', 'tangra_yumco', 'telashi', 'telmen', 'tonle_sap', 'ulan_ul', 'ulungur', 'xiangyang', 'yamzho_yumco', 'zhari_namco', 'zhelin', 'ziling', 'zonag', 'chlew_larn', 'bay', 'boontsagaan', 'xuelian_hu', 'barkal', 'orba_co', 'baikal', 'baunt', 'bratskoye', 'chlya', 'chukochye', 'illmen', 'inarinjarvi', 'krasnoyarskoye', 'kubenskoye', 'kulundinskoye', 'kumskoye', 'kuybyshevskoye', 'ladoga', 'novosibirskoye', 'onega', 'peipus', 'pyaozero', 'rybinskoye', 'saratovskoye', 'segozerskoye', 'tchany', 'teletskoye', 'umbozero', 'vanajanselka', 'vanerm', 'vattern', 'zeyskoye', 'bolmen', 'bodensee', 'khanka', 'kremenchutska', 'leman', 'prespa', 'tsimlyanskoye', 'rosarito', 'corangamite', 'pukaki', 'argyle'],
        region = ['oceania', 'southern_america', 'northern_africa', 'southern_africa', 'northern_north_america', 'southern_north_america', 'northern_europe', 'southern_europe', 'northern_asia', 'southwestern_asia', 'southeastern_asia'],
        variable = ['all'],
    )

    @Collection.wrapper
    def download(cls, lake: OneOrMore[str], region: OneOrMore[str], variable: str = 'all'): 
        """
        Parameters
        ----------
        :param lake:
        :type lake: str

        **Valid values:**
        
        - albert

        
        - bagre

        
        - bankim

        
        - bogoria

        
        - fitri

        
        - kainji

        
        - kossou

        
        - kyoga

        
        - lagdo

        
        - langano

        
        - mangbeto

        
        - nasser

        
        - roseires

        
        - shiroro

        
        - tana

        
        - tchad

        
        - turkana

        
        - volta

        
        - ziway

        
        - bangweulu

        
        - cahora_bassa

        
        - chishi

        
        - edouard

        
        - george

        
        - hendrik_verwoerd

        
        - kabele

        
        - kabwe

        
        - kariba

        
        - kisale

        
        - kinkony

        
        - kivu

        
        - mai_ndombe

        
        - malawi

        
        - mweru

        
        - naivasha

        
        - rukwa

        
        - tanganika

        
        - tumba

        
        - victoria

        
        - zimbambo

        
        - sulunga

        
        - amadjuak

        
        - athabasca

        
        - aylmer

        
        - baker

        
        - bienville

        
        - birch

        
        - big_trout

        
        - bluenose

        
        - caribou

        
        - cedar

        
        - claire

        
        - dubawnt

        
        - faber

        
        - gods

        
        - grande_trois

        
        - greatslave

        
        - hottah

        
        - iliamna

        
        - kamilukuak

        
        - kasba

        
        - manitoba

        
        - nueltin

        
        - old_wives

        
        - swan

        
        - williston

        
        - winnipegosis

        
        - winnipeg

        
        - atlin

        
        - churchill

        
        - teshekpuk

        
        - black

        
        - tustumena

        
        - cormorant

        
        - cumberland

        
        - american_falls

        
        - cayuga

        
        - cerros_colorados

        
        - chapala

        
        - des_bois

        
        - erie

        
        - fort_peck

        
        - hinojo

        
        - huron

        
        - michigan

        
        - mono

        
        - mullet

        
        - nezahualcoyoti

        
        - nicaragua

        
        - nipissing

        
        - oahe

        
        - ontario

        
        - saint_jean

        
        - sakakawea

        
        - san_martin

        
        - superior

        
        - tres_marias

        
        - viedma

        
        - walker

        
        - yellowstone

        
        - okeechobee

        
        - argentino

        
        - balbina

        
        - chocon

        
        - cienagachilloa

        
        - cochrane

        
        - fontana

        
        - guri

        
        - lagoa_dos_patos

        
        - ranco

        
        - sobradino

        
        - titicaca

        
        - todos_los_santos

        
        - valencia

        
        - brokopondo

        
        - cabaliana

        
        - cardiel

        
        - biarini

        
        - coari

        
        - azhibeksorkoli

        
        - hovsgol

        
        - tengiz

        
        - uvs

        
        - alakol

        
        - aydarkul

        
        - bairab

        
        - balkhash

        
        - beas

        
        - beysehir

        
        - biylikol

        
        - bugunskoye

        
        - caspian

        
        - chardarya

        
        - chagbo_co

        
        - chatyrkol

        
        - egridir

        
        - gyeze_caka

        
        - habbaniyah

        
        - hamrin

        
        - hawizeh_marshes

        
        - heishi_beihu

        
        - issykkul

        
        - iznik

        
        - jayakwadi

        
        - kairakum

        
        - kamyshlybas

        
        - kapchagayskoye

        
        - kara_bogaz_gol

        
        - karasor

        
        - langa_co

        
        - lumajangdong_co

        
        - luotuo

        
        - memar

        
        - mingacevir

        
        - mossoul

        
        - saksak

        
        - sarykamish

        
        - sasykkol

        
        - saysan

        
        - sevan

        
        - srisailam

        
        - tharthar

        
        - toktogul

        
        - van

        
        - achit

        
        - aqqikol_hu

        
        - ayakkum

        
        - bosten

        
        - cuodarima

        
        - dagze_co

        
        - dalai

        
        - danau_towuti

        
        - danausingkarak

        
        - dangqiong

        
        - dogaicoring_q

        
        - dorgon

        
        - dorsoidong_co

        
        - garkung

        
        - gyaring_co

        
        - hala

        
        - har

        
        - hoh_xil_hu

        
        - hongze

        
        - hulun

        
        - hyargas

        
        - kokonor

        
        - lano

        
        - lixiodain_co

        
        - migriggyangzham

        
        - namco

        
        - namngum

        
        - ngangze

        
        - ngoring_co

        
        - serbug

        
        - soungari

        
        - tangra_yumco

        
        - telashi

        
        - telmen

        
        - tonle_sap

        
        - ulan_ul

        
        - ulungur

        
        - xiangyang

        
        - yamzho_yumco

        
        - zhari_namco

        
        - zhelin

        
        - ziling

        
        - zonag

        
        - chlew_larn

        
        - bay

        
        - boontsagaan

        
        - xuelian_hu

        
        - barkal

        
        - orba_co

        
        - baikal

        
        - baunt

        
        - bratskoye

        
        - chlya

        
        - chukochye

        
        - illmen

        
        - inarinjarvi

        
        - krasnoyarskoye

        
        - kubenskoye

        
        - kulundinskoye

        
        - kumskoye

        
        - kuybyshevskoye

        
        - ladoga

        
        - novosibirskoye

        
        - onega

        
        - peipus

        
        - pyaozero

        
        - rybinskoye

        
        - saratovskoye

        
        - segozerskoye

        
        - tchany

        
        - teletskoye

        
        - umbozero

        
        - vanajanselka

        
        - vanerm

        
        - vattern

        
        - zeyskoye

        
        - bolmen

        
        - bodensee

        
        - khanka

        
        - kremenchutska

        
        - leman

        
        - prespa

        
        - tsimlyanskoye

        
        - rosarito

        
        - corangamite

        
        - pukaki

        
        - argyle

        ---

        :param region:
        :type region: str

        **Valid values:**
        
        - oceania

        
        - southern_america

        
        - northern_africa

        
        - southern_africa

        
        - northern_north_america

        
        - southern_north_america

        
        - northern_europe

        
        - southern_europe

        
        - northern_asia

        
        - southwestern_asia

        
        - southeastern_asia

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - all

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_satellite_lake_water_level(lake: OneOrMore[str], region: OneOrMore[str], variable: str = 'all'):
    return Collection_satellite_lake_water_level.download(lake=lake, region=region, variable=variable)

