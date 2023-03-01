class cats:

    def __init__(self, name):
        self.name = name
        self.age = 1
    def display_info(self):
        print(f"Name: {self.name}  Color: {self.color}  Age: {self.age}  Сharacter: {self.age}")


Alicia = cats("Alicia")
Alicia.color = "white"
Alicia.age = "2 months"
Alicia.сharacter = "Fast, smart, kind and loves to play with the ball"
Alicia.display_info()

Bella = cats("Bella ")
Bella.color = "Black"
Bella.age = "5 months"
Bella.сharacter = "Fast, smart, cunning and loves to be noticed"
Bella.display_info()