import argparse
import json
from pathlib import Path
from services import calculate_summary
from storage import load_transactions, save_transactions
from storage import backup_transactions
from uuid import uuid4
from datetime import date
import math
from validation import validate_transaction

def main():

    parser = argparse.ArgumentParser(
        description="Personal budget manager"
    )

    commands = parser.add_subparsers(
        dest="command",
        required=True
    )

    add = commands.add_parser("add")
    add.add_argument("kind", choices=["income", "expense"])
    add.add_argument("amount", type=float)
    add.add_argument("category")
    add.add_argument("--date", default=date.today().isoformat())

    commands.add_parser("summary")
    commands.add_parser("list")
    backup = commands.add_parser("backup")
    backup.add_argument("destination")
    args = parser.parse_args()

    try:
        transactions = load_transactions()
    except ValueError as error:
        parser.error(str(error))

    if args.command == "add":
        if not math.isfinite(args.amount) or args.amount <= 0:
            parser.error("Amount must be a finite number greater than zero.")

        category = args.category.strip().casefold()

        allowed_categories = [
            "food", "transport", "rent",
            "leisure", "salary", "other"
        ]

        if category not in allowed_categories:
            parser.error(
                "Category must be food, transport, rent, "
                "leisure, salary, or other."
            )
        try:
            transaction_date = date.fromisoformat(args.date)
        except ValueError:
            parser.error("Invalid date. Use YYYY-MM-DD.")

        if transaction_date.isoformat() != args.date:
            parser.error("Use the date format YYYY-MM-DD.")

        transaction = {
            "id": str(uuid4()),
            "kind": args.kind,
            "category": category,
            "amount": args.amount,
            "currency": "EUR",
            "date": transaction_date.isoformat()
        }
        try:
            validate_transaction(transaction)
        except ValueError as error:
            parser.error(str(error))

        transactions.append(transaction)
        save_transactions(transactions)

        print("Transaction saved.")

    elif args.command == "summary":
        income, expenses, balance = calculate_summary(transactions)

        print(f"Income: EUR {income:.2f}")
        print(f"Expenses: EUR {expenses:.2f}")
        print(f"Balance: EUR {balance:.2f}")
    elif args.command == "list":
        if not transactions:
            print("No transactions yet.")

        for transaction in transactions:
            print(
                f"{transaction.get('date', 'No date')} | "
                f"{transaction['kind']} | "
                f"{transaction['category']} | "
                f"EUR {transaction['amount']:.2f} | "
                f"ID: {transaction.get('id', 'No ID')}"
            )
    elif args.command == "backup":
        backup_transactions(args.destination)
        print("Backup saved.")
if __name__ == "__main__":
    main()