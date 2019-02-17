from flask import Flask, render_template
import test

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/spit")
def get_data():
    return test.spitJson()


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)