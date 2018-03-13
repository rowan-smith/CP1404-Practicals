user_name = input("Please enter your name:\n>> ")
name_file = open('name.txt', 'w')
print('{}'.format(user_name), file=name_file)
name_file.close()

# -----------------------------------------------

new_name_file = open('name.txt', 'r')
new_user_name = new_name_file.read()
print("Your name is {}".format(new_user_name))
new_name_file.close()

# -----------------------------------------------

numbers_file = open('numbers.txt', 'r')
number_1 = numbers_file.readline()
number_2 = numbers_file.readline()
total = int(number_1) + int(number_2)
print(total)
numbers_file.close()

# -----------------------------------------------
# Lindsay's Example:
#
# in_file = open("numbers.txt", "r")
# total = 0
# for line in in_file:
# number = int(line)
# total += number
# print(total)
# in_file.close()