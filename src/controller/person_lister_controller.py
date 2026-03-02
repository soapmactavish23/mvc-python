from typing import Dict, List

from src.controller.interfaces.person_lister_controller_interface import PetListerControllerInterface
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetListerController(PetListerControllerInterface):
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def list(self) -> Dict:
        pets = self.__get_pets_in_db()
        return self.__format_response(pets)

    def __get_pets_in_db(self) -> List[PetsTable]:
        return self.__pet_repository.list_pets()

    def __format_response(self, pets: List[PetsTable]) -> Dict:
        formatted_pets = []
        for pet in pets:
            formatted_pets.append({"name": pet.name, "id": pet.id, "type": pet.type})

        return {
            "data": {
                "type": "Pets",
                "count": len(formatted_pets),
                "attributes": formatted_pets
            }
        }