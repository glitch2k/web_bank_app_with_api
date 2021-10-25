from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from modules.endpoint_mods import MemInfo, BankBalance, CreateNewMem, Deposit, Withdraw
# import jsonify, json

app = Flask(__name__)
api = Api(app)


# this ties the api endpoint to the a pattern that will be received in from the url request
# when the api receives a GET request with the following url:
#   - http://127.0.0.0:5000/member/2
# it will envoke the "member" class and pass the parameters from the request into that class for 
# ...further processing 
api.add_resource(MemInfo, "/member/<int:mem_id>")
api.add_resource(BankBalance, "/bank_bal")
api.add_resource(CreateNewMem, "/createmem")
api.add_resource(Deposit, "/deposit/<int:mem_id>")
api.add_resource(Withdraw, "/withdraw/<int:mem_id>")

if __name__ == "__main__":
	# app.run(debug=True, host='0.0.0.0')
	app.run(debug=True)