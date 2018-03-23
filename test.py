from click.core import augment_usage_errors

from OnlineTicTacToeBack import app, db
from flask import request
from uuid import uuid4

# import model here (needs to be after db ?)
from User import User

# RAZ BDD
db.drop_all()
db.create_all()

tokens_users = {}

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/create_user')
def create_user():
    new_user = User(email=request.args["email"], password=request.args["password"], username=request.args["username"],
                    verified=False)
    db.session.add(new_user)
    db.session.commit()
    return "OK"


@app.route('/get_token')
def get_token():
    user = User.query.filter_by(email=request.args["email"]).first()
    if user.password != request.args["password"]:
        return "WRONG PWD"
    else:
        token = uuid4().hex
        tokens_users[token] = user.id
        return token


@app.route('/get_resource')
def get_resource():
    authenticated_user_id = tokens_users.get(request.args["token"])
    if authenticated_user_id is None:
        return "NOT AUTHENENTICATED"
    else:
        print("user", authenticated_user_id, "accessed resource")
        return "This is a resource !!!"


if __name__ == '__main__':
    app.run()