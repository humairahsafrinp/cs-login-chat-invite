from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        return redirect(url_for("chat", username=name))
    return render_template("login.html")

@app.route("/chat/<username>")
def chat(username):
    return render_template("chat.html", username=username)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

