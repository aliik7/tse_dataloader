import pandas as pd
from jdatetime import date as jdate
import requests
import os
import io


def convert_to_shamsi(date):
    date = str(date)
    date_shamsi = jdate.fromgregorian(
        day=int(date[-2:]), month=int(date[4:6]), year=int(date[:4])
    ).strftime("%Y/%m/%d")
    return date_shamsi


def get_data(ticker):
    try:
        # open data file in the package
        tse_dir = os.path.dirname(__file__)
        dfm = pd.read_csv(f'{tse_dir}/data/TSE_Symbol_List.csv')
        # find the ticker ins code for generating the url
        code = dfm.loc[dfm['Symbol'] == ticker, 'Code'].iat[0]

        # create url for given ticker code and sending a request for data
        url = "http://www.tsetmc.com/tsev2/data/Export-txt.aspx?t=i&a=1&b=0&i={}"
        response = requests.get(url.format(code))
        file_object = io.StringIO(response.content.decode('utf-8'))
        # read downloaded data with pandas
        df = pd.read_csv(file_object)

        # changing columns' names and date formant from int to date
        df.columns = ['TICKER', 'DTYYYYMMDD', 'FIRST', 'HIGH', 'LOW', 'CLOSE',
                      'VALUE', 'VOL', 'OPENINT', 'PER', 'OPEN', 'LAST']
        df['Date'] = pd.to_datetime(df['DTYYYYMMDD'].astype(str), format='%Y%m%d')
        df["date_shamsi"] = df["DTYYYYMMDD"].apply(convert_to_shamsi)
        df.set_index('Date', inplace=True)
        df.drop(columns=["DTYYYYMMDD"], inplace=True)
        df.sort_index(inplace=True)

        return df

    except IndexError:
        return 'No match'


def getcode_data(code):
    try:
        # create url for given ticker code and sending a request for data
        url = "http://www.tsetmc.com/tsev2/data/Export-txt.aspx?t=i&a=1&b=0&i={}"
        response = requests.get(url.format(code))
        file_object = io.StringIO(response.content.decode('utf-8'))
        # read downloaded data with pandas
        df = pd.read_csv(file_object)

        # changing columns' names and date formant from int to date
        df.columns = ['TICKER', 'DTYYYYMMDD', 'FIRST', 'HIGH', 'LOW', 'CLOSE',
                      'VALUE', 'VOL', 'OPENINT', 'PER', 'OPEN', 'LAST']
        df['Date'] = pd.to_datetime(df['DTYYYYMMDD'].astype(str), format='%Y%m%d')
        df["date_shamsi"] = df["DTYYYYMMDD"].apply(convert_to_shamsi)
        df.set_index('Date', inplace=True)
        df.drop(columns=["DTYYYYMMDD"], inplace=True)
        df.sort_index(inplace=True)

        return df

    except IndexError:
        return 'No file found!'

