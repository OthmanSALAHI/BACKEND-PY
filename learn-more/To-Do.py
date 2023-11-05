#!/usr/bin/python3
from sys import argv
import os

def add_task(filename, task):
    with open(filename, 'a') as file:
        file.write(f"{task}\n")

def del_task(filename, task):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    with open(filename, 'w') as file:
        for line in lines:
            if line.strip() != task:
                file.write(line)

def display_tasks(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

def main():
    if len(argv) < 3:
        print(f"Usage: {argv[0]} <command> <todo>")
        return

    filename = "todo.txt"
    command = argv[1]
    task = argv[2]

    if command == "add":
        add_task(filename, task)
    elif command == "del":
        del_task(filename, f"-- {task}")
    else:
        print("Command not found!")

    display_tasks(filename)

if __name__ == "__main__":
    main()
