from auth import get_quote
from flask import Flask
app = Flask(__name__)


@app.route("/", methods=['GET'])
def quote():
    # return jsonify({"quote":get_quote()})
    print(get_quote())
    return get_quote()


if __name__ == '__main__':
    # quote = get_quote()
    app.run(host='0.0.0.0', port=5000)
    # print(quote)

