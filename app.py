from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Personalized quotes for staff
STAFF_QUOTES = {
    "maidhili": "Your dedication and gentle guidance have shaped our confidence and character.",
    "kamakshi": "Your wisdom and discipline inspired us to strive for excellence every day.",
    "radhika": "Your encouragement and clarity made learning meaningful and memorable.",
    "aishwariya": "Your passion for teaching motivated us to explore beyond the syllabus.",
    "sudha": "Your patience and constant support helped us grow both academically and personally.",
    "pandi": "Your practical guidance and real-world insights prepared us for future challenges."
}

DEFAULT_QUOTE = "Your guidance has shaped our journey and inspired us deeply."

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name").strip()
        title = request.form.get("title")

        key_name = name.lower()
        quote = STAFF_QUOTES.get(key_name, DEFAULT_QUOTE)

        return redirect(url_for(
            "chat",
            username=name,
            title=title,
            quote=quote
        ))

    return render_template("login.html")

@app.route("/chat/<username>/<title>/<path:quote>")
def chat(username, title, quote):
    fullname = f"{username} {title}"
    return render_template(
        "chat.html",
        fullname=fullname,
        quote=quote
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
