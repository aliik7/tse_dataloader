# tse_dataloader

tse_dataloader is a python package for extracting stock historical data from Tehran Stock Exchange.

[![Generic badge](https://img.shields.io/badge/pypi-v0.1.2-<COLOR>.svg)](https://shields.io/) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
- [x] Extract data and load them in `Pandas` data frame
- [x] Calculate SMA and EMA
- [x] Create line charts with `matplotlib`

## Install:
```
pip install tse_dataloader
```

## Functions:

- Loading data with **get_data(ticker)** or **getcode_data(code)**

```
>>> from tse_dataloader import download
>>> MELT= download.get_data('وبملت')
>>> print(MELT)

                   TICKER    FIRST     HIGH  ...     OPEN     LAST  date_shamsi
Date                                         ...                               
2009-02-18  S*Mellat.Bank   1050.0   1050.0  ...   1000.0   1050.0   1387/11/30
2009-02-21  S*Mellat.Bank   1051.0   1076.0  ...   1050.0   1057.0   1387/12/03
2009-02-22  S*Mellat.Bank   1065.0   1074.0  ...   1050.0   1055.0   1387/12/04
2009-02-23  S*Mellat.Bank   1066.0   1067.0  ...   1065.0   1060.0   1387/12/05
2009-02-25  S*Mellat.Bank   1061.0   1064.0  ...   1061.0   1060.0   1387/12/07
...                   ...      ...      ...  ...      ...      ...          ...
2020-07-01  S*Mellat.Bank  27350.0  27370.0  ...  26110.0  26690.0   1399/04/11
2020-07-04  S*Mellat.Bank  26940.0  27000.0  ...  26940.0  25600.0   1399/04/14
2020-07-05  S*Mellat.Bank  24560.0  27040.0  ...  25760.0  25860.0   1399/04/15
2020-07-06  S*Mellat.Bank  26200.0  26950.0  ...  25670.0  26950.0   1399/04/16
2020-07-07  S*Mellat.Bank  27320.0  28200.0  ...  26860.0  26040.0   1399/04/17

[2374 rows x 12 columns]

>>> MELT= download.getcode_data(778253364357513)
```
- Plot Close price and Volume line chart with **close_vol()**

```
>>> from tse_dataloader import analysis
>>> analysis.close_vol(MELT)

# to create a chart without gaps you can use df.reset_index()
>>> analysis.close_vol(MELT.reset_index())
```
- Calculate short and long term Simple Moving Average, Exponential Moving Average, add them to your data frame and plot chart line with **sma()** and **ema()**

```
>>> from tse_dataloader import analysis
>>> analysis.sma(MELT, 20, 50)
>>> analysis.ema(MELT, 20, 50)
```

- For your convenience, I create a list of tickers and attached it to the package to load data faster. In order to update your symbol list, you can use **stock_list.update()**. it takes a few minutes to update data from tsetmc. 

```
>>> import tse_dataloader
>>> stock_list.update()

Database has updated!
```

- In some cases, if you couldn't find your specific symbol in the list, you can add it to the list manually with the **stock_list.add()** function.

```
>>> import tse_dataloader
>>> stock_list.add(2400322364771558, 'شستا')


Symbol added to the list!
```
You can find every symbol's code at the end of its URL:   
<a href="http://www.tsetmc.com/loader.aspx?ParTree=151311&i=2400322364771558">http://www.tsetmc.com/loader.aspx?ParTree=151311&i=</strong>2400322364771558</strong></a>



Thanks to [tehran-stock](https://github.com/ghodsizadeh/tehran-stocks)
