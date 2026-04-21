from flask import Flask 
app = Flask(__name__)
@app.route("/")
def home():
	return """This is Uzair, DevOps Enthusiast</br>
Learning day by day</br>
One Step ahead</br>
Today I learned how to add reverse proxy and add domain to the app."""
 
@app.route("/health")
def health():
	return "OK", 200
@app.route("/ready")
def ready():
	return jsonify({
		"status": "ready"}), 200
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)

