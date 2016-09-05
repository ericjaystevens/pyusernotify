#!flask/bin/python
from flask import Flask
import pyUserMessages as pums

app = Flask(__name__)

@app.route('/send/<string:message>/<string:toEmail>', methods=['GET'])
def index(message, toEmail):

    msgs = pums.pyUserMessages()
    msg = msgs.get(message)
    msg.send(toEmail)
    return 'OK'
    
if __name__ == '__main__':
    app.run(debug=True)