from flask import Flask
from werkzeug.serving import make_ssl_devcert
import os

app = Flask(__name__)

def generate_ssl_certificate(cert_file, key_file):
    make_ssl_devcert(os.path.join(os.getcwd(), cert_file), host='localhost')

if __name__ == "__main__":
    cert_filename = "server.crt"
    key_filename = "server.key"

    generate_ssl_certificate(cert_filename, key_filename)

    print(f"SSL certificate and key generated: {cert_filename}, {key_filename}")
