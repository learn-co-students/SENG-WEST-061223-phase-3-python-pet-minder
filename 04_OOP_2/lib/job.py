# 30a. create class Job
# 30b. init with pet, handler, date, duration
# 30c. include class var all[] and in init 'save' new instances to all[]
class Job:

    all = []

    def __init__(self, pet, handler, date, duration):
        self.pet = pet
        self.handler = handler
        self.date = date
        self.duration = duration
        Job.all.append(self)

# (31 goto pet.py)

# 42. add a fee() method which uses handler.hourly_rate and duration to make the calculation
    def fee(self):
        return self.handler.hourly_rate * self.duration

# (43 goto pet.py)

# 45. implement pet.total_billing for one of the pets

# 46. implement Pet.oldest_pet() on the Pet class