from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Names(Resource):
    def get(self, name):
        age = len(name)
        return {'name': name, 'age': age}

class Cars(Resource):
    def get(self, car):
        make = car.upper()
        model = car.lower()
        return {'make': make, 'model': model}

@app.route('/')
def home():
    return "HELLO"

@app.route('/Test/')
def test():
    return "Howdy"

api.add_resource(Names, '/names/<string:name>')
api.add_resource(Cars, '/cars/<string:car>')

app.run(port=5000)
