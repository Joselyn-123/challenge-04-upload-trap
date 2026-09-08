from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Keep the flag outside the public upload directory
FLAG = "whitesec{Upl0ad_V4lid4t10n!_M1st4k3#2026}"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file selected"

    file = request.files["file"]

    if file.filename == "":
        return "No file selected"

    filename = secure_filename(file.filename)

    # Deliberately weak validation:
    # The server checks only the filename extension.
    if not filename.endswith(".txt"):
        return "Only .txt files are allowed"

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    # Read the uploaded content
    with open(filepath, "r", errors="ignore") as f:
        content = f.read()

    # Intended challenge condition
    if content.strip() == "CTF-ACCESS-2026":
        return f"""
        <h1>🎉 Flag Found!</h1>
        <p>{FLAG}</p>
        """

    return f"""
    <h2>File uploaded successfully!</h2>
    <p>Filename: {filename}</p>
    <p>Content:</p>
    <pre>{content}</pre>
    <p>Something is still missing...</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)