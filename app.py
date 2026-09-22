import os
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
  return (
      "Mona AI Agent is Live! Server is running and ready to create content."
  )


@app.route("/chat", methods=["POST"])
def chat():
  data = request.json
  user_message = data.get("message", "")

  # Yahan aap apna custom logic ya local AI integration likh sakte hain
  ai_response = (
      f"Mona received your message: '{user_message}'. Processing locally..."
  )

  return jsonify({"response": ai_response})


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 10000))
  app.run(host="0.0.0.0", port=port)
