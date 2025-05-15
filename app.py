from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
	return "Bonjour a tous, ceci est une simple application conteneuriser avec Docker par NKOT!"
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000)
