from flask import Flask, render_template_string 
app = Flask(__name__)
@app.route("/")
def home():
	return render_template_string("""
	<!DOCTYPE html>
	<html>
	<head>
		<title>DevOps CI/CD App</title>
		<style>
			body {
				margin: 0;
				font-family: Arial,sans-serif;
				background: linear-gradient(135deg, #0f172a, #1e293b);
				color: white;
				text-align: center;
			}
			.container {
				padding-top: 120px;
			}
			h1 {
				font-size: 48px;
				margin-bottom: 10px;
			}
			p {
				font-size: 18px;
				color: #cbd5e1;
			}
			.card {
				margin: 40px auto;
				width: 60%;
				padding: 20px;
				background: rgba(255,255,255,0.05);
				border-radius: 12px;
				box-shadow: 0 0 20px rgba(0,0,0,0.4);
			}
			.badge {
				display: inline-block;
				padding: 8px 14px;
				background: @22c55e;
				border-radius: 20px;
				margin-top: 20px;
				font-size: 14px;
			}
			footer {
				margin-top: 80px;
				font-size: 12px;
				color: #94a3b8;
			}
		</style>
	</head>
	<body>
		<div class="container">
			<h1>🚀 DevOps CI/CD Pipeline</h1>
			<p>Deployed on AWS EKS using Docker, Kubernetes & Github Actions</p>
			<div class="card">
				<h2>System Status</h2>
				<p>Application is running successfully on Kubernetes cluster</p>
				<div class="badge">✔ Deployment Active</div>
			</div>
			<footer>
				Built by Uzair Munir | Powered by AWS EKS + Docker + CI/CD
			</footer>
		</div>
	</body>
	</html>
	""")
if __name__ ==  "__main__":
	app.run(host="0.0.0.0", port=5000)

