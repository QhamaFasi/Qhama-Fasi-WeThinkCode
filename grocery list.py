#grocery.py

grocery_list = []

while True:
    try:
        user_input = input().lower()

        if user_input == "":
            break

        grocery_list.append(user_input)
    except EOFError:
        break
    
each_item = sorted(set(grocery_list))
for item in each_item:
    print(grocery_list.count(item), item.upper())
    
