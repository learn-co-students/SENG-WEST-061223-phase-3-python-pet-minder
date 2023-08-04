import ipdb
from models import Base, Handler, Job, Owner, Pet
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("sqlite:///pet_app.db")
    # Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # 3✅ One to Many
    # Getting an owners pets
    # Use session.query and first to grab the first owner
    own1 = session.query(Owner).first()
    own2 = session.get(Owner, 2)
    # use session.query and filter_by to get the owners pets from Pet
    own1_pets = session.query(Pet).filter(Pet.owner_id == own1.id)
    own2_pets = own2.pets
    # print out your owners pets
    print([pet for pet in own1_pets])
    print([pet for pet in own2_pets])
    # Getting a pets owner
    # Use session.query and first to grab the first pet
    pet = session.get(Pet, 33)
    owner = session.query(Owner).filter(Owner.id == pet.owner_id)
    print([o for o in owner])
    # Use session.query and filter_by to get the owner associated with this pet

    # 4✅ Head back to models to build out a Many to Many
# --------------------------------------------

# 6.✅ Many to Many
# Use session.query and .first to get the first handler
handler = session.query(Handler).filter(Handler.id == 55).first()
# Use session.query and the .filter_by to grab the jobs
# handler_jobs = session.query(Job).filter(Job.handler_id == handler.id)
handler_jobs = handler.jobs
# ipdb.set_trace()
# Print the jobs
print([job for job in handler_jobs])
# Use the handler_jobs to query pets for the associated pet to each job.
handler_pets = [session.get(Pet, job.pet_id) for job in handler_jobs]
print([pet for pet in handler_pets])
# Optional breakpoint for debugging
# import ipdb; ipdb.set_trace()
