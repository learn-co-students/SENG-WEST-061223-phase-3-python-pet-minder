from lib.config import Pet, Job
# 25a. create Handler class 
# 25b. init with name, email, hourly_rate
class Handler:

# 36. add cls var all[] and append new instances on init
    all = []

    def __init__(self, name, email, hourly_rate):
        self.name = name
        self.email = email
        self.hourly_rate = hourly_rate
        Handler.all.append(self)

# 26. create pets() instance method which uses a list comprehension of Pet.all (import Pet) with conditional if self in pet.handlers()
    def get_pets(self):
        # return [pet for pet in Pet.all if self in pet.handlers]
        return [job.pet for job in self.jobs()]

# 27. create an add_pet() which takes a pet instance and and adds self to that pet's handlers
    # def add_pet(self, pet):
    #     if isinstance(pet, Pet):
    #         pet.add_handler(self)
    #     else:
    #         raise ValueError("Handler must be an instance of the Handler class")

# (28 goto debug.py)

# 37. refactor add_pet() to create_job() which takes in a pet, day and duration and instantiates a Job
    def create_job(self, pet, day, duration):
        Job(pet, self, day, duration)

# 38. write jobs() which uses a list comprehension, Job.all (import) and a conditional matching job.handler == self
    def jobs(self):
        return [job for job in Job.all if job.handler == self]

# 39. refactor get_pets() to create a new list comprehension using jobs()

# (40 goto debug.py)


