from flask import Blueprint, request, jsonify, redirect
from forms import ShortProxy

api = Blueprint('api', __name__, url_prefix='')
p = ShortProxy()

@api.route('/<short>')
def get(short):
	return redirect(p.redirect_to(request.base_url, str(request.headers) + request.remote_addr), code=301)

@api.route('/generate', methods=['POST'])
def post():
	return jsonify({'result': p.generate_url(request.url_root, request.form['target'])})
