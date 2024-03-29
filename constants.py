from pathlib import Path
import pandas as pd

import getpass

if getpass.getuser() == 'a.acar':
    project_path = Path(r'C:\Users\a.acar\Desktop\PycharmProjects\ca_nov')
    fintable_path = project_path / Path('fintable')
    hist_store = str(
        r'C:\Users\a.acar\Desktop\PycharmProjects\VaR\sources\hist_data.h5')
    tahvil_pkl = str(
        r'C:\Users\a.acar\Desktop\PycharmProjects\ca_nov\sources\tahvil2_5_10.pkl')
    hist_pkl = str(
        r'C:\Users\a.acar\Desktop\PycharmProjects\VaR\sources\hist_data.pkl')
    hdf5_store = str(
        r'C:\Users\a.acar\Desktop\PycharmProjects\ca_nov\sources\hist_data.h5')
    hist_pkl_1m = str(
        r'C:\Users\a.acar\Desktop\PycharmProjects\VaR\sources\hist_data_1m.pkl')

    hist_pkl_1h = str(r'C:\Users\a.acar\Desktop\PycharmProjects\VaR\sources\hist_data_1h.pkl')

    VaR_png_output_path = str(r"C:\Users\a.acar\Desktop\PycharmProjects\VaR\outputs")
    mali_tablolar_path = r'C:\Users\a.acar\PycharmProjects\runfintble\excels\{}_Finansal_Tablolar_Bilanco.xlsx'

if getpass.getuser() == 'root':
    project_path = Path('/home/acanacar/Desktop/projects/pycharm/VaR')
    data_path = Path('/home/acanacar/Desktop/data/')

    bar_path = str(data_path / 'bar/')
    tickall_path = str(data_path / 'tickall.pkl')
    hdf5_store = str(
        '/home/acanacar/PycharmProjects/ca_nov/sources/hist_data.h5')
    hist_store = str(
        '/home/acanacar/Desktop/projects/pycharm/VaR/sources/hist_data.h5')
    hist_pkl = str(
        '/home/acanacar/Desktop/projects/pycharm/VaR/sources/hist_data.pkl')
    hist_pkl_1m = str('/home/acanacar/Desktop/projects/pycharm/VaR/sources/hist_data_1m.pkl')
    hist_pkl_1h = str('/home/acanacar/Desktop/projects/pycharm/VaR/sources/hist_data_1h.pkl')

    VaR_png_output_path = str(project_path / 'outputs/')


def Security_Tickers():
    tickers = [
        'EURUSD=X', 'EURTRY=X', 'TRY=X',
        'XU100.IS',
        'AKBNK.IS',
        'ARCLK.IS',
        'ASELS.IS',
        'BIMAS.IS',
        'DOHOL.IS',
        'EKGYO.IS',
        'EREGL.IS',
        'FROTO.IS',
        'GARAN.IS',
        'HALKB.IS',
        'ISCTR.IS',
        'KCHOL.IS',
        'KOZAA.IS',
        'KOZAL.IS',
        'KRDMD.IS',
        'PETKM.IS',
        'PGSUS.IS',
        'SAHOL.IS',
        'SISE.IS',
        'SODA.IS',
        'TAVHL.IS',
        'TCELL.IS',
        'THYAO.IS',
        'TKFEN.IS',
        'TOASO.IS',
        'TTKOM.IS',
        'TUPRS.IS',
        'VAKBN.IS',
        'YKBNK.IS']
    return tickers


def Vix_Tickers():
    Vix = ['VXX', 'UVXY', 'SVXY', 'BZ=F', 'GC=F', '^VIX']
    return Vix


def Bonds_Tickers():
    Bonds = ['^FVX', '^TNX']
    return Bonds


def Tr_Tahvil_Tickers():
    Tahvil_Tr = ['tahvil2y', 'tahvil5y', 'tahvil10y']
    return Tahvil_Tr
