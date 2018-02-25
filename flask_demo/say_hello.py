from flask import Flask

app = Flask(__name__)
@app.route("/SayHello/<user_name>")

def home(user_name):
    return "Hello " + user_name
app.run()
