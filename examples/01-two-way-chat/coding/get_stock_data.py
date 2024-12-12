# filename: get_stock_data.py
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key='DUMMY_API_KEY', output_format='pandas')

meta_data, _ = ts.get_daily_adjusted(symbol='META',outputsize='full')
tesla_data, _ = ts.get_daily_adjusted(symbol='TSLA',outputsize='full')

# Save data to CSV files
meta_data.to_csv('metadatadata.csv')
tesla_data.to_csv('tesladata.csv')