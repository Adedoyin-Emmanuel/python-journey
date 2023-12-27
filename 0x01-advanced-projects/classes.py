class Dog:
    # this is a magic method
    def __init__(self):
        print("This is me")
    

    #this is a class method
    @classmethod
    def bite(self):
        print("Dog wants to bite")


    def bark(self):
        print("Woof woof")
    


dog = Dog()

dog.bark()