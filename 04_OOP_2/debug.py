#!/usr/bin/env python3
# 📚 Review With Students:
# Introduction to Object Oriented programming, classes, instances, methods

from lib.cat import *

# 11. import owner class on config.py and import config.py here (circular imports)
from lib.config import *

# Importing the pet class
from lib.pet import *

# Instances of the pet classes
rose = Pet("rose", 11, "domestic longhair", "sweet", "rose.jpg")
cookie = Pet("cookie", 1, "Dachshund", "hyper", "cookie.jpg")
princess_grace = Cat(
    "princess grace", 7, "domestic longhair", "affectionate", "gracy.png", True
)

# 12. create owner instance
arthur = Owner("Arthur", "arthur@mail.com")
# 13. add pets to owner
# arthur.pets.append(rose)
# arthur.pets.append(cookie)
# 14. print the owner's pet list
# for pet in arthur.pets:
#     print(pet.name, pet.age)
# (15 goto pet.py)

# 22. refactor 13 and 14 above; use new methods add_pet() and pets() instead
arthur.add_pet(rose)
arthur.add_pet(cookie)

for pet in arthur.get_pets():
    pet.print_pet_details()
# (23 goto pet.py)

# 28. create 2 handler instances; create associations with both the #pet.add_handler and #handler.add_pet methods
aixe = Handler("Aixe", "aixe@mail.com", 22)
hodor = Handler("Hodor", "hodor@mail.com", 19.99)
luke = Pet("luke", 3, "domestic longhair", "sleepy", "luke.jpg")

# 29. discuss shortcomings of this approach and 30 goto job.py

# 40. refactor previous code; now use new methods on Pet and Handler to create Job instances which also create the desired associations
rose.book_handler(aixe, "7-31-23", 2)
rose.book_handler(hodor, "8-2-23", 2)
luke.book_handler(hodor, "8-3-23", 1.5)
hodor.create_job(luke, "7-24-23", 2.5)
aixe.create_job(luke, "7-26-23", 1.5)

# 41. demo the association methods

# (42 goto job.py)
import ipdb

ipdb.set_trace()
