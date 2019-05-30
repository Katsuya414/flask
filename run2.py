import requests, bs4
from flask import Flask, render_template, request
import json
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello World"
    return name

@app.route('/form')
def form():
   return render_template('form.html')


@app.route("/index", methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
       result = request.form.get('Name')
       brands = {}
       res = requests.get('https://folio-sec.com/theme/' + "%s" % result)
       res.raise_for_status()
       soup = bs4.BeautifulSoup(res.text, "html.parser")
       elems = soup.find_all(class_="TextMainLink__textMainLink--38tbe Instruments__instrumentName--4jzC9 gtm-stock-detail")
       for index2, elem in enumerate(elems):
        brands[index2]=elem.text

       b=brands
    return render_template('index.html', message=b)

if __name__ == "__main__":
    app.run()
