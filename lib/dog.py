class Dog:
    bark_sound = "Woof!"

    def __init__(self, name="Unnamed", breed="Unknown"):
        self.name = name
        self.breed = breed

    def sit(self):
        print("The dog is sitting.")

    def bark(self):
        print(self.bark_sound)