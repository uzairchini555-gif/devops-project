from flask import Flask 
app = Flask(__name__)
@app.route("/")
def home():
	return """Q. What is linux?<br>
A. A Linux is an open-source OS (operating system) widely used in servers and cloud environment."""

app.run(host="0.0.0.0", port=5000)
 
@app.route("/health")
daf health():
	return "OK", 200
