from services import calculate_summary

# Normal case: income minus expenses
transactions = [
    {"kind": "income", "amount": 100},
    {"kind": "expense", "amount": 25}
]
assert calculate_summary(transactions) == (100, 25, 75)

# Boundary case: no transactions
assert calculate_summary([]) == (0, 0, 0)

# Boundary case: expenses exceed income
transactions = [
    {"kind": "income", "amount": 10},
    {"kind": "expense", "amount": 20}
]
assert calculate_summary(transactions) == (10, 20, -10)

print("All 3 summary tests passed.")