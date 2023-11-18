# Let's do some loops

for i in range(10):
    print("I love you Jesus", i)

# This is what we call a format specifier
print("\n")

# Okay, let's jump out of a loop when a condition is met

for i in range(10):
    if i == 7:
        break
    print("I love you Jesus", i)



# using the new line format specifier again.
print("\n")

# Mosh hasn't taught me this, but experience with JavaScript, PHP and C taught me this.

# Okay, let's not jump, but skip that current iteration
for i in range(10): 
    if i == 7:
        continue
    print("I love you Jesus", i)



# using the new line format specifier again.
print("\n")

# Let's expore the range() function,
# specifying the first and second argument specifies the start and stop.
# specifying another specifies the step

for i in range(1, 10):
    # Now this would start from 1
    print(i)


# using the new line format specifier again.
print("\n")

for i in range(1, 10, 2):
    # Now this would start from 1 and increment by 2
    print(i)


# using the new line format specifier again.
print("\n")


# Let's check the type of range function
print(type(range(10)))