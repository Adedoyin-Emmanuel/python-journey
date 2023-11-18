# A list is like an array in other programming languages
# They are iteratable

letters = ["a", "b", "c", "d", "e", "f"]

# Loop over the letters list and print each letter
for letter in letters:
    print(letter)

print("\n")

# Now you may ask, to get the index of the list, we can use an inbuilt function called enumerate

for index, letter in enumerate(letters):
    print(letter, index)


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