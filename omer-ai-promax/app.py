from flask import Flask, render_template, request, redirect, session, jsonify

app = Flask(__name__)
app.secret_key = "omer_ai"

@app.route("/")
def home():
    if "user" in session:
        return render_template("index.html", user=session["user"])
    return redirect("/login")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        session["user"] = request.form["username"]
        return redirect("/")
    return render_template("login.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        return redirect("/login")
    return render_template("register.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json["message"]
    return jsonify({"reply": "ÖMER AI: " + msg})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
