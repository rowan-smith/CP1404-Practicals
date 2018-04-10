menu = """(H)ello
(G)oodbye
(Q)uit
""" 

user_name = input("Enter name: ")
user_choice = input(menu + ">>> ").upper()
while user_choice != 'Q':
    if user_choice == 'H':
        print("Hello {}!".format(user_name))
    elif user_choice == 'G':
        print("Goodbye {}!".format(user_name))
    else:
        print("Invalid choice")
    user_choice = input(menu + ">>> ").upper()
print("Finished.")
