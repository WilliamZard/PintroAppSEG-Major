from flask import Flask, g, jsonify
from neo4j import GraphDatabase
from transaction_functions import get_user_by_email, get_user_by_full_name, set_user_email, set_user_full_name, create_user, check_user
import os
from flask_restplus import Api, Resource, fields
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
api = Api(app)
# TODO: type anotation
# TODO: use swagger.



uri = os.getenv("NEO4J_URI")
db_user = 'neo4j'
password = os.getenv("NEO4J_PASSWORD")
driver = GraphDatabase.driver(uri, auth=(db_user, password))

def create_session():
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = driver.session()
    return g.neo4j_db


user_email_model = api.model('User email', {'email' : fields.String(description= 'The new user email')}) #description for user emails.
user_fullname_model = api.model('User full name', {'fullName' : fields.String(description= 'The new user email')})
account_model = api.model('User data', {'email' : fields.String(description= 'The user email. MANDATORY.'),
                               'password': fields.String(description= 'The user password with no hashing yet. MANDATORY.'),
                               'full_name': fields.String(description= 'The user full name. MANDATORY.'),
                               'preferred_name': fields.String(description= 'The user preferred name.'),
                               'image': fields.String(description= 'image saved as array of Bytes representing the user\'s profile pic.'),
                               'phone': fields.Integer(description= 'The user\'s phone number.'),
                               'gender': fields.String(description= 'male or female.'),
                               'job_title': fields.String(description= 'current job title of the user.'),
                               'location': fields.String(description= 'current city of the user.'),
                               'short_bio': fields.String(description= 'short bio describing the user of maximum 250 characters.'),
                               'story': fields.String(description= 'story describing the user of maximum 250 words.'),
                               'education': fields.String(description= 'Highest level obtained.')})#description for accounts that needs to be created.
login_credentials = api.model('Login credentials', {'email': fields.String(description= 'User\'s email'),
                                                    'password': fields.String(description= 'Plain user\'s password')})

@api.route('/user/email/<email>')
class user(Resource):
    def get(self, email):
        with create_session() as session:
            response = session.read_transaction(get_user_by_email, email)
            user = response.single()
            if user:
                return dict(user['user'].items()), 200
            return "", 404

    @api.expect(user_email_model)#You need to specify what is expected to be posted as body of the http message on this post.
    def put(self, email):
         with create_session() as session:
            response = session.read_transaction(set_user_email, email, api.payload.get('email'))

            user = response.single()
            if user:
                return dict(user['user'].items()), 200
            return "", 404

@api.route('/user/full-name/<full_name>')
class user(Resource):
    def get(self, full_name):
        with create_session() as session:
            response = session.read_transaction(get_user_by_full_name, full_name)
            user = response.single()
            if user:
                return dict(user['user'].items()), 200
            return "User was not found", 404

    @api.expect(user_fullname_model)    
    def put(self, full_name):
         with create_session() as session:
            response = session.read_transaction(set_user_full_name, full_name, api.payload.get('fullName'))

            user = response.single()
            if user:
                return dict(user['user'].items()), 200
            return "User was not found", 404


@api.route('/signup')
class SignUp(Resource):

    @api.expect(account_model)
    def post(self):
        with create_session() as session:
            response = session.read_transaction(create_user, api.payload)
            if type(response) is dict:
                return response

            profile = response.single()
            if profile:
                return dict(profile['newUser'].items()), 200
            return "", 404

@api.route('/login')
class LogIn(Resource):
    
    @api.expect(login_credentials)
    def post(self):
        with create_session() as session:
            profile = session.read_transaction(check_user, api.payload)
            if type(profile) is dict:
                return profile
            
            if profile:
                return dict(profile['p'].items()), 200
            return "", 404

                

# TODO: support updating user info

if __name__ == '__main__':
    app.run(debug=True)

