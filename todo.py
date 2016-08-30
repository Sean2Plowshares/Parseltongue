#!/usr/bin/env python3
import json
import os

class Todo():
    def __init__(self, title, description, priority=0):
        self.title = title
        self.description = description
        self.priority = priority

    def __repr__(self):
        return self.title + "\n" + str(self.priority) + "\n\n" + self.description + "\n"

class TodoList():
    todos = []
    def __init__(self, name):
        self.name = name
        self.file_name = str(name) + ".json"

    def add_todo(self, todo):
        self.todos.append(todo)

    def find_todo(self, query):
        try:
            idx = int(target)
            return self.todos[idx -1]
        except ValueError:
            for todo in self.todos:
                if todo.title == target:
                    return todo
            return None

    def __repr__(self):
        r = ""
        for index, todo in enumerate(self.todos):
            r += "\t"+ str(index + 1) + todo.title
        return r

    def load(self):
        try:
            with open(nj, r) as todo_load:
                return json.loads(todo_load.read())
        except:
            return ''

    def save(self):
        with open("TEST.txt", "w") as f:
            j = json.dumps(self.todos)
            f.write(j)

def help():
    print("""
    Available commands are new, show, list, load, and quit.
    new <title> - creates a new todo with the title given
    show <index number / title> - displays the indicated todo title and body
    list - displays all todo titles and their index numbers
    quit - exits Super Todo
    """)

def parse_args(command):
    return command.split(' ')[1:]

def new(title, todo_list):
    print("Creating a new todo:", title)
    print("Write a short description for this todo. Enter an empty line when finished.")
    body = get_longform_user_input()
    todo_list.add_todo(Todo(title, body))

def get_longform_user_input():
    lines = []
    line = input()

    while line != '':
        lines.append(line)
        line = input()

    return '\n'.join(lines)

def list(todo_list):
    print()
    print("Your current todo list:")
    print(todo_list)

def show(query, todo_list):
    t = todo_list.find_todo(query)
    if t == None:
        print("Couldn't find that todo.")
    else:
        print(t)

print("""
Welcome to Super Todo! This is a CLI to organize your life like it's 1999!
Just type a command to get started. If you need to know what commands are
available, just type 'help' or '?'
""")

tl = TodoList("Default")

while True:
    command = input("Command: ")

    if command == "help" or command == "?":
        help()
    elif command.startswith("new"):
        new(parse_args(command), tl)
    elif command.startswith("show"):
        show(parse_args(command), tl)
    elif command == "list":
        list(tl)
    elif command == "quit" or command == "exit":
        print("Thanks for using Super Todo!")
        break
    else:
        print("That's not a valid command. Use 'help' or '?' for more info.")
    tl.save
