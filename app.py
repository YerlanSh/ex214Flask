from flask import Flask
from OpenSSL import SSL

app = Flask(__name__)

context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file("server.key")
context.use_certificate_file("server.crt")

@app.route('/')
def index():
    return 'Hello, this is a secure server!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=context, threaded=True, debug=True)
