#!/usr/bin/python3

import json
import csv
from os import error
from flask import Flask, render_template, request

app = Flask(_name_)

def read_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = jsoan.load(f)
        
        return data

def read_from_csv(file_path):
    data_list = []
    with open(file_path, 'r', encoding='utf-8') as f:
        data = csv.DictReader(f)
        
        for item in data:
            item['id'] = int(item['id'])
            item['price'] = float(item['price'])
            
            data_list.append(item)

    return data_list


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r', encoding="utf-8") as f:
            data = json.load(f)
            items = data.get('items', [])

    except FileNotFoundError:
        items = []

    return render_template('items.html', items=items)

if __name__ == "__main__":
    app.run(debug=True, port=5000)