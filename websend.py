#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/send/<string:message>/<string:toEmail>', methods=['GET'])
def index(message, toEmail):
    return "Send message:" + message + " to " + toEmail

if __name__ == '__main__':
    app.run(debug=True)