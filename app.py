from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ----------------------------
# PRESET QUESTIONS & ANSWERS
# WITH TRANSLATIONS
# ----------------------------

qa_data = {
    "Where is the Library?": {
        "en": "The Library is in Block A, 2nd Floor.",
        "ml": "ലൈബ്രറി ബ്ലോക്ക് A യുടെ 2ാം നിലയിലാണ്.",
        "hi": "पुस्तकालय ब्लॉक A की दूसरी मंजिल पर है।"
    },
    "Where is the Office?": {
        "en": "The Office is in Block B, Ground Floor.",
        "ml": "ഓഫീസ് ബ്ലോക്ക് B യുടെ ഗ്രൗണ്ട് ഫ്ലോറിലാണ്.",
        "hi": "कार्यालय ब्लॉक B के ग्राउंड फ्लोर पर है।"
    },
    "What is College Timing?": {
        "en": "College timing is 9:00 AM to 4:00 PM.",
        "ml": "കോളേജ് സമയം രാവിലെ 9 മുതൽ വൈകിട്ട് 4 വരെ ആണ്.",
        "hi": "कॉलेज का समय सुबह 9 से शाम 4 बजे तक है।"
    }
}

# ----------------------------
@app.route("/")
def home():
    return render_template("index.html", questions=list(qa_data.keys()))

# ----------------------------
@app.route("/get_answer", methods=["POST"])
def get_answer():
    selected_question = request.json["question"]
    language = request.json["language"]

    answer = qa_data.get(selected_question, {}).get(language, "Answer not available.")

    return jsonify({
        "question": selected_question,
        "answer": answer
    })

# ----------------------------
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

