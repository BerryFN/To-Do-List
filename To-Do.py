#To Do List

import json 
import os 
import time    

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_todolist():
    if not os.path.exists("ToDoList.json"):
        return{}
    with open("ToDoList.json", "r") as f:
        return json.load(f)
    
def save_todolist(ToDoList):
    with open("ToDoList.json", "w") as f:
        json.dump(ToDoList, f, indent=4)

clear_screen()
print("Welcome to your To-Do List!")
input("Press Enter To Continue...")
clear_screen()

print("Welcome to your To-Do List!")
print("1. Create New List")
print("2. Delete List")
print("3. Save And Exit")
Choice = input("")
clear_screen()

if Choice == '1':
    clear_screen()


if Choice == '3':
    clear_screen()
    print("Saving.")
    time.sleep(1)
    clear_screen()
    print("Saving..")
    time.sleep(1)
    clear_screen()
    print("Saving...")
    time.sleep(1)
    clear_screen()
    print("Saving.")
    time.sleep(1)
    clear_screen()
    print("Saving..")
    time.sleep(1)
    clear_screen()
    print("Saving...")
    time.sleep(1)
    clear_screen()
    print("Finished Saving")
    input("Press Enter To Exit...")
    clear_screen()
    SystemExit

