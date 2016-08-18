#!/usr/bin/env pyhton3

def help():
    print("Available commands are new, show, list, and quit.")

print("""
Welcome to Super Todo! This is a CLI to organize your life like it's 1999!
Just type a command to get started. If you need to know what commands are
available, just type 'help' or '?'
""")

while True:
    command = input("Command:")

    if command == "help" or command == "?":
        help()
    elif command == "new":
        print("Sorry, I can't do that yet.")
    elif command == "show":
        print("Sorry, I can't do that yet.")
    elif command == "list":
        print("Sorry, I can't do that yet.")
    elif command == "quit" or command == "exit":
        print("Thanks for using Super Todo!")
        break
    else:
        print("""
        That's not a valid command.
        Use commands 'help' or '?' for a list of valid commands.
        ''")
