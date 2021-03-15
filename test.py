import user

'''
This test file can be used to verified that the provided example is working correctly with out the use of the web server
'''


def test():
    u = user.User()

    u.add_transaction({"payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z"})
    u.add_transaction({"payer": "UNILEVER", "points": 200, "timestamp": "2020-10-31T11:00:00Z"})
    u.add_transaction({"payer": "DANNON", "points": -200, "timestamp": "2020-10-31T15:00:00Z"})
    u.add_transaction({"payer": "MILLER COORS", "points": 10000, "timestamp": "2020-11-01T14:00:00Z"})
    u.add_transaction({"payer": "DANNON", "points": 300, "timestamp": "2020-10-31T10:00:00Z"})

    print("----- SORTED TRANSACTIONS -----")
    for i in u.transactions:
        print(i)
    print()

    print("----- PAYER BALANCES -----")
    print(u.get_payers(), "\n")

    print("------ CALL TO SPEND POINTS ------")
    print(u.spend_points({'points': 5000}), "\n")

    print("----- PAYER BALANCES AFTER SPENDING -----")
    print(u.get_payers(), "\n")

    print("----- TRANSACTIONS IN LEDGER AFTER SPENDING -----")
    for i in u.transactions:
        print(i)


if __name__ == '__main__':
    test()
