from flask import Flask, render_template, send_from_directory, request, redirect, flash

app = Flask(__name__)


def predict_death(age: int):
    if age > 80:
        return False
    else:
        return True


@app.route("/", methods=["GET", "POST"])
def index():
    pred = "Enter your age."
    if request.method == "GET":
        return render_template("index.html", pred=pred)
    else:
        print(request.form)
        try:
            response = int(request.form.get('text'))
            pred = "You're probably good" if predict_death(response) else "...Take some time off..."
        except:
            redirect("index.html")
    return render_template("index.html", pred=pred)

@app.route("/js/<path:path>")
def send_js(path):
    return send_from_directory("static/js", path)


@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory("static/css", path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
