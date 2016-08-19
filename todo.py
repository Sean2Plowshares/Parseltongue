#!/usr/bin/env python3

def help():
    print("""
    Available commands are new, show, list, and quit.
    new <title> - creates a new todo with the title given
    show <index number / title> - displays the indicated todo title and body
    list - displays all todo titles and their index numbers
    quit - exits Super Todo
    """)

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

def print_todo(todo):
    print()
    print("Title:")
    print(todo["title"])
    print()
    print("Description:")
    print(todo["body"])
    print()

def show(command):
    parsed_args = command.split(' ')[1:]
    target = ' '.join(parsed_args)

    try:
        idx = int(target)
        print_todo(todos[idx -1])
    except ValueError:
        for todo in todos:
            if todo["title"] == target:
                print_todo(todo)
                return
        print("Input error. Try again.")
    except e:
        print("Invalid input. Try again")


print("""
Welcome to Super Todo! This is a CLI to organize your life like it's 1999!
Just type a command to get started. If you need to know what commands are
available, just type 'help' or '?'
""")

todos = []

while True:
    command = input("Command: ")

    if command == "help" or command == "?":
        help()
    elif command.startswith("new"):
        todos.append(new(command))
    elif command.startswith("show"):
        show(command)
    elif command == "list":
        list()
    elif command == "quit" or command == "exit":
        print("Thanks for using Super Todo!")
        break
    else:
        print("That's not a valid command. Use 'help' or '?' for more info.")
