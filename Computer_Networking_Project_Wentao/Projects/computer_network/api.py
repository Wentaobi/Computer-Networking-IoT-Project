import requests
import time

key = "cbf17f7b412a0644"
ApiUrl = \
   "http://api.wunderground.com/api/" + key + "/forecast/q/MI/Detroit.json"

r = requests.get(ApiUrl)
forecast = r.json()

# print(forecast['forecast']['txt_forecast']['forecastday'][0]['fcttext_metric'])
#print('\t time:', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '\n\t',
#     'date:', forecast['forecast']['txt_forecast']['forecastday'][0]['title'], '\n\t',
#     'weather:', forecast['forecast']['txt_forecast']['forecastday'][0]['icon'])

time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
date= forecast['forecast']['txt_forecast']['forecastday'][0]['title']
weather = forecast['forecast']['txt_forecast']['forecastday'][0]['icon']

print(time)
print(date) 
print(weather)
