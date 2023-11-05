#!/usr/bin/python3
from sys import argv
import os
filename = __file__
def TODO(command, todo_list, todo):
    if command == "add":
        todo_list.append(todo)
    elif command == "del":
        try:
            todo_list.remove(todo)
        except ValueError:
            print(f"Todo '{todo}' not found in the list.")
    else:
        print("Command not found!")

    for item in todo_list:
        with open("todo.txt" , "a") as f:
            f.write(f"  -- {item}\n")

def main():
    if len(argv) < 3:
        print(f"Usage: {filename} <command> <todo> <todo_list>")
        return

    command = argv[1]
    todo = argv[2]
    todo_list = []
    TODO(command, todo_list, todo)
    with open("todo.txt","r") as file:
        content = file.read()
    print(content)
if __name__ == "__main__":
    main()
