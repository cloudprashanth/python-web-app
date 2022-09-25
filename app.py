from flask import Flask
from datetime import datetime
import time
app = Flask(__name__)
ts = time.time()

@app.route('/')
def hello_world():
    return 'Hello, Docker!'
@app.route('/app')
def app_1():
    return str(time.time())
@app.route("/time")
def home():
    date = datetime.now()
    return str(date)

if __name__ == "__main__":
    app.run(debug=True)
