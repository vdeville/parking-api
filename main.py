from flask import Flask
from flask_restful import Resource, Api
from webargs import fields
from webargs.flaskparser import use_args
import json

app = Flask(__name__)
api = Api(app)


class DataResponse(Resource):
    args = {
        'lat': fields.Str(missing=None),
        'long': fields.Str(missing=None),
        'camera_id': fields.Str(missing=None)
    }

    @use_args(args)
    def get(self, args):
        if args['lat'] is not None and args['long'] is not None:
            return {'message': 'The shortest parking is: XXX'}

        if args['camera_id'] is not None:
            with open('storage.json', mode='r') as file:
                return {'data': json.loads(file.read())[args['camera_id']]}

        with open('storage.json', mode='r') as file:
            return {'data': json.loads(file.read())}

    post_args = {
        'camera_id': fields.Str(missing=None),
        'available_place': fields.Str(missing=None),
        'total_place': fields.Str(missing=None),
    }

    @use_args(post_args)
    def post(self, post_args):

        json_dict = {}

        with open('storage.json') as file:
            content = file.read()
            if content == '':
                json_dict = {}
            else:
                json_dict = json.loads(content)
            file.close()

        json_dict.update({
            post_args['camera_id']: {
                "available_place": post_args['available_place'],
                "total_place": post_args['total_place']
            }
        })

        with open('storage.json', mode='w') as file:
            file.write(json.dumps(json_dict, indent=True))
            file.close()

        return {'success': True}


api.add_resource(DataResponse, '/data')

if __name__ == '__main__':
    app.run(debug=True)
