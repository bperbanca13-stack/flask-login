from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/auth", methods=["POST"])
def auth():
    data = request.form.to_dict()
    print(data)  # stampa in console su Railway
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run()
