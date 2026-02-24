import pytest
from Tools.scripts.fixdiv import report

from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.models.sqlite.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    reponse = repo.list_pets()
    print()
    print(reponse)

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_delete_pet():
    name = "belinha"

    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_insert_person():
    first_name = "Test name"
    last_name = "Test last name"
    age = 77
    pet_id = 2

    repo = PeopleRepository(db_connection_handler)
    repo.insert_person(first_name, last_name, age, pet_id)
