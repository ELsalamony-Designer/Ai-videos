from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # عشان نسمح للـ frontend يتواصل مع السيرفر

@app.route("/generate", methods=["POST"])
def generate_video():
    prompt = request.form["prompt"]
    image = request.files.get("image")

    # بدل الكود الجاي بكود حقيقي بيتعامل مع Runway أو Pika API
    # هنرجع لينك ثابت للفيديو كتجربة
    return jsonify({
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4"
    })

if __name__ == "__main__":
    app.run(debug=True)
