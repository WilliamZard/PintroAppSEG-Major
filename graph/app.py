from flask import Flask, g, jsonify
from neo4j import GraphDatabase
from transaction_functions import get_user, set_user_email
import os
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app)
# TODO: type anotation
# TODO: use swagger.

# os.environ["NEO4J_URI"] = "bolt://35.246.56.244:7687"
# os.environ["NEO4J_PASSWORD"] = "L0nd0n&EU"

uri = os.getenv("NEO4J_URI")
db_user = 'neo4j'
password = os.getenv("NEO4J_PASSWORD")
driver = GraphDatabase.driver(uri, auth=(db_user, password))

def create_session():
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = driver.session()
    return g.neo4j_db


user_email = api.model('User email', {'email' : fields.String('The new user email')}) #description for user emails.

@api.route('/user/<email>')
class user(Resource):
    def get(self, email):
        with create_session() as session:
            response = session.read_transaction(get_user, email)
            user = response.single()
            if user:
                return dict(user['user'].items()), 200
            return "", 404

    @api.expect(user_email)#You need to specify what is expected to be posted as body of the http message on this post.
    def post(self, email):
         with create_session() as session:
            response = session.read_transaction(set_user_email, email, api.payload.get('email'))
            user = response.single()
            if user:
                return dict(user['user'].items()), 200
            return "", 404


# TODO: support updating user info

if __name__ == '__main__':
    app.run(debug=True)

