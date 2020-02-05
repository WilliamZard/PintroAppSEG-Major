from flask import Flask, g, jsonify
from neo4j import GraphDatabase
from .transaction_functions import get_user
import os

app = Flask(__name__)
# TODO: type anotation

uri = os.getenv("NEO4J_URI")
db_user = 'neo4j'
password = os.getenv("NEO4J_PASSWORD")
driver = GraphDatabase.driver(uri, auth=(db_user, password))

def create_session():
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = driver.session()
    return g.neo4j_db


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/<email>', methods=['GET'])
def get_single_user(email):
    with create_session() as session:
        response = session.read_transaction(get_user, email)
        user = response.single()
        if user:
            return jsonify(dict(user['user'].items()))
        return []


if __name__ == '__main__':
    app.run(debug=True)

