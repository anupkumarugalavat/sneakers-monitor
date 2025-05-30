# app.py
from flask import Flask, render_template, request, redirect
from data import monitored_products, lock
from monitor import start_monitor

app = Flask(__name__)
start_monitor()

@app.route('/')
def dashboard():
    with lock:
        products = monitored_products.copy()
    return render_template("dashboard.html", products=products)

@app.route('/add', methods=['POST'])
def add_product():
    product_id = request.form['product_id']
    sizes = request.form['sizes'].split(',')
    with lock:
        monitored_products[product_id] = {
            "sizes": [s.strip() for s in sizes],
            "status": "Checking...",
            "available_sizes": []
        }
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)