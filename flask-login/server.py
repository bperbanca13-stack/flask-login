from flask import Flask, render_template, request, make_response, send_file
import os

app = Flask(__name__)

@app.route("/auth", methods=["POST"])
def auth():
    print(request.form.to_dict())
    return "ok"

@app.route("/")
def index():
    response = make_response(render_template("login.html"))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
