#!/usr/bin/env python3
# 📚 Review With Students:
    # Introduction to Object Oriented programming, classes, instances, methods

# Importing the pet class 
# from lib.pet import * // now causing circular import
# from lib.pet import *
# from lib.cat import *
from lib.config import *
# 11. import owner class
# from lib.owner import *
# from lib.config import Cat, Owner

# Instances of the pet classes
rose = Pet('rose', 11, 'domestic longhair', 'sweet', 'rose.jpg')
cookie = Pet('cookie', 1, 'Dachshund', 'hyper', 'cookie.jpg')
princess_grace = Cat('princess grace', 7, 'domestic longhair', 'affectionate', 'gracy.png', True)

# 4a. Demonstrate the class attribute using debug.py
        # Pet.total_pets -> 0
        # rose.total_pets -> 0
        # cookie.total_pets -> 0
        # Demonstrate updating a class attribute 
        # Pet.total_pets += 1
        # rose.total_pets -> 1
        # cookie.total_pets -> 1
# 4b. Demonstrate total_pets updating with each instance 
        # Pet.total_pets -> 3
        # Pet('luke', 3, 'domestic longhair', 'sleepy', 'luke.jpg')
        # Pet.total_pets -> 4

#12. create owner instance
arthur = Owner('Arthur', 'arthur@mail.com')
#13. add pets to owner
# arthur.pets.append(rose)
# arthur.pets.append(cookie)
#14. print the owner's pet list
# for pet in arthur.pets:
#     print(pet.name, pet.age)
# (15 goto pet.py)

# 22. refactor 13 and 14 above; use new methods add_pet() and pets() instead
arthur.add_pet(rose)
arthur.add_pet(cookie)
# [pet.print_pet_details() for pet in arthur.pets()]
for pet in arthur.get_pets():
    pet.print_pet_details()

# (23 goto pet.py)

# 28. create 2 handler instances; create associations with both the #pet.add_handler and #handler.add_pet methods
aixe = Handler('Aixe', 'aixe@mail.com', 22)
hodor = Handler('Hodor', 'hodor@mail.com', 19.99)
luke = Pet('luke', 3, 'domestic longhair', 'sleepy', 'luke.jpg')
# rose.add_handler(aixe)
# cookie.add_handler(aixe)
# hodor.add_pet(luke)
# hodor.add_pet(cookie)

# 29. discuss shortcomings of this approach and 30 goto job.py

# 40. refactor previous code; now use new methods on Pet and Handler to create Job instances which also create the desired associations
rose.book_handler(aixe, '7-21-23', 2)
rose.book_handler(hodor, '7-23-23', 1.5)
hodor.create_job(luke, '7-24-23', 2.5)
aixe.create_job(luke, '7-26-23', 1.5)

# 41. demo the association methods

# (42 goto job.py)
import ipdb; ipdb.set_trace()