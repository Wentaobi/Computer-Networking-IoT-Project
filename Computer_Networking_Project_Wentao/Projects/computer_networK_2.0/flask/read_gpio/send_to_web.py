from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO 
import requests
import time
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
pin = '2/3'
@app.route("/")
def readPin():
      key = "cbf17f7b412a0644"
      ApiUrl = \
	   "http://api.wunderground.com/api/" + key + "/forecast/q/MI/Detroit.json"

      r = requests.get(ApiUrl)
      forecast = r.json()

      #time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
      date= forecast['forecast']['txt_forecast']['forecastday'][0]['title']
      weather = forecast['forecast']['txt_forecast']['forecastday'][0]['icon']
      now = datetime.datetime.now()
      timeString = now.strftime("%Y-%m-%d %H:%M:%S")

      try:
            GPIO.setup(4, GPIO.IN)
            if GPIO.input(4) == 1:
               response = "BCM_gpio_2/3 is high!"
            else:
               response = "BCM_gpio_2/3 is low!"
      except:
               response = "There was an error reading pin 4"

      templateData = {
                  'time': timeString,
                  'title' : 'Status of Pin' + pin,
                  'response' : response,
		  'weather' : weather
                  }
      return render_template('read_pin.html', **templateData)
if __name__ == "__main__":
   app.run(port=8890, debug=True)





