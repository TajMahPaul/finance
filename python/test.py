import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates as mdates
from matplotlib import ticker as mticker
from matplotlib.finance import candlestick_ohlc
import datetime as dt

headers = {
    'Content-Type': 'application/json'
}
requestResponse = requests.get("https://api.tiingo.com/tiingo/fx/audusd/prices?startDate=2019-06-30&resampleFreq=5min&token=99b007dd46f3ced1f0362cd3a52383c1865c0b10", headers=headers)
df = pd.DataFrame(requestResponse.json())
print (df)
# df.plot(x='Quantity', y='Rate')