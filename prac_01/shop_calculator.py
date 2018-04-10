number_of_items = int(input("Please enter quantity of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Please enter quantity of items: "))

total = 0
for i in range(number_of_items):
    item_price = float(input("Please enter item {}'s price: $".format(i + 1)))
    total += item_price

if total > 100:
    discount = 10 / 100 * total
    total -= discount
print("Total price for {} items is ${:.2f}".format(number_of_items, total))
