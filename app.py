from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"student_number": "200573379"})

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()

    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName")

    if intent_name == "Equipment Availability":
        response_text = "We have treadmills, dumbbells, squat racks, and more. Availability may vary during peak hours."
    else:
        response_text = "I am not sure how to respond to that."

    return jsonify({"fulfillmentText": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
