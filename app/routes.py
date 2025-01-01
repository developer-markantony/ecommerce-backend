from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products')
def get_products():
    return jsonify({"products": ["item1", "item2", "item3"]})

if __name__ == "__main__":
    app.run(debug=True)

