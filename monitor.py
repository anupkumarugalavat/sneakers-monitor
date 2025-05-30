# monitor.py
import requests, time, threading
from data import monitored_products, lock

BEARER_TOKEN = 'your_access_token_here'
HEADERS = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "User-Agent": "Nike/79.0 iOS/14.4",
    "Accept": "application/json"
}

def fetch_availability(product_id):
    url = f"https://api.nike.com/deliver/available_skus/v1/{product_id}"
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            return None
        return response.json()
    except Exception as e:
        print(f"Error fetching {product_id}: {e}")
        return None

def monitor_loop():
    while True:
        with lock:
            for product_id, product in monitored_products.items():
                skus = fetch_availability(product_id)
                if not skus:
                    product["status"] = "Error"
                    continue

                available_sizes = [
                    sku["size"] for sku in skus
                    if sku["size"] in product["sizes"] and sku["available"]
                ]
                product["status"] = "Available" if available_sizes else "Unavailable"
                product["available_sizes"] = available_sizes
        time.sleep(60)

def start_monitor():
    thread = threading.Thread(target=monitor_loop)
    thread.daemon = True
    thread.start()
