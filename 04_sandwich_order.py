
total_cost = 0.00
sugar_tax = 0.50

bread_type = input("Sandwich or Wrap?")

filling_type = input("Meat, Vegetarian or Vegan?")

pudding = input("Cookie, Chips, Fruit or None")

drink = input("Fizzy drink, Water, Juice or None")

if bread_type != "sandwich":
  total_cost = 2.00
else:
  total_cost = 3.00

if filling_type == "vegetarian" or filling_type == "vegan":
  total_cost = total_cost + 1.00
else:
  total_cost = total_cost + 1.50

if pudding == "cookie" and drink == "fizzy drink":
  total_cost = total_cost + sugar_tax
if pudding == "none" or drink == "none":
  total_cost = total_cost - 0.50

print("Your total cost is: ${}".format(total_cost))

