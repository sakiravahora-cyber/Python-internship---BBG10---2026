price_per_notebook = 45
budget = 500

# 1. Total cost for 7 notebooks
total_cost = price_per_notebook * 7
print("Total cost for 7 notebooks:", total_cost)

# 2. Maximum notebooks bought with 500 rupees (using floor division //)
notebooks_bought = budget // price_per_notebook
print("Notebooks bought with 500:", notebooks_bought)

# 3. Money left over after buying maximum notebooks (using modulus %)
money_left = budget % price_per_notebook
print("Money left over:", money_left)