from flask import Flask, request, jsonify
from chatbot import handle_query

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("query")
    response = handle_query(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
