from flask import Flask 
app = Flask(__name__)
@app.route("/")
def home():
	return """Q. What is linux?<br>
A. A Linux is an open-source OS (operating system) widely used in servers and cloud environment."""
 
@app.route("/health")
def health():
	return "OK", 200
@app.route("/ready")
def ready():
	return jsonify({
		"status": "ready"}), 200
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)

