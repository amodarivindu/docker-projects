from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
 return "Hello, Docker!  I am amoda rivindu please let us know if you need any help with docker or anything else."
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=5000)
