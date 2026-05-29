from flask import Flask, render_template
import psutil
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/metrics")
def metrics():
    cpu = int(psutil.cpu_percent(interval=1))
    memory = int(psutil.virtual_memory().percent)

    if os.name == "nt":
        disk = int(psutil.disk_usage("C:\\").percent)
    else:
        disk = int(psutil.disk_usage("/").percent)

    return render_template("metrics.html", cpu=cpu, memory=memory, disk=disk)

@app.route("/security")
def security():
    logs = [
        {"source": "pfSense Firewall", "event": "Blocked WAN connection attempt detected", "severity": "Warning"},
        {"source": "DMZ Network", "event": "DMZ traffic logging enabled and monitored", "severity": "Info"},
        {"source": "Suricata IDS/IPS", "event": "Suspicious TCP stream activity detected", "severity": "High"},
        {"source": "Azure Monitor", "event": "SuspiciousActivityAlert triggered and email notification sent", "severity": "High"}
    ]
    return render_template("security.html", logs=logs)

@app.route("/ids")
def ids():
    alerts = [
        {"interface": "WAN / DMZ", "protocol": "TCP", "source": "104.20.28.246", "destination": "192.168.122.245", "description": "SURICATA STREAM reassembly depth reached"},
        {"interface": "WAN / DMZ", "protocol": "TCP", "source": "193.0.14.129", "destination": "192.168.122.245", "description": "SURICATA STREAM FIN recv but no session"}
    ]
    return render_template("ids.html", alerts=alerts)

@app.route("/azure")
def azure():
    return render_template("azure.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)