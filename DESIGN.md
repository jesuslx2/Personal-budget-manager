# Why I organized the project this way

I split the program into three files to make it easier to follow.
budget_manager.py handles the terminal commands, services.py
calculates the totals, and storage.py loads and saves the data.

This means I can test the calculations without running the whole
program or changing the saved transactions. Having several files
takes a little more organization, but it makes each part easier
to find and update. The program checks new inputs before saving
them so that invalid transactions do not change the budget.