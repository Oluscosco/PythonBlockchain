from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from email.message import EmailMessage
import ssl
import smtplib
Alert
emailPass = ""
email = ""
emailReceiver = ""
subject="Transaction Alert"

app = Flask(__name__)
CORS(app)

@app.route('/streams', methods=["POST"])
def streams():

    details = request.json
    print(details)

    return jsonify(success=True)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)
