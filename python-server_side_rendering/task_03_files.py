#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/products')
def products():

    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':

        try:
            with open('products.json', 'r') as file:
                read_data = json.load(file)
        except Exception as e:
            print(f"Error reading JSON file: {e}")
            read_data = []
    
    elif source == 'csv':

        try:
            with open('products.csv', 'r') as csvf:
                csvReader = csv.DictReader(csvf)
                read_data = list(csvReader)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            read_data = []

    else:
        err_msg = 'Wrong source. source must be json or csv.'
        return render_template('product_display.html', err_msg=err_msg)

    if product_id:
        products = [product for product in read_data if str(product.get('id')) == str(product_id)]
        if not products:
            print('products: {}'.format(products))
            err_msg = 'Product not found'
            return render_template('product_display.html', err_msg=err_msg)

        return render_template('product_display.html', products=products)

    else:
        return render_template('product_display.html', products=read_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
