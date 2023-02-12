import unittest
from flask_caching import Cache
from flask_restful import Resource,Api
from flask import Flask,jsonify, request,Flask,Response,current_app
from main.functions import *
from main.errors  import CustomApi

#config api
app = Flask(__name__) 
app.config.from_pyfile('../config.py')

#config test in api
@app.cli.command()    
def test():
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner().run(tests)

#config cache in api
cache = Cache(app)

#set custom api with own handler error
api=CustomApi(app)

#function to get endpoint /artist
class get_info_artist(Resource):  
    @cache.cached(timeout=120,query_string=True)
    def get(self):
        return Response(json.dumps(get_data_artist()), mimetype='application/json')


#setting link between path and function
api.add_resource(get_info_artist,'/artist')
