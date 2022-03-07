
print("---Welcome to Split My Bill---")

bill_total = float(input("What is the total bill?"))

people = int(input("How many people are sharing?"))

tip_percentage = int(input("What percentage tip would you like to leave?"))


bill_total = bill_total + (bill_total * tip_percentage/100)
cost_per_person = bill_total / people

print("Total bill including tip is ${}".format(bill_total))
print("Total cost per person is ${}".format(cost_per_person))

