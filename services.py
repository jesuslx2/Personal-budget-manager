def calculate_summary(transactions):
    income = 0
    expenses = 0

    for transaction in transactions:
        if transaction["kind"] == "income":
            income += transaction["amount"]
        else:
            expenses += transaction["amount"]

    balance = income - expenses
    return income, expenses, balance