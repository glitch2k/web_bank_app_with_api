from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from modules.database_mods import Member, db
import jsonify, json


# this dictionary will be used in conjunction with the "@marshal_with" module
# it defines how that module will convert an object into a serialized json object
mem_info_return = {
	'id': fields.Integer,
	'fname': fields.String,
	'lname': fields.String,
	'chk_bal': fields.Integer
}

total_bal_return = {
	'bank_bal': fields.Integer
}


# this creates an api endpoint to retreive data from the database based on the member id
# ...that was passed in the url
class MemInfo(Resource):
	@marshal_with(mem_info_return)
	def get(self, mem_id): # "mem_id" will hold the value to perform the query with
		result = Member.query.filter_by(id=mem_id).first() # this will return an object
		if not result:
			abort(404, message="Could not find member with that id")
		return result

class BankBalance(Resource):
	# bank_bal = 0
	# @marshal_with(total_bal_return)
	def get(self):
		bank_bal = 0
		accts = Member.query.all()
		# result = Member.query.filter_by(id=1).first()
		for acct in accts:
			bank_bal = acct.chk_bal + bank_bal
		return {"total bank balance": bank_bal}


class CreateNewMem(Resource):
	def post(self):
		new_mem = request.get_json()
		fname = new_mem['fname']
		lname = new_mem['lname']
		chk_bal = new_mem['chk_bal']

		new_mem_db = Member(fname=fname, lname=lname, chk_bal=chk_bal)
		db.session.add(new_mem_db)
		db.session.commit()
		return {"message": "member added"}
		
class Deposit(Resource):
	def post(self, mem_id):
		json_body = request.get_json()
		dep_amt = json_body['amt']
		find_mem = Member.query.filter_by(id=mem_id).first()
		if not find_mem:
			abort(404, message="Could not find member with supplied ID")

		find_mem.chk_bal = find_mem.chk_bal + int(dep_amt)
		db.session.add(find_mem)
		db.session.commit()

		verify = Member.query.filter_by(id=mem_id).first()
		return {"New balance": verify.chk_bal}
		
class Withdraw(Resource):
	def post(self, mem_id):
		json_body = request.get_json()
		wit_amt = int(json_body['amt'])
		find_mem = Member.query.filter_by(id=mem_id).first()
		if not find_mem:
			abort(404, message="Could not find member with supplied ID")

		if find_mem.chk_bal < wit_amt:
			abort(404, message="Member does not have enough funds to withdraw")
			
		find_mem.chk_bal = find_mem.chk_bal - wit_amt
		db.session.add(find_mem)
		db.session.commit()

		verify = Member.query.filter_by(id=mem_id).first()
		return {"New balance": verify.chk_bal}
