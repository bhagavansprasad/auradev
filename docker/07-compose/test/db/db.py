# Simple web server 
import sys
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Product(Resource):
	def get(self):
		return {
			'products' : ['Bicycle', 'Toys', 'Books']
		}

api.add_resource(Product, '/')

if (__name__ =='__main__'):
	print("Running program")
	sport = int(sys.argv[1])
	app.run(host='0.0.0.0', port=sport, debug=True)
	print("Exiting program")

