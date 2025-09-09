from flask import Flask, request, jsonify
from model import similarity_score

app = Flask(__name__)

@app.route("/similarity", methods=["POST"])
def get_similarity():
    data = request.get_json()

    text1 = data.get("text1", "")
    text2 = data.get("text2", "")

    score = similarity_score(text1, text2)

    return jsonify({"similarity score": round(score, 1)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
