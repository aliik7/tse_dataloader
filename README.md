# tse_dataloader

tse_dataloader is a python package for extracting stock historical data from Tehran Stock Exchange.

- [x] Extract data and load them in `Pandas` data frame
- [x] Calculate SMA and EMA
- [x] Create line charts with `matplotlib`

## Install:
```
pip install tse_dataloader
```

## Functions:

- Loading data with get_data(ticker)

```
>>> from tse_dataloader import download
>>> MELT= download.get_data('وبملت')
>>> MELT

	TICKER	FIRST	HIGH	LOW	CLOSE	VALUE	VOL	OPENINT	PER	OPEN	LAST	date_shamsi
Date												
2009-02-18	S*Mellat.Bank	1050.0	1050.0	1050.0	1050.0	347393807250	330851245	800	D	1000.0	1050.0	1387/11/30
2009-02-21	S*Mellat.Bank	1051.0	1076.0	1042.0	1050.0	352194689892	335334212	6457	D	1050.0	1057.0	1387/12/03
2009-02-22	S*Mellat.Bank	1065.0	1074.0	1055.0	1065.0	8981292784	8435464	603	D	1050.0	1055.0	1387/12/04
2009-02-23	S*Mellat.Bank	1066.0	1067.0	1059.0	1061.0	9090532333	8570222	937	D	1065.0	1060.0	1387/12/05
2009-02-25	S*Mellat.Bank	1061.0	1064.0	1050.0	1058.0	7863032258	7434309	616	D	1061.0	1060.0	1387/12/07
...	...	...	...	...	...	...	...	...	...	...	...	...
2020-06-30	S*Mellat.Bank	25900.0	26170.0	25000.0	26110.0	3841979105490	147166333	38097	D	24930.0	26170.0	1399/04/10
2020-07-01	S*Mellat.Bank	27350.0	27370.0	26500.0	26940.0	4531902777600	168219804	56583	D	26110.0	26690.0	1399/04/11
2020-07-04	S*Mellat.Bank	26940.0	27000.0	25600.0	25760.0	5958222319060	231283534	65195	D	26940.0	25600.0	1399/04/14
2020-07-05	S*Mellat.Bank	24560.0	27040.0	24480.0	25670.0	5766735541640	224649840	65488	D	25760.0	25860.0	1399/04/15
2020-07-06	S*Mellat.Bank	26200.0	26950.0	26200.0	26860.0	6812022224090	253566140	52045	D	25670.0	26950.0	1399/04/16
2377 rows × 12 columns
```
- Plot Close price and Volume line chart with close_vol()

```
>>> from tse_dataloader import analysis
>>> analysis.close_vol(MELT)

# to create a chart without gaps you can use df.reset_index()
>>> analysis.close_vol(MELT.reset_index())
```
- Calculate short and long term Simple Moving Average, Exponential Moving Average, add them to your data frame and plot chart line with SMA()

```
>>> from tse_dataloader import analysis
>>> analysis.sma(MELT, 20, 50)
>>> analysis.ema(MELT, 20, 50)
```

- For your convenience, I create a list of tickers and attached it to the package to load data faster. In order to update your symbol list, you can use stock_list.update(). it takes a few minutes to update data from tsetmc. 

```
>>> import tse_dataloader
>>> stock_list.update()

Database has updated!
```

- In some cases, if you couldn't find your specific symbol in the list, you can add it to the list manually with the stock_list.add() function.

```
>>> import tse_dataloader
>>> stock_list.add(2400322364771558, 'شستا')


Symbol added to the list!
```
you can find every symbol's code at the end of its URL:
http://www.tsetmc.com/loader.aspx?ParTree=151311&i=**2400322364771558**




Thanks to [tehran-stock](https://github.com/ghodsizadeh/tehran-stocks)
