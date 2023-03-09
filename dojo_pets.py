class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        print("Walking Sethems")
    
    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()

    def bathe(self):
        self.pet.noise()



class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5


    def noise(self):
        print(self.noise)


treats = ['Bacon','Cheese']
pet_food = ['Beefz','Chickenz']

seth = Pet("Seth", "Dog",'farts', 'bark')
carlos = Ninja("Carlos","Delgado", treats, pet_food, seth)

carlos.feed()
carlos.feed()
carlos.walk()