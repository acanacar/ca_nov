from pathlib import Path
import pandas as pd

import getpass
if getpass.getuser()=='a.acar':
    hist_store = str(
        r'C:\Users\a.acar\PycharmProjects\VaR\sources\hist_data.h5')
    hist_pkl = str(
            r'C:\Users\a.acar\PycharmProjects\VaR\sources\hist_data.pkl')
    hist_pkl_1m = str(
                r'C:\Users\a.acar\PycharmProjects\VaR\sources\hist_data_1m.pkl')

    hist_pkl_1h = str(r'C:\Users\a.acar\PycharmProjects\VaR\sources\hist_data_1h.pkl')

    VaR_png_output_path = str(r"C:\Users\a.acar\PycharmProjects\VaR\outputs")

if getpass.getuser()=='root':
    project_path = Path('/home/acanacar/Desktop/projects/pycharm/VaR')
    data_path = Path('/home/acanacar/Desktop/data/')

    bar_path = str(data_path / 'bar/')
    tickall_path = str(data_path / 'tickall.pkl')

    hist_store = str(
        '/home/acanacar/Desktop/projects/pycharm/VaR/sources/hist_data.h5')
    hist_pkl = str(
            '/home/acanacar/Desktop/projects/pycharm/VaR/sources/hist_data.pkl')
    hist_pkl_1m = str('/home/acanacar/Desktop/projects/pycharm/VaR/sources/hist_data_1m.pkl')
    hist_pkl_1h = str('/home/acanacar/Desktop/projects/pycharm/VaR/sources/hist_data_1h.pkl')

    VaR_png_output_path = str(project_path/'outputs/')


def Tickers():
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