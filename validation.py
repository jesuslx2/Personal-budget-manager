import math
from datetime import date


def validate_transaction(transaction):
    if not isinstance(transaction, dict):
        raise ValueError("Each transaction must be a dictionary.")

    required = ["id", "date", "kind", "category", "amount", "currency"]

    for field in required:
        if field not in transaction:
            raise ValueError(f"Missing field: {field}.")

    if not isinstance(transaction["id"], str) or not transaction["id"].strip():
        raise ValueError("ID must be non-empty text.")

    if transaction["kind"] not in ["income", "expense"]:
        raise ValueError("Kind must be income or expense.")

    allowed = ["food", "transport", "rent", "leisure", "salary", "other"]

    if transaction["category"] not in allowed:
        raise ValueError("Unknown category.")

    amount = transaction["amount"]

    if type(amount) not in [int, float]:
        raise ValueError("Amount must be a number.")

    if not math.isfinite(amount) or amount <= 0:
        raise ValueError("Amount must be finite and greater than zero.")

    if transaction["currency"] != "EUR":
        raise ValueError("Currency must be EUR.")

    try:
        parsed_date = date.fromisoformat(transaction["date"])
    except (ValueError, TypeError):
        raise ValueError("Date must be valid and use YYYY-MM-DD.")

    if parsed_date.isoformat() != transaction["date"]:
        raise ValueError("Date must use YYYY-MM-DD.")