class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        old_hunger = self.hunger
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food. Hunger decreased from {old_hunger} to {self.hunger}.")
        print(f"{self.name}'s happiness increased to {self.happiness}.")
        
    def sleep(self):
        old_energy = self.energy
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy increased from {old_energy} to {self.energy}.")

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play.")
        else:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10,self.hunger + 1)
            print(f"{self.name} played! Energy is now at {self.energy}.")
            print(f"{self.name}'s happiness increased to {self.happiness}.")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows the trick: {trick}.")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}.")
        else:
            print(f"{self.name} doesn't know any tricks yet.")

    def get_status(self):
        print(f"🐶 {self.name}'s Status 🐶")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
