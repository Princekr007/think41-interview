from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import handle_query

app = Flask(__name__)
CORS(app)  # ✅ This enables Cross-Origin Resource Sharing for all routes

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("query")
    response = handle_query(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
