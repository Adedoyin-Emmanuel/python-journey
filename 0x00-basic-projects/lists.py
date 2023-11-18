# A list is like an array in other programming languages
# They are iteratable

letters = ["a", "b", "c", "d", "e", "f"]

# Loop over the letters list and print each letter
for letter in letters:
    print(letter)

print("\n")

# Now you may ask, to get the index of the list, we can use an inbuilt function called enumerate

for i, letter in enumerate(letters):
    print(letter, i)


# we could also do splitting in arrays,
# NOTE performing an action on a list returns a new list
# and does not modify the existing one

language = ["C#", "C", "C++", "Python", "TypeScript"]

print(language[3:])


print("\n")



# Unpacking or destructing lists

fruits = ["Mango", "Orange", "Pineapple", "Guava", "Strawberry"]

mango, orange, *others = fruits

print(mango)
print(orange)
print(others)



print("\n")


# Looping over 2 dimensional lists

arrays = [[0,1], [0,2], [0,3], [0,4], [0,5]]

for i, array in enumerate(arrays):
    print(f"Index is {i}")
    for j,number in enumerate(array):
        print(f"Index of second array is {j}")
        print(number)



print("\n")


# List methods
cars = ["Bugatti", "Labmorghini", "Benz", "Lexus", "Prada", "Volvo"]


# Add a new element to the array
cars.append("Ferrari")

# Add a new element at a specified index

cars.insert(0, "Henenssey Venom")


# Remove the element at the last
cars.pop()

# remove a specified index
cars.pop(1)

print(cars)