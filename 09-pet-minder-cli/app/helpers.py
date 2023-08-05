from datetime import datetime

from models import Handler, Job, Pet
from pick import pick
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///pet_app.db")
session = sessionmaker(bind=engine)()
# Define model operations


def get_all_pets():
    return session.query(Pet).all()


def find_pet_by_id(id):
    return session.get(Pet, id)


def add_job_to_pet(pet):
    handler_names = [handler.name for handler in session.query(Handler).all()]
    title = "Which handler will be taking care of this job?"
    handler_name, index = pick(handler_names, title)
    handler = session.query(Handler).filter(Handler.name == handler_name).first()
    req_type = "What type of job are you requesting?"
    request_choice, index = pick(["Walk", "Drop-in", "Boarding"], req_type)
    date_string = input("Enter date and time in the format YYYY-MM-DD HH:MM:SS: ")
    date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    notes = input("Enter any special notes for the handler")
    job = Job(
        request=request_choice,
        handler_id=handler.id,
        pet_id=pet.id,
        date=date,
        notes=notes,
        fee=handler.hourly_rate,
    )
    session.add(job)
    session.commit()


def add_pet():
    pass
