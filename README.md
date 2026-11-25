
# Personal Budget Manager

This project helps you keep track of your income and expenses
from the terminal. You can add transactions, view them, check
your balance, and create a backup.

Transactions are saved in a JSON file, so they are still there
when you close and reopen the program.

## Getting started

You need Python 3.10 or newer. There is nothing extra to install.

Open the terminal in the folder containing budget_manager.py.
To see the available commands, run:

```bash
python3 budget_manager.py --help
```

## Adding transactions

To record an expense:

```bash
python3 budget_manager.py add expense 18.50 food --date 2026-11-25
```

To record income:

```bash
python3 budget_manager.py add income 100 salary
```

If you leave out the date, the program uses today's date.
Each time you run an add command, it saves a new transaction.

You can use these categories:
food, transport, rent, leisure, salary, and other.

The program rejects zero or negative amounts, infinite values,
invalid dates, and categories outside this list. It also cleans
category names, so "Food" and "food" are treated the same.

## Viewing your budget

To see all saved transactions:

```bash
python3 budget_manager.py list
```

To see your total income, expenses, and remaining balance:

```bash
python3 budget_manager.py summary
```

For example, if you receive EUR 100 and spend EUR 25,
your balance will be EUR 75.

## Creating a backup

To save a separate copy of your transactions:

```bash
python3 budget_manager.py backup backup-new.json
```

Choose a filename that does not already exist. The program
will not overwrite an existing backup.

## Running the tests

Run:


```bash
python3 test_services.py
python3 test_storage.py
python3 test_validation.py
```

The tests check budget calculations, saving and loading,
missing files, damaged JSON, and invalid transaction values.
They use separate test data and do not change saved transactions.

## How the project is organized

- validation.py checks transaction fields and values.
- test_storage.py checks saving, loading, and damaged JSON.
- test_validation.py checks valid and invalid transactions.
- data/ contains valid and invalid CSV examples.
- 
## What still needs improvement

The program supports EUR only.

Amounts use Python floats, so small rounding differences
are possible.

Saving and backup errors, such as a folder without write
permission or an existing backup filename, may display
Python error messages.

The program does not protect against two copies saving
transactions at the same time.

The CSV files in data/ are examples for review.
The program currently loads transactions from JSON.
