import requests as rq
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def student():
	return render_template("input.html")

@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form['Name']
		EXCHANGE="NYSE"
		symbol='MSFT'	
		API_KEY='EKCQJHJUDHO3W4XR'
		result=rq.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+EXCHANGE+':'+result+'&apikey='+API_KEY)
		if(result.status_code==200):
			r=result.json()
			daily=r['Time Series (Daily)']
	return render_template("price.html",result = daily)

if __name__ == '__main__':
	app.run(debug = True)




