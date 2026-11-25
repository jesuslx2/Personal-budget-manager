from validation import validate_transaction

valid = {
    "id": "TEST001",
    "date": "2026-11-25",
    "kind": "expense",
    "category": "food",
    "amount": 5.0,
    "currency": "EUR"
}

# Valid data should be accepted.
validate_transaction(valid)

# Each invalid value should be rejected.
invalid_cases = [
    ("amount", 0),
    ("amount", -5),
    ("amount", float("nan")),
    ("category", "unknown"),
    ("date", "2026-02-30"),
    ("kind", "purchase")
]

for field, value in invalid_cases:
    transaction = valid.copy()
    transaction[field] = value

    try:
        validate_transaction(transaction)
    except ValueError:
        pass
    else:
        raise AssertionError(f"Invalid {field} was accepted.")

print("All 7 validation tests passed.")