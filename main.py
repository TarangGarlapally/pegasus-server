from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def welcome():
    return "Hello"

@app.route('/home', methods=['GET'])
def home():
    return {"message": "hi"}

if __name__ == "__main__":
    app.run()
