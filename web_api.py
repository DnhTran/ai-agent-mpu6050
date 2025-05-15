from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to AI Agent API"}), 200

@app.route('/state')
def get_state():
    # Trả dữ liệu trạng thái ở đây
    return jsonify({"state": "OK", "confidence": 0.99})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
