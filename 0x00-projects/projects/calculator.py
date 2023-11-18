"""
Simple calculator in Python
"""

print("Emmysoft Python calculator\n")
print("Type quit to exit the program")

command = input(">")

def reset():
    command = input(">")

while True:
    if(command.lower() == "quit"):
        break
    result = eval(command)

    print(result)
    reset()
