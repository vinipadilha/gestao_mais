from flask import Flask

app = Flask(__name__)

from routes import *

if __name__ == "__main__":
    app.run(debug=True, port=5001)
    # app.run()