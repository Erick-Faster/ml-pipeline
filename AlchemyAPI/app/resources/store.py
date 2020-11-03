from flask_restful import Resource, reqparse
from models.store import StoreModel

class Store(Resource):

    parser = reqparse.RequestParser() #Condicoes de entrada
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self):

        data = Store.parser.parse_args() #Validacao das condicoes de entrada

        if StoreModel.find_by_name(data['name']):
            return {'message': "A store with name '{}' already exists".format(name)}, 400

        
        store = StoreModel(data['name'])
        try:
            store.save_to_db()
        except:
            return {'message': "An error occured while creating the store"}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.find_all()]}