from flask import Flask, jsonify
from flask_cors import CORS
from models import setup_db, Plant


# define the first endpoint called "app route decorator"
# underneath that, we define a method called "hello" to handle that route
# it returns a jsonify object with a key of message

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    # if you want to allow specific domains to access your resources or CROSS origin for specific groups
    # CORS(app, resources={r"*/api/*": {"origins": "*"}})

    # CORS Headers - After a request is received, run this method.
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response


    @app.route('/plants')
    def get_plants():
        plants = Plants.query.all()
        formatted_plants = [plant.format() for plant in plants]

        return jsonify({
            'success':True,
            'plants': formatted_plants
        })

    return app

'''
    @app.route('/messages')
    @cross_origin()
    def get_messages():
        return 'GETTING MESSAGES'
        
    @app.route("/hello")
    @cross_origin()
    def get_greeting():
        return jsonify({'message':'Hello, World!'})

    # a simple page that says hello
    @app.route('/')
    def hello():
        return jsonify({'message': 'HELLO WORLD'})

    @app.route('/smiley')
    def smiley():
        return ':)'
'''


