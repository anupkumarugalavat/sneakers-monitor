simple SNKRS monitoring dashboard that tracks multiple products and shows available sizes in real-time. I’ll walk you through building a web-based dashboard using:

✅ Stack:
Python (Flask): backend for the API and server

HTML + JavaScript (AJAX): frontend dashboard UI

Bootstrap: for simple responsive styling

📦 Features:
Monitors multiple SNKRS SKUs

Auto-refreshes size availability every few seconds

Optional: Discord alerts

Clean web interface


snkrs_monitor/
├── app.py
├── monitor.py
├── templates/
│   └── dashboard.html
├── static/
│   └── style.css (optional)
└── requirements.txt

Install with:
pip install -r requirements.txt



✅ Run It
python app.py


Then open http://localhost:5000 in your browser.