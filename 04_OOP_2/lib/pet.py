#!/usr/bin/env python3
# Class Attributes and Methods 

class Pet:
    # 4✅. Define a class attribute total_pets and set it to 0
        # Demonstrate the class attribute using debug.py
    total_pets = 0

    # 6✅. Create a class method increase_pets that will increment total_pets
        # replace Pet.total_pets += 1 in __init__ with increase_pets()
    @classmethod
    def increase_pets(cls, increment=1):
        cls.total_pets += increment

    # 15. add cls var all[] to keep all pet instances in memory (SSOT)
    
    # 23. for m2m w/o join cls, add handlers=None to init params
    def __init__(self,name, age, breed, temperament, image_url):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.image_url = image_url
        # 5✅. Update the class attribute whenever an instance is initialized
        # Pet.total_pets += 1
        # Demonstrate total_pets updating with each instance 
        self.increase_pets()

        # 24a. add protected _handlers=[]
        # 24d. iterate through handlers on init and use add_handler to populate _handlers
        # (25 goto handler.py)
        # 31. refactor init to remove _handlers refs

        # 16a. add protected _owner property, b/c not part of initial constructor
        # 16b. don't forget to 'save' new instances of Pet to all[]
        
    # 17. use @property decorator to expose the new protected _owner prpty

    # 18. create setter for owner property

    # 24b. reader method to expose _handlers (w/ @propery decorator?)

    # 24c. add_handler method takes a handler instance and appends to _handlers

    # (19 goto owner.py)

    # 32. refactor to remove handler-related methods

    # 33. write book_handler() which takes a handler, date, and duration (impoort Job class) and makes the appropriate Job instance

    # 34. write jobs() which uses a list comprehension, Job.all and a conditional matching job.pet == self

    # 35. write handlers() which makes another list comprehension based on jobs()

    # (36 goto handler.py)

    # 43. create an aggregate method total_billing() which uses a list comprehension with pet.jobs() and job.fee() to sum the fees for a pet instance's walks

    # 44. create a class aggregate method oldest_pet which will return the oldest pet instance

    # (45 goto debug.py)
 
    

    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
            image_url:{self.image_url}
        ''')




