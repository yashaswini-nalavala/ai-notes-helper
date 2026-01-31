from flask import Flask, render_template, request

app = Flask(__name__)

def simulated_ai_summary(text):
    return f"""
Summary:
- This is a simulated AI-generated summary.
- It demonstrates AI workflow without an API key.
- Key idea extracted from input:
  "{text[:80]}..."
- Designed for first-year hackathon demo.
"""

@app.route("/", methods=["GET", "POST"])
def home():
    summary = ""
    if request.method == "POST":
        user_text = request.form["text"]
        summary = simulated_ai_summary(user_text)
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
