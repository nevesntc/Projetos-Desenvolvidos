from Flask import flask
import webbrowser 

app = Flask(__name__)
@app.route("/")

def site():
    