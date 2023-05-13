import subprocess
import platform
from flask import Flask, request, jsonify

# Install Flask package
subprocess.run(["pip", "install", "flask"])
# Install and configure Squid proxy
def install_squid():
    if platform.system() == 'Windows':
        subprocess.run(["choco", "install", "-y", "squid"])
    elif platform.system() == 'Linux':
        subprocess.run(["sudo", "apt-get", "update"])
        subprocess.run(["sudo", "apt-get", "install", "-y", "squid"])

def configure_squid(config):
    if platform.system() == 'Windows':
        with open("C:\\squid\\squid.conf", "w") as f:
            f.write(config)
    elif platform.system() == 'Linux':
        with open("/etc/squid/squid.conf", "w") as f:
            f.write(config)

# Agent REST API
app = Flask(__name__)

@app.route('/configure', methods=['POST'])
def configure_proxy():
    config = request.form.get('config')
    configure_squid(config)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    install_squid()
    configure_squid("x")
    app.run(host='0.0.0.0', port=5001)