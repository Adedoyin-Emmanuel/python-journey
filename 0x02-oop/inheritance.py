class Enemy:
    def __init__(self):
        self.x = 5
        self.y = 10
    
    def attack(self):
        print("Attacking")
    


class Alien(Enemy):
    def move(self):
        print("Moving")



alien = Alien()

alien.attack()
alien.move()