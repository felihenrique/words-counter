from flask import Blueprint, request, jsonify, abort
from application.modules.words.services import process_text

bp = Blueprint('words', __name__, url_prefix='/words')

@bp.route('/count', methods=['POST'])
def count_words():
    body = request.json
    if(body['text'] == None):
        abort(422, 'Text is not present in the body')

    if(body['lang'] == None):
        abort(422, 'Lang is not present in the body')

    if(body['lang'] != 'en'):
        abort(400, 'Only english language is supported at this moment')

    result = process_text(body['text'])
    return jsonify(result)
