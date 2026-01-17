from flask import Flask, render_template

app = Flask(__name__)

subjects = ['maths','social','english','population']

@app.route("/")
def index():
    return render_template('index.html',name='tikaram',subjects = subjects)

@app.route("/about")
def about():
    return "my name is tikaram"

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)