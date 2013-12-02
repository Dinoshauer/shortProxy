from flask import Flask, redirect, url_for
from api.views import api

app = Flask(__name__)
app.register_blueprint(api)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
