from datetime import datetime


class User:
    transactions = []  # Ledger of currently available transactions
    payers = {}  # Current payer balances

    '''
    This function is going to take a json from the request and add the transaction to the ledger and
    update how much money the payer has after the transaction takes place
    '''

    def add_transaction(self, request):
        request['timestamp'] = self.parse_date(request['timestamp'])  # First parse date to sort later
        self.process_payer(request['payer'], request['points'])  # Update payer balance
        self.transactions.append(request)  # Log transaction
        self.sort_by_date()  # Sort ledger by date after new addition

    '''
    This function is going to update/create the payers balance if the negative att is tru
    the function will subtract otherwise it will add
    '''

    def process_payer(self, payer, points, negative=False):
        # Create instance of payer in map if one does not exist
        if payer not in self.payers.keys():
            self.payers[payer] = 0

        if negative:
            self.payers[payer] = self.payers[payer] - points  # Subtract points from balance

        else:
            self.payers[payer] = self.payers[payer] + points  # Add points to balance

    '''
    This function is going to take a json from the request and process the points from the input 
    by spending the transactions in chronological order, if a given transaction is not enough 
    to pay the point balance, the point value of the transaction will be subtracted from the balance
    and the transaction will be marked for deletion, if the transaction is sufficient to cover the 
    balance then the points in the balance will be subtracted from the transaction point value.
    At the end the transactions marked for deletion will be removed from the ledger and the function will
    return a summary of what was spent and from which payers.
    '''

    def spend_points(self, request):
        # Init our local variables
        remove = []
        response = []
        spent = {}
        points = request['points']

        for t in self.transactions:
            # Check if transaction will have remainder after point deduction
            if points >= t['points']:
                self.process_payer(t['payer'], t['points'], True)  # Update payer balance
                remove.append(t)  # Mark transaction for removal
                points = points - t['points']  # Subtract spent points from balance

                # Update payer expenditure log
                if t['payer'] not in spent.keys():
                    spent[t['payer']] = 0
                spent[t['payer']] = spent[t['payer']] - t['points']

            else:
                t['points'] = t['points'] - points  # Update transaction balance
                self.process_payer(t['payer'], points, True)  # Update payer balance

                # Update payer expenditure log
                if t['payer'] not in spent.keys():
                    spent[t['payer']] = 0 - points

                points = points - t['points']  # Subtract spent points from balance
                break  # Exit loop since we have no balance remaining

        # At the end if there is not enough points to cover balance we exit and raise an error
        if points > 0:
            return None

        # Build response body
        for key, value in spent.items():
            response.append({'payer': key, 'points': value})
        # Removed used transactions from ledger
        for r in remove:
            self.transactions.remove(r)

        return response

    '''
    Returns the list of current payer balances
    '''

    def get_payers(self):
        return self.payers

    '''
    Sorts the transaction ledger in chronological order
    '''

    def sort_by_date(self):
        self.transactions.sort(key=lambda x: x['timestamp'])

    '''
    Turns timestamp string into datetime object
    '''

    def parse_date(self, date):
        return datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
