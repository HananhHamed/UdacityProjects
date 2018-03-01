from flask import Flask, render_template
import models, stores

app = Flask(__name__)
post_store = stores.PostStore()

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts = post_store.get_all())

app.run()
