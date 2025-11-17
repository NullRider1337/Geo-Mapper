from flask import Flask, render_template, request
from exif_utils import extract_gps

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    gps_data = None
    filename = None

    if request.method == "POST":
        image = request.files.get("image")

        if image:
            filename = image.filename
            gps_data = extract_gps(image)

    return render_template("index.html", gps_data=gps_data, filename=filename)


if __name__ == "__main__":
    app.run(debug=True)
