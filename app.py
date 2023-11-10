from flask import Flask, request, jsonify

app = Flask(__name__)

survey_responses = []
def calculate_average(scores):
    return sum(scores) / len(scores) if len(scores) > 0 else 0

@app.route('/survey', methods=['POST'])
def submit_survey():
    data = request.get_json()

    if 'score' in data:
        score = int(data['score'])
        survey_responses.append({'score': score})
        return jsonify({"message": "Umfrageantwort erfolgreich hinzugefügt."}), 201
    else:
        return jsonify({"error": "Ungültige Anfrage. 'score' fehlt."}), 400

@app.route('/results', methods=['GET'])
def get_results():
    if not survey_responses:
        return jsonify({"message": "Keine Umfrageantworten vorhanden."}), 404

    average_score = calculate_average(response['score'] for response in survey_responses)
    return jsonify({"average_score": average_score, "survey_responses": survey_responses}), 200

if __name__ == '__main__':
    app.run(debug=True)


