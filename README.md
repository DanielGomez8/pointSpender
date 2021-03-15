# Transaction point spender
## Setup
This project uses Flask so make sure you have flask installed in your python environment by either running `pip install flask` on your command line.

If you are using an IDE like [pycharm](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html) or  please refer to their respective user guides on how to install python packages If you are using an IDE like [pycharm](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html) or [anaconda]() please refer to their respective user guides on how to install python packages

## Start up
For the web service to start you simply have to run `python main.py` in your terminal once you are in the project dictionary, if you are using an IDE just load the project into it and run it from there

## Usage
This is hosted on `http://localhost:5000`.

The following are the available URI routes:
### GET /payers
This route is going to return the list of payers and their respective balances

### POST /addTransaction
This route will add a new transaction to user's ledger and update payer balances
Expects: `{"payer": String, "points": Integer, "timestamp": '%Y-%m-%dT%H:%M:%SZ'}`

### POST /spend
Expects: `{"points": Integer}`
This route will process the expenditure of the given points and delete depleted transactions

## Testing
if you prefer to skip the web service all together you can test the functionality of the back end by simple running `test.py`
