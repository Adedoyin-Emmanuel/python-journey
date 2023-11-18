# Here we use if statement and 
# tenary operators which is like syntatical sugar
# for if and else statement


jesusWouldProvide =  True

if(jesusWouldProvide):
    print("He would provide")


# Let's try the tenary operator

age = 28

isEligible = True if age >= 18 else False

message = "You can vote" if isEligible else "You can't vote" 

print(message, isEligible)


print("\n")

# Let's try the elif and else statement

iLoveMango = True

if(iLoveMango):
    print("I love mango")
else:   
    print("I don't love mango")


# let's try the elif statement

mangoLovesMe = True

if(mangoLovesMe):
    print("Mango loves me")
elif(iLoveMango):
    print("I love Mango")
else:
    print("You don't love mango and mango doesn't love you.")




# conditional chaining
if(iLoveMango and mangoLovesMe):
    print("Congrats, you love mango and mango fruit loves you.")
else:
    print("Oh no, something isn't right!")