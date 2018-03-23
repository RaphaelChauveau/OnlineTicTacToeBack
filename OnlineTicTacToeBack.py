from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:admin@localhost:3306/sys'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()
