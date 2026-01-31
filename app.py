from flask import Flask, request, jsonify, render_template
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json(force=True)
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Preprocess
    text = text.replace('\n', ' ')
    sentences = [s.strip() for s in text.split('.') if len(s.strip()) > 15]

    if len(sentences) <= 2:
        return jsonify({"summary": ["• " + s + "." for s in sentences]})

    # Stop words
    stop_words = {
        "the","is","a","an","and","or","to","in","of","for","on","with",
        "as","by","this","that","are","was","were","be","has","have",
        "it","its","from","at"
    }

    # Word frequency
    word_freq = {}
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    for word in words:
        if word not in stop_words:
            word_freq[word] = word_freq.get(word, 0) + 1

    # Score sentences
    scored = []
    for s in sentences:
        score = sum(word_freq.get(w.lower().strip(string.punctuation), 0) for w in s.split())
        scored.append((s, score))

    # Average score → threshold
    avg_score = sum(score for _, score in scored) / len(scored)

    # Select ONLY important sentences
    important = [s for s, score in scored if score >= avg_score]

    # Limit bullet points (AI-like)
    important = important[:5]

    # AI-style rewrite (light)
    bullets = []
    for s in important:
        s = s.capitalize()
        if not s.endswith('.'):
            s += '.'
        bullets.append("• " + s)

    return jsonify({"summary": bullets})

if __name__ == '__main__':
    app.run(debug=True)

