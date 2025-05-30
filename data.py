# data.py
from threading import Lock

# Holds product monitoring state
monitored_products = {}
lock = Lock()