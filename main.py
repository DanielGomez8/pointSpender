from flask import Flask, jsonify, request
import user

api = Flask(__name__)

# Init our user instance to save our actions
u = user.User()

'''
for testing purposes
'''
#u.add_transaction({"payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z"})
u.add_transaction({"payer": "UNILEVER", "points": 200, "timestamp": "2020-10-31T11:00:00Z"})
u.add_transaction({"payer": "DANNON", "points": -200, "timestamp": "2020-10-31T15:00:00Z"})
u.add_transaction({"payer": "MILLER COORS", "points": 10000, "timestamp": "2020-11-01T14:00:00Z"})
u.add_transaction({"payer": "DANNON", "points": 300, "timestamp": "2020-10-31T10:00:00Z"})


'''
This route will return a list of payers and their respective balances currently in the system
'''


@api.route('/payers', methods=['GET'])
def get_payers():
    return jsonify(u.get_payers()), 200


'''
Expects: {"payer": String, "points": Integer, "timestamp": '%Y-%m-%dT%H:%M:%SZ'}
This route will add a new transaction to user's ledger and update payer balances
'''


@api.route('/addTransaction', methods=['POST'])
def add_transaction():
    u.add_transaction(request.json)
    return jsonify(request.json), 201


'''
Expects: {"points": Integer}
This route will process the expenditure of the given points and delete depleted transactions
'''


@api.route('/spend', methods=['POST'])
def spend_points():
    return jsonify(u.spend_points(request.json)), 201


if __name__ == '__main__':
    api.run()
