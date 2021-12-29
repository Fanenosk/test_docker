import requests
from flask import Flask
app = Flask(__name__)


@app.route("/")
def quote_upper():
    return requests.get('http://172.17.0.1:5000/').text.upper()


if __name__ == '__main__':
    # quote = get_quote()
    app.run(host='0.0.0.0', port=5001)
    # print(quote)