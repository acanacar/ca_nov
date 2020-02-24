def carior(dv, kvb):
    '''
    TOPLAM VARLIKLAR - TOPLAM ÖZKAYNAKLAR
    '''
    return dv / kvb


def bovor(tv, to):
    '''
    TOPLAM VARLIKLAR - TOPLAM ÖZKAYNAKLAR
    '''
    return tv - to


def boovor(ty, to):
    '''
    TOPLAM VARLIKLAR - TOPLAM ÖZKAYNAKLAR
    '''
    return ty - to


def lior(dv, stok, kvb):
    return (dv - stok) / kvb


def enterprise_value():
    pass


def akdor(hasilat, tv):
    '''
    HASILAT /TOPLAM VARLIKLAR
    '''
    return hasilat / tv


def ebit(dkar, dvg, evg, fgid, fgel):
    """
    'DÖNEM KARI (ZARARI)',
    'Dönem Vergi (Gideri) Geliri',
    'Ertelenmiş Vergi (Gideri) Geliri',
    'Finansman Giderleri'
    'Finansman Gelirleri'
    """
    nvg = dvg + evg
    nfg = fgid - fgel
    return dkar + nfg + nvg


def ebitda(ebit, amortisman):
    """
    :param ebit: Vergi oncesi kar
    :param amortisman: 'Amortisman ve İtfa Gideri İle İlgili Düzeltmeler'
    """
    return ebit + amortisman


def ebitdam(ebitda, hasilat):
    """
    :param ebitda:Faiz, Vergi, Amortisman Öncesi Kar
    :param hasilat:HASILAT
    """
    return ebitda / hasilat


def eps_growth():
    pass


def gross_margin(smm, has):
    """
    :param smm: Satılan Malın Maliyeti
    :param has: Net Ciro
    """
    return 1 - (smm / has)


def net_margin(dkar, has):
    """
    :param dkar: Donem Kari
    :param has: Net Ciro
    """
    return dkar / has


def interest_burden(dkar, dvg, evg, ebit):
    """
    :param dkar: Donem Kari
    :param dvg: 'Dönem Vergi (Gideri) Geliri',
    :param evg: 'Ertelenmiş Vergi (Gideri) Geliri',
    :param ebit: Vergi oncesi kar
    :return:
    """
    return dkar + dvg + evg / ebit


def bdor(ebit, nfg):
    """
    :param ebit:Vergi oncesi kar
    :param nfg: net faiz geliri
    """
    return ebit / (ebit - nfg)


def net_income_growth(dkar, odkar):
    """
    :param dkar:Dönem Karı
    :param odkar:Bir Önceki Dönem Karı
    """
    return dkar / odkar


def pay_out_ratio():
    pass


def roas(dkar, tv):
    """
    :param dkar: Dönem Karı
    :param tv: toplam varliklar
    """
    return dkar / tv


def roeq(dkar, to):
    """
    :param dkar: Dönem Karı
    :param to: toplam ozvarliklar
    """
    return dkar / to


def rosa(dkar, sg):
    """
    :param dkar: Dönem Karı
    :param has: net ciro
    """
    return dkar / sg


def current_ratio(dd, kvb):
    """
    :param dd:donen degerler
    :param kvb: kisa vadeli borclar
    """
    return dd / kvb


def acid_test_ratio(dd, stok, kvb):
    """
    :param dd:donen degerler
    :param stok: stoklar
    :param kvb: kisa vadeli borclar
    """
    return (dd - stok) / kvb


def atr(sg, tk):
    return sg / tk


def grmar(sm, sg):
    return sm / sg
def roa(dkar,tk):
    return dkar/tk

def price_to_book_ratio():
    pass


def market_cap():
    pass


def price_earning_ratio():
    pass


def enterprise_value_over_ebit():
    pass
