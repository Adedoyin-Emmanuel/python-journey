from abc import ABC, abstractmethod

class Enemy(ABC):
    def __init__(self):
        self.name = "Enemy"

    @abstractmethod
    def walk(self):
        pass

    def attack(self):
        print(f"{self.name} is attacking")


class Alien(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Alien"
    
    def walk(self):
        print("Walking")


class EvilBird(Enemy):

    def __init__(self):
        super().__init__()
        self.name = "Evil Bird"
    
    def walk(self):
        print("Walking")



evilBird = EvilBird()
alien = Alien()

evilBird.attack()
alien.attack()