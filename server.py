from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/youtube")
def youtube():
    URL = 'http://kworb.net/youtube'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    tbl =soup.find("table",{"id":"youtuberealtime"})

    df = pd.read_html(str(tbl))[0]
    parsed = df.to_dict('records')

    return jsonify(parsed)


@app.route("/spotifyartist")
def spotifyartist():
    URL = 'http://kworb.net/spotify'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    tbl =soup.find("table",{"id":"artisttable"})

    df = pd.read_html(str(tbl))[0]
    parsed = df.to_dict('records')

    return jsonify(parsed)

"""
@app.route("/itunes")
def itunes():
    URL = 'http://kworb.net/pop'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    tbl =soup.find("table", {"class":"sortable popbars"})

    df = pd.read_html(str(tbl))[0]
    parsed = df.to_dict('records')
    print(parsed)
    return jsonify(parsed)
"""

if __name__ == "__main__":
    app.run(debug=True)