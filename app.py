from flask import Flask, render_template_string 
app = Flask(__name__)
@app.route("/")
def home():
	return """
Hello</br>
This is UZair DevOps Enthusiast</br>
learning day by day"""
if __name__ ==  "__main__":
	app.run(host="0.0.0.0", port=5000)

