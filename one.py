from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Names(Resource):
    def get(self, name):
        age = len(name)
        return {'name': name, 'age': age}


@app.route('/')
def home():
    return "HELLO"


api.add_resource(Names, '/names/<string:name>')

app.run(port=5000)
