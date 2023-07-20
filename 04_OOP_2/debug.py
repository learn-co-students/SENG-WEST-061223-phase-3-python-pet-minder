#!/usr/bin/env python3
# 📚 Review With Students:
    # Introduction to Object Oriented programming, classes, instances, methods

# Importing the pet class 
from lib.pet import *
from lib.cat import *
# 11. import owner class on config.py and import config.py here (circular imports)

# Instances of the pet classes
rose = Pet('rose', 11, 'domestic longhair', 'sweet', 'rose.jpg', True)
cookie = Pet('cookie', 1, 'Dachshund', 'hyper', 'cookie.jpg')
princess_grace = Cat('princess grace', 7, 'domestic longhair', 'affectionate', 'gracy.png')

#12. create owner instance
#13. add pets to owner

#14. print the owner's pet list

# (15 goto pet.py)

# 22. refactor 13 and 14 above; use new methods add_pet() and pets() instead

# (23 goto pet.py)

# 28. create 2 handler instances; create associations with both the #pet.add_handler and #handler.add_pet methods

# 29. discuss shortcomings of this approach and 30 goto job.py

# 40. refactor previous code; now use new methods on Pet and Handler to create Job instances which also create the desired associations

# 41. demo the association methods

# (42 goto job.py)
import ipdb; ipdb.set_trace()