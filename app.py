import os

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

"""
CONFIG
"""

# db - construct path to SQLite file
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, os.getenv("SQLITE_FILE"))
db_uri = "sqlite:///" + db_path

# app - init, config
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db - init, declare model, create tables on app start
db = SQLAlchemy(app)


class Thing(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    def __repr__(self):
        return f"id {self.pk} name {self.name}"


db.create_all()

"""
ROUTES
"""

@app.route('/healthcheck')
def index():
    return "docker-flask-sqlite runnning", 200

@app.route("/get-things")
def read():
    things = [dict(id=x.pk, name=x.name) for x in Thing.query.all()]
    return jsonify({"things": things})

@app.route("/post-thing", methods=["POST"])
def create():
    thing = Thing(name=request.json["name"])
    db.session.add(thing)
    db.session.commit()
    return jsonify({"thing": dict(id=thing.pk, name=thing.name)})
