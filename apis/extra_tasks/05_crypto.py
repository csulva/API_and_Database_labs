'''
http://docs.nomics.com/
Using the nomics API, repeatedly fetch the price of Bitcoin for a duration of 10 minutes.
Store each value in a dictionary that uses the time of query as a key.

After the script stopped running, determine programmatically at what query time the price
was the highest, and when the lowest.

HINTS:
- request an API key first and remember to include it in your queries
- the /prices endpoint of the nomics API can be used for achieving this task
- remember to use packages from the standard library, e.g. for time keeping and dates

BONUS: Explore the logging package for easier tracking

'''

import requests
import datetime
import time

#url = "https://api.nomics.com/v1/currencies?key=a2388e583fb00867472c69b07bb5a1fb9dc2966c&ids=BTC,ETH,XRP&attributes=id,name,logo_url"
url = "https://api.nomics.com/v1/currencies/ticker?key=a2388e583fb00867472c69b07bb5a1fb9dc2966c&ids=BTC,ETH,XRP&interval=1d,30d&convert=EUR&per-page=100&page=1"
response = requests.get(url)
response = response.json()

response = response[0]

saved_BTC_date = {}
ten_min = time.time() + 60 + 10

while time.time() < ten_min:
    #every ten seconds
    time.sleep(30)
    for key, value in response.items():
        if key == 'price':
            saved_BTC_date[str(datetime.datetime.now())] = value
            append = open('/Users/christophersulva/Desktop/API_project/API_Labs/python_apis_databases/apis/extra_tasks/Bitcoin_data.csv', 'w')
            append.write(f'{saved_BTC_date}')
            append.close()