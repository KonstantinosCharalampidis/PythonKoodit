from flask import Flask, jsonify

app = Flask(__name__)
AIRPORTS = {
    "EFHK": {"ICAO": "EFHK", "Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EGLL": {"ICAO": "EGLL", "Name": "London Heathrow Airport", "Location": "London"},
}

@app.route("/airport/<icao_code>")
def airport_info(icao_code):
    icao_code = icao_code.upper()
    airport = AIRPORTS.get(icao_code)

    if airport is None:
        return jsonify({"error": "Airport not found"}), 404

    return jsonify(airport)

if __name__ == "__main__":
    app.run(debug=True)