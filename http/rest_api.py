from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # 👈 QUAN TRỌNG

@app.route("/api/status")
def status():
    return jsonify({
        "service": "Network Suite",
        "status": "ok"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
