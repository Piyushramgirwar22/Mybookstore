from flask import Flask, render_template, url_for, redirect,request
import pandas as pd
from data_dao import book_range

########### Data Work ###############
df = pd.read_csv(r'C:\Users\lenovo\OneDrive\Desktop\mybooks project\app_folder\mybooks_project_data.csv')
########### flask app ##############

from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    data = df.T.to_dict().values()
    return render_template('new.html', data = data)

@app.route('/home')
def Home():
    data = df.T.to_dict().values()
    return render_template('new.html', data = data)


@app.route('/low')
def low():
    data = book_range('low range', df)
    return render_template('new.html', data = data)

@app.route('/medium')
def medium():
    data = book_range('mid range', df)
    return render_template('new.html', data = data)

@app.route('/high')
def high():
    data = book_range('high range', df)
    return render_template('new.html', data = data)




if __name__ == '__main__':
    app.run(debug = True)