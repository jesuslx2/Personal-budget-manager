import json
from pathlib import Path
from validation import validate_transaction

DATA_FILE = Path(__file__).parent / "transactions.json"


def load_transactions():
    if not DATA_FILE.exists():
        return []

    try:
        text = DATA_FILE.read_text(encoding="utf-8")
        transactions = json.loads(text)
    except (OSError, UnicodeError) as error:
        raise ValueError(
            "Cannot read transactions.json. Check the file and permissions."
        ) from error
    except json.JSONDecodeError as error:
        raise ValueError(
            "transactions.json contains invalid JSON. Check it before continuing."
        ) from error

    if not isinstance(transactions, list):
        raise ValueError(
            "transactions.json must contain a list of transactions."
        )
    seen_ids = set()

    for row, transaction in enumerate(transactions, start=1):
        try:
            validate_transaction(transaction)

            if transaction["id"] in seen_ids:
                raise ValueError("Duplicate transaction ID.")

            seen_ids.add(transaction["id"])

        except ValueError as error:
            raise ValueError(f"Record {row}: {error}") from error

    return transactions


def save_transactions(transactions):
    DATA_FILE.write_text(
        json.dumps(transactions, indent=4),
        encoding="utf-8"
    )

def backup_transactions(destination):
    transactions = load_transactions()

    with open(destination, "x", encoding="utf-8") as output:
        json.dump(transactions, output, indent=4)