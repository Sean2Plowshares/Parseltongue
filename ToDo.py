#!/usr/bin/env python3

def help():
    print("Available commands are new, show, list, and quit.")

def new(command):
    parsed_args = command.split(' ')[1:]
    title = ' '.join(parsed_args)
    print("Creating a new todo:", title)
    print("Write a short description for this todo. Enter an empty line when finished.")
    body = get_longform_user_input()
    return {'title': title, 'body': body, }

def get_longform_user_input():
    lines = []
    line = input()

    while line != '':
        lines.append(line)
        line = input()

    return '\n'.join(lines)

def list ():
    print()
    print("Your current todo list:")
    print()
    for index, todo in enumerate(todos):
        print("\t", index +1, todo['title'])
        print()


print("""
Welcome to Super Todo! This is a CLI to organize your life like it's 1999!
Just type a command to get started. If you need to know what commands are
available, just type 'help' or '?'
""")

while True:
    command = input("Command: ")

    if command == "help" or command == "?":
        help()
    elif command.startswith("new"):
        todos.append(new(command))
    elif command == "show":
        print("Sorry, I can't do that yet.")
    elif command == "list":
        print("Sorry, I can't do that yet.")
    elif command == "quit" or command == "exit":
        print("Thanks for using Super Todo!")
        break
    else:
        print("That's not a valid command. Use 'help' or '?' for more info.")
