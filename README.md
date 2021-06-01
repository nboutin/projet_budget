# Features

Data are stored in Database

Transactions: date, account source, account destination, description, credit, debit
List, Insert, Delete

Account: name
List, Insert, Delete

# Usage

    python -m src.projet_budget

    [command] [args]

    transaction
		-l, --list
		-i, --insert
		-d, --delete
        
	account
		-l, --list
		-i, --insert
		-d, --delete

# Development

PEP8 configuration:

    -a -a --max-line-length 120

# Test

	cd src
	python -m unittest -v

# Dependencies

	sudo apt-get install python3-tk
	pip3 install tkintertable