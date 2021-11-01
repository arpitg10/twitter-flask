from flask import Flask, request, jsonify, make_response

from dao_object import get_data_new
from service import get_user_tweets_by_user, get_tweets_by_hashtag
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Twitter"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


### end swagger specific ###


@app.route('/')
def hello_world():
    return 'hello flask-twitter'


@app.route('/hashtags/<hashtag>')
def get_tweets_with_hashtag(hashtag):
    pageSize = request.args.get('limit')
    if not pageSize: pageSize = 30
    return jsonify(get_tweets_by_hashtag(hashtag, pageSize))


@app.route('/users/<user>')
def get_user_tweets(user):
    pageSize = request.args.get('limit')
    if not pageSize: pageSize = 30
    return jsonify(get_user_tweets_by_user(user, pageSize))

@app.route('/repo')
def get_data():
    return jsonify(get_data_new())

@app.errorhandler(404)
def handle_404_error(_error):
    return make_response(jsonify({
        'error': 'Url not found, Kindly check the url'
    }), 404)


@app.errorhandler(500)
def handle_500_error(_error):
    return make_response(jsonify({
        'error': 'Something happened, Kindly check your request'
    }), 500)


@app.errorhandler(400)
def handle_400_error(_error):
    return make_response(jsonify({
        'error': 'Bad Request'
    }), 400)


if __name__ == '__main__':
    app.run("0.0.0.0", port=80, debug=True)
