import pandas as pd
import matplotlib.pyplot as plt


def close_vol(df):
    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
    ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)

    ax1.plot(df.index, df['CLOSE'])
    ax2.bar(df.index, df['VOL'])

    return plt.show()


def ema(df, short, long):
    emasused = [short, long]
    # calculate exponential moving average for different periods and add them to your dataframe
    for x in emasused:
        ema = x
        df["Ema_"+str(ema)] = round(df.loc[:, ['CLOSE']].ewm(span=ema, adjust=False).mean(),2)

    # plot stock close price, short, and long periods with line chart.
    df.plot(kind='line',
            y=['CLOSE', f'Ema_{short}', f'Ema_{long}'],
            color=['black', 'b', 'r'],
            figsize=(16, 6))

    return plt.show()


def sma(df, short, long):
    smasused = [short, long]
    # # calculate simple moving average for different periods and add them to your dataframe
    for x in smasused:
        sma = x
        df["Sma_"+str(sma)] = round(df.loc[:, ['CLOSE']].rolling(window=sma, min_periods=0).mean(), 2)

    # plot stock close price, short, and long periods with line chart.
    df.plot(kind='line',
            y=['CLOSE', f'Sma_{short}', f'Sma_{long}'],
            color=['black', 'b', 'r'],
            figsize=(16, 6))

    return plt.show()


def return_dev(df):
    close_px = df['CLOSE']
    rets = close_px / close_px.shift(1) - 1
    rets.plot(label='return')
    return plt.show()