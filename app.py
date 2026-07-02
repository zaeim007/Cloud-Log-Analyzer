import os

from analyzer import analyze_log
from flask import Flask, render_template, request

app = Flask(__name__)

# Upload folder configuration
UPLOAD_FOLDER = "logs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["logfile"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(filepath)

    result = analyze_log(filepath)

    return render_template(
        "result.html",
        data=result
    )


if __name__ == "__main__":
    app.run(debug=True)