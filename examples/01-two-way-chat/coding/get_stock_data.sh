# filename: get_stock_data.sh
sh -c "echo 'Downloading stock data...'
curl --silent https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=METADATA+inc.&outputsize=full&apikey=DUMMY_API_KEY &interval=daily > metadatadata.csv
echo 'Downloading TESLA data...'
curl  --silent https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&outputsize=full&apikey=DUMMY_API_KEY &interval=daily >> tesladata.csv
echo 'Done'
" > get_stock_data.sh

bash get_stock_data.sh