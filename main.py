from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
""""""

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/forms")
def forms():
    return render_template("Forms.html")



""""""
if __name__=="__main__":
    app.run(debug=True)