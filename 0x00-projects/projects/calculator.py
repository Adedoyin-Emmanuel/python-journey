"""
Simple calculator in Python
"""

print("Python calculator\n")
print("Enter quit to quit")

command = input(">")
while True:
    if(command.lower() == "quit"):
        break
    result = eval(command)

    print(result)
