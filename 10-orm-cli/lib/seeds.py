import random
import sqlite3

from faker import Faker
from handler import Handler
from job import Job
from owner import Owner
from pet import Pet

if __name__ == "__main__":

    Job.drop_table()
    Pet.drop_table()
    Handler.drop_table()
    Owner.drop_table()
    Handler.create_table()
    Owner.create_table()
    Pet.create_table()
    Job.create_table()

    # Initialize faker
    fake = Faker()
    # Create an list for species with "CAT" and "Dog"
    species = ["CAT", "DOG"]
    # Create an list of cat breeds
    cat_breeds = [
        "Domestic long hair",
        "Domestic short hair",
        "Siamese",
        "Ragdoll",
        "Sphynx",
        "Burmese",
    ]

    # Create an list of dog breeds
    dog_breeds = [
        "Mix",
        "Husky",
        "Malamute",
        "Dachshound",
        "Samoyed",
        "Shiba Inu",
        "Corgi",
    ]

    # Create an list of temperaments
    temperament = ["Calm", "Nervous", "Mischievous", "Aggressive", "Hyper"]

    # Create an empty list for owners
    owners = []
    # Create a for loop that iterates 50 times
    for _ in range(50):
        # Create an owner using data from faker
        owner = Owner(
            name=f"{fake.first_name()} {fake.last_name()}",
            email=fake.email(),
            phone=random.randint(1000000000, 9999999999),
            address=fake.address(),
        )
        owner.save()
        owners.append(owner)

    # Create an empty pets list
    pets = []
    # Create a for loop that iterates over the owners list
    for owner in owners:
        # Create a for loop that iterates 1 - 3 times
        for _ in range(random.randint(1, 3)):
            # Use faker and the species, cat breeds, dog breeds and temperament list to create a pet
            rand_species = random.choice(species)
            pet = Pet(
                name=fake.name(),
                species=rand_species,
                breed=(
                    random.choice(cat_breeds)
                    if rand_species == "CAT"
                    else random.choice(dog_breeds)
                ),
                temperament=random.choice(temperament),
                owner_id=owner.id,
            )
            pet.save()
            pets.append(pet)

    # 5.✅ Create a empty list set to handlers
    handlers = []
    # Create a for loop that iterates 50 times
    for _ in range(50):
        # Create a handler with faker data
        handler = Handler(
            name=f"{fake.first_name()} {fake.last_name()}",
            email=fake.email(),
            phone=random.randint(1000000000, 9999999999),
            hourly_rate=random.uniform(25.50, 80.50),
        )
        handler.save()
        # Append handler to handlers
        handlers.append(handler)
    # Create an list of requests, "Walk", "Drop-in" and "Boarding"
    requests = ["Walk", "Drop-in", "Boarding"]

    # Create an empty list and set it to jobs
    jobs = []
    # Create a for loop that iterates over the handlers list
    for handler in handlers:
        # Create a for loop that iterates 1 - 10 times
        for _ in range(random.randint(1, 10)):
            # Create a Job using faker, the request list and pets list
            job = Job(
                request=random.choice(requests),
                date=fake.date_this_year(),
                notes=fake.sentence(),
                fee=handler.hourly_rate,
                handler_id=handler.id,
                pet_id=random.choice(pets).id,
            )
            # append the job to the jobs list
            job.save()
            jobs.append(job)


# 6.✅ Run the seeds file and head over to debug.py to test out your Many to Many
