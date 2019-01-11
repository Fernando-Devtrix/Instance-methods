class Player:

    # Class Attribute
    #species = 'mammal'
    
    # Initializer / Instance Attributes
    def __init__(self, name, position, number):
        self.name = name
        self.position = position
        self.number = number

    # instance method
    def description(self):
        return "{} plays as {} with t-shirt number {}".format(self.name, self.position, self.number)


# Instantiate the Dog object

kike = Player("Enrique", "Deffender", 10)

# call our instance methods

print(kike.description())
