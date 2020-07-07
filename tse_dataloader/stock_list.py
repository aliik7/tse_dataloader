import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


def update():
    """
    necessary data is attached into the package data file, so you can use them without
    running this function because it could take a few minute to update the main csv file.
    The main csv file contains symbol names and their code to generate url for downloading
    historical data. Over time this list on the tsetmc.com website would change and you can
    update your list with this function.
    """
    main_df = pd.DataFrame()
    # list of all pages that we should grab stock information from them and insert in our file
    pages = ['0', 'آ', 'ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض',
             'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی']

    # load all pages of symbols and insert data into dataframe
    for page in pages:

        url = f'http://www.tsetmc.com/Loader.aspx?ParTree=111C1416&firstChar={page}'
        r = requests.get(url)

        # web scraping with BeautifulSoup
        soup = BeautifulSoup(r.content, 'html.parser')
        # specify table in html page and table rows
        table = soup.find(id='tblToGrid')
        rows = table.find_all('tr')

        # find and insert each cell into a table
        table = []
        t = 0
        for tr in rows:
            td = tr.find_all('td')
            t += 1
            name = [i.text for i in td]
            table.append(name)

        # convert table to dataframe and insert headers
        df = pd.DataFrame(table)
        # take the data less the header row
        df = df[1:]
        df.columns = ['Symbol_Code', 'Group', 'Industries_Group', 'Table', 'En_Symbol', 'EN_name', 'Symbol1', 'Name1']

        # append each page of table to the main dataframe
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.append(df, ignore_index=True)

    # split name and symbol columns contents to separate columns
    new = main_df["Name1"].str.split(",", n=1, expand=True)
    main_df["Code"] = new[0]
    main_df["Name"] = new[1]

    new1 = main_df["Symbol1"].str.split(",", n=1, expand=True)
    main_df["a"] = new1[0]
    main_df["Symbol"] = new1[1]

    # drop redundant columns
    main_df.drop(columns=["Name1", 'a', "Symbol1"], inplace=True)

    # save main dataframe into CSV file
    tse_dir = os.path.dirname(__file__)
    path = f'{tse_dir}/data/TSE_Symbol_List.csv'
    main_df.to_csv(path, encoding='utf-8', index=False)

    print('Database has updated!')
    return main_df


def add(code, symbol):
    """
    tsetms website may update the symbol list with delay and if you want to load your new added stock
    with this package, you can simply add your specific symbol to the list with this function.
    """
    # finding file path in the package
    tse_dir = os.path.dirname(__file__)
    # open main csv file and add a row
    dfm = pd.read_csv(f'{tse_dir}/data/TSE_Symbol_List.csv')
    new_row = {'Code': code, 'Symbol': symbol}
    dfm = dfm.append(new_row, ignore_index=True)
    # replace new file with old file in the package
    path = f'{tse_dir}/data/TSE_Symbol_List.csv'
    dfm.to_csv(path, encoding='utf-8', index=False)

    return print('Symbol added to the list!')