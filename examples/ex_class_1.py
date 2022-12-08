class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
        self.demange = 10

    def display(self):
        print(f"Моё имя {self.name} и мне {self.age} лет [{self.health}%]")

    def attack(self, person):
        import random
        self.health = self.health - person.demange - random.randint(-7, 7)
        self.beep()

    def beep(self):
        import winsound
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 200  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)

    def isLive(self):
        if self.health >= 0:
            return True
        else:
            print(f"{self.name} Game Over")
            return False


Mihalich = Person("Михалыч", 37)
Daniel = Person("Даниель", 16)

while Mihalich.isLive() and Daniel.isLive():
    Mihalich.display()
    Daniel.display()
    Daniel.attack(Mihalich)
    Mihalich.attack(Daniel)

import winsound
frequency = 2000  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
for i in range(30):
    winsound.Beep(frequency+i*50, duration-30*i)
winsound.Beep(frequency, 10000)