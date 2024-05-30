import json
import os.path

if os.path.isfile('memory.json'):
    with open('memory.json') as mem:
            memory = json.load(mem)

print("--Caesium OS--")
print(memory)
def end():
    with open('memory.json', 'w') as mem:
        json.dump(memory, mem)
    quit()


def process(text):
    text_list = text.split()
    header = text_list[0].lower()

    if header == "end":
        print("Ending Process...\n")
        end()
    elif header == "open":
        if text_list[1] == "calculator": calculator()
        if text_list[1] == "memory": memory_manager()
def calculator():

    
    while True:
        value1 = input()
        if not value1.isdigit():
            print("Please provide 2 numbers in a row.")
            continue
        
        value2 = input()
        if not value2.isdigit():
            print("Please provide 2 numbers in a row.")
            continue
        
        operation = input("Enter an operation (+, -, *, /)")
        if operation == "+": print(float(value1) + float(value2))
        elif operation == "-": print(float(value1) - float(value2))
        elif operation == "*": print(float(value1) * float(value2))
        elif operation == "/": print(float(value1) / float(value2))
        else: print("You didn't enter in an operation. I am lazy, so frick you."); end
        if input("Q to Quit:").lower() == "q": print("Exiting Calculator..."); break

def memory_manager():
    while True:
    
        command = input("Enter [read] to read all memory, enter the key for a value to change or delete it, or enter a new key to create a new entry.").lower()
        if command == "read": print(memory)
        elif command in memory:
            option = input(f"Key {command} holds the value {memory[command]}. Do you want to [Change] it or [Delete] it from memory?")
            if option.lower() == "change": memory[command] = input("Enter the new value:")
            elif option.lower() == "delete": del memory[command]
        else:
            key = command
            value = input(f"Enter the value to define key {key} as:")
            memory.update({key:value})
        if input("Q to Quit").lower() == "q": break
while True:
    last_input = input("##")
    process(last_input)