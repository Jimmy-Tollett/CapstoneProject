from flask import Flask, jsonify

app = Flask(__name__) # Start web app

# Check that she's actually alive
@app.get("/healthz")
def health():
    return jsonify(ok=True)

@app.get("/")
def root():
    return jsonify(service="smo-api", status="up")

app.run(host="0.0.0.0", port=8000, debug=True)