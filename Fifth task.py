
profit = float(input("Type in profit"))
costs = float(input("Type in costs"))
if profit > costs:
    print(f"All is good. Clean profit is  {profit / costs:.2f}")
    workers = int(input("Type in workers' quantity"))
    print(f"profit per worker {profit / workers:.2f}")
elif profit == costs:
    print("NO profit")
else:
    print("No profit with debts")