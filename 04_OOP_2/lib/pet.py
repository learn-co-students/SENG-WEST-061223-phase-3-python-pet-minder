#!/usr/bin/env python3
# Class Attributes and Methods 
# from lib.config import Owner
from lib.job import Job

class Pet:
    # 4✅. Define a class attribute total_pets and set it to 0
        # Demonstrate the class attribute using debug.py
    total_pets = 0

    # 15. add cls var all[] to keep all pet instances in memory (SSOT)
    all = []

    # 6✅. Create a class method increase_pets that will increment total_pets
        # replace Pet.total_pets += 1 in __init__ with increase_pets()
    @classmethod
    def increase_pets(cls, increment=1):
        cls.total_pets += increment

    
    # 23. for m2m w/o join cls, add handlers=None to init params
    def __init__(self,name, age, breed, temperament, image_url, handlers=None):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.image_url = image_url
        # 5✅. Update the class attribute whenever an instance is initialized
        # Pet.total_pets += 1
        # Demonstrate total_pets updating with each instance 
        self.increase_pets()
        # 16a. add protected _owner property, b/c not part of initial constructor
        # 16b. don't forget to 'save' new instances of Pet to all[]
        self._owner = None
        Pet.all.append(self)

        # 24a. add protected _handlers=[]
        # self._handlers = []
        # 24d. iterate through handlers on init and use add_handler to populate _handlers
        # if handlers:
        #     for handler in handlers:
        #         self.add_handler(handler)
        # (25 goto handler.py)

        # 31. refactor init to remove _handlers refs

        
    # 17. use @property decorator to expose the new protected _owner prpty
    @property
    def owner(self):
        return self._owner

    # 18. create setter for owner property
    @owner.setter
    def owner(self, value):
        # if not isinstance(value, Owner):
        #     raise TypeError("Owner must be an instance of Owner class")
        self._owner = value

    # (19 goto owner.py)

    # 24b. reader method to expose _handlers (w/ @propery decorator?)
    # @property
    # def handlers(self):
    #     return self._handlers

    # 24c. add_handler method takes a handler instance and appends to _handlers
    # def add_handler(self, handler):
    #     self._handlers.append(handler)

    # 32. refactor to remove handler-related methods

    # 33. write book_handler() which takes a handler, date, and duration (impoort Job class) and makes the appropriate Job instance
    def book_handler(self, handler, date, duration):
        Job(self, handler, date, duration)

    # 34. write bookings() which uses a list comprehension, Job.all and a conditional matching job.pet == self
    def bookings(self):
        return [job for job in Job.all if job.pet == self]

    # 35. write handlers() which makes another list comprehension based on jobs()
    def handlers(self):
        return [job.handler for job in self.bookings()]

    # (36 goto handler.py)

    # 43. create an aggregate method total_billing() which uses a list comprehension with pet.bookings() and job.fee() to sum the fees for a pet instance's walks
    def total_billing(self):
        return f"${sum([job.fee() for job in self.bookings()]):.2f}"

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




