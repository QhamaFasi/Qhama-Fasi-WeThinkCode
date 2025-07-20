#coke.py

due = 50
print(f"Amount due: ${due}")
while True:
    user_amount = int(input("Insert coin (5, 10, or 25 cents): "))

    if user_amount in [5, 10, 25]:
        due -= user_amount
        if due <= 0:
            change = abs(due)
            break

    print(f"Amount due: ${due}")

print(f"Change owed: ${change}")


