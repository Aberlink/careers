from flask import Flask, render_template

app = Flask(__name__)
adress = "127.0.0.1"
port = 5000

@app.route("/")
def hellow():
    return render_template('home.html')

app.run(host=adress, port=port, debug=True)