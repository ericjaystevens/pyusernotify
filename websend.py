#!flask/bin/python
from flask import Flask
import pyUserMessage as pum

app = Flask(__name__)

@app.route('/send/<string:message>/<string:toEmail>', methods=['GET'])
def index(message, toEmail):

    msg = pum.pyUserMessage(message)
    msg.send(toEmail)
    return 'OK'
    
if __name__ == '__main__':
    app.run(debug=True)