from flask import Flask, g, jsonify
from neo4j import GraphDatabase
from transaction_functions import get_user_by_email, get_user_by_full_name, get_user_by_preferred_name, set_user_email, set_user_job_title
from transaction_functions import set_user_full_name, set_user_preferred_name, set_user_short_bio, set_user_story, create_user
from transaction_functions import check_user, set_user_education, set_user_gender, set_user_phone, set_user_profile_pic, set_user_location
import os
from flask_restplus import Api, Resource, fields
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
api = Api(app)


uri = os.getenv("NEO4J_URI")
db_user = 'neo4j'
password = os.getenv("NEO4J_PASSWORD")
driver = GraphDatabase.driver(uri, auth=(db_user, password))


def create_session():
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = driver.session()
    return g.neo4j_db


user_email_model = api.model('User email', {'new_email': fields.String(
    description='The new user email')})  # description for user emails.
user_fullname_model = api.model('User full name', {'new_full_name': fields.String(description='The new user\' full name'),
                                                   'user_email': fields.String(description='The user\'s email')})
user_preferredname_model = api.model('User preferred name', {'new_preferred_name': fields.String(description='The new user\'s preferred name'),
                                                             'user_email': fields.String(description='The user\'s email')})
user_short_bio_model = api.model('User short bio', {
                                 'new_short_bio': fields.String(description='The new user\'s short bio')})
user_story_model = api.model(
    'User story', {'new_story': fields.String(description='The new user\'s story')})
user_education_model = api.model('User education', {
                                 'new_education': fields.String(description='The new user\'s education')})
user_gender_model = api.model('User gender', {
                              'new_gender': fields.String(description='The new user\'s gender')})
user_phone_model = api.model(
    'User phone', {'new_phone': fields.String(description='The new user\'s phone')})
user_profile_pic_model = api.model('User profile pic', {
                                   'new_profile_pic': fields.String(description='The new user\'s profile pic')})
user_location_model = api.model('User location', {
                                'new_location': fields.String(description='The new user\'s location')})
user_job_title_model = api.model('User job title', {
                                 'new_job_title': fields.String(description='The new user\'s job title')})
account_model = api.model('User data', {'email': fields.String(description='The user email. MANDATORY.'),
                                        'password': fields.String(description='The user password with no hashing yet. MANDATORY.'),
                                        'full_name': fields.String(description='The user full name. MANDATORY.'),
                                        'preferred_name': fields.String(description='The user preferred name.'),
                                        'image': fields.String(description='image saved as array of Bytes representing the user\'s profile pic.'),
                                        'phone': fields.String(description='The user\'s phone number.'),
                                        'gender': fields.String(description='male or female.'),
                                        'job_title': fields.String(description='current job title of the user.'),
                                        'location': fields.String(description='current city of the user.'),
                                        'short_bio': fields.String(description='short bio describing the user of maximum 250 characters.'),
                                        'story': fields.String(description='story describing the user of maximum 250 words.'),
                                        'education': fields.String(description='Highest level obtained.')})  # description for accounts that needs to be created.
login_credentials_model = api.model('Login credentials', {'email': fields.String(description='User\'s email'),
                                                          'password': fields.String(description='Plain user\'s password')})


@api.route('/user/email/<email>')
class EmailUser(Resource):
    def get(self, email):
        with create_session() as session:
            response = session.read_transaction(get_user_by_email, email)
            user = response.single()
            if user:
                return 200
            return "User was not found", 404

    # You need to specify what is expected to be posted as body of the http message on this post.
    @api.expect(user_email_model)
    def put(self, email):
        with create_session() as session:
            response = session.read_transaction(
                set_user_email, email, api.payload.get('new_email'))
            if response:
                return 200
            return "User was not found", 404


@api.route('/user/full-name')
class FullName(Resource):
    @api.expect(user_fullname_model)
    def put(self):
        with create_session() as session:
            response = session.read_transaction(set_user_full_name, api.payload.get(
                'user_email'), api.payload.get('new_full_name'))
            user = response.single()
            if user:
                return 200
            return "User was not found", 404


@api.route('/user/preferred-name')
class PreferredName(Resource):
    @api.expect(user_preferredname_model)
    def put(self):
        with create_session() as session:
            response = session.read_transaction(set_user_preferred_name, api.payload.get(
                'user_email'), api.payload.get('new_preferred_name'))
            user = response.single()
            if user:
                return 200
            return "User was not found", 404


@api.route('/user/short-bio/<user_email>')
class ShortBio(Resource):
    @api.expect(user_short_bio_model)
    def put(self, user_email):
        with create_session() as session:
            response = session.read_transaction(
                set_user_short_bio, user_email, api.payload.get('new_short_bio'))

            user = response.single()
            if user:
                return 200
            return "User was not found", 404


@api.route('/user/story/<user_email>')
class Story(Resource):
    @api.expect(user_story_model)
    def put(self, user_email):
        with create_session() as session:
            response = session.read_transaction(
                set_user_story, user_email, api.payload.get('new_story'))
            user = response.single()
            if user:
                return 200
            return "User was not found", 404


@api.route('/user/education/<user_email>')
class Education(Resource):
    @api.expect(user_education_model)
    def put(self, user_email):
        with create_session() as session:
            response = session.read_transaction(
                set_user_education, user_email, api.payload.get('new_education'))
            user = response.single()
            if user:
                return 200
            return "User was not found", 404


@api.route('/user/gender/<user_email>')
class Gender(Resource):
    @api.expect(user_gender_model)
    def put(self, user_email):
        with create_session() as session:
            response = session.read_transaction(
                set_user_gender, user_email, api.payload.get('new_gender'))
            user = response.single()
            if user:
                return 200
            return "User was not found", 404


@api.route('/user/phone/<user_email>')
class Phone(Resource):
    @api.expect(user_phone_model)
    def put(self, user_email):
        with create_session() as session:
            response = session.read_transaction(
                set_user_phone, user_email, api.payload.get('new_phone'))
            user = response.single()
            if user:
                return 200
            return "User was not found", 404


@api.route('/user/profile-pic/<user_email>')
class ProfilePic(Resource):
    @api.expect(user_profile_pic_model)
    def put(self, user_email):
        with create_session() as session:
            response = session.read_transaction(
                set_user_profile_pic, user_email, api.payload.get('new_profile_pic'))
            user = response.single()
            if user:
                return 200
            return "User was not found", 404


@api.route('/user/location/<user_email>')
class Location(Resource):
    @api.expect(user_location_model)
    def put(self, user_email):
        with create_session() as session:
            response = session.read_transaction(
                set_user_location, user_email, api.payload.get('new_location'))
            user = response.single()
            if user:
                return 200
            return "User was not found", 404


@api.route('/user/job-title/<user_email>')
class JobTitle(Resource):
    @api.expect(user_job_title_model)
    def put(self, user_email):
        with create_session() as session:
            response = session.read_transaction(
                set_user_job_title, user_email, api.payload.get('new_job_title'))
            user = response.single()
            if user:
                return 200
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
            return "User was not found", 404


@api.route('/login')
class LogIn(Resource):

    @api.expect(login_credentials_model)
    def post(self):
        with create_session() as session:
            profile = session.read_transaction(check_user, api.payload)
            if type(profile) is dict:
                return profile

            if profile:
                return dict(profile['p'].items()), 200
            return "User was not found", 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# TODO Get endpoints for education, gender, phone, profilePic, location, job_titles
