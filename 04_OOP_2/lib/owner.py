from lib.config import Pet
# 10a. create class for Owner
# 10b. initialize with name and email
# 10c. demo one-way assn by init with pets []
class Owner:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        # self.pets = []
        # (11 goto debug.py)

    def __repr__(self):
        return f'<Owner: {self.name} {self.email}>'

# 19. remove pets property on refactor to two-way assn

# 20. write instance method pets() which returns a list comprehension of Pet.all (import Pet) with conditional to match pet.owner == self
    def get_pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

# 21. write instance method add_pet(self, pet) which takes a pet instance (checks to be sure it IS a pet instance) then assigns self as that instances owner
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError('Pet must be an instance of Pet class')
        pet.owner = self

# (22 goto debug.py)