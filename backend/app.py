from flask_cors import CORS
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app)  # Allows requests from your React frontend

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    # Basic mock response
    reply = f"You said: {message}"

    return jsonify({"reply": reply})
if __name__ == "__main__":
    app.run(debug=True)
