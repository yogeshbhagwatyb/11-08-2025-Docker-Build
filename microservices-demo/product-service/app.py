from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify([
        {"id": 101, "name": "Laptop"},
        {"id": 102, "name": "Phone"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
