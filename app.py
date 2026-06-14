from analyzer import analyze_log
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["logfile"]

    filepath = f"logs/{file.filename}"

    file.save(filepath)

    result = analyze_log(filepath)

    return render_template(
    "result.html",
    data=result
)


if __name__ == "__main__":
    app.run(debug=True)