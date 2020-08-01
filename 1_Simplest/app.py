from flask import Flask, render_template, send_from_directory, request, redirect, flash
import secrets
import pickle

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)

# Let's load in the model we used before
with open('model.pkl', 'rb') as f:
    clf = pickle.load(f)


@app.route("/", methods=["GET", "POST"])
def index():
    index = "index.html"
    pred = "Enter your iris sepal and petal specs below."
    if request.method == "GET":
        return render_template(index, pred=pred)
    else:
        print(list(request.form.keys()))
        try:
            # Get the things from the form, make them floats (they start as strings)
            responses = [request.form.get(item) for item in ["sepal_len", "sepal_wid", "petal_len", "petal_wid"]]
            print(responses)
            inputs = [[float(item) for item in responses]]
            print(inputs)

            pred = f"We think your flower is a {clf.predict(inputs)[0]}!"
        except Exception as e:
            print(e)
            flash("Invalid inputs! Try again.", "warn")
            redirect(index)

    return render_template(index, pred=pred)


@app.route("/js/<path:path>")
def send_js(path):
    return send_from_directory("static/js", path)


@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory("static/css", path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
