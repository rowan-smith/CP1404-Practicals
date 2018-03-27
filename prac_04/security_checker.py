NAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
         'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
         'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    user_name = input("Please enter user name: ")
    if user_name in NAMES:
        print("Access Granted!")
    else:
        print("Access Denied!")


main()
