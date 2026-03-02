from src.controller.interfaces.pet_deleter_controller_interface import PetDeleterControllerInterface
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetDeleterController(PetDeleterControllerInterface):
    def __init__(self, pet_repository: PetsRepositoryInterface):
        self.__pet_repository = pet_repository

    def delete(self, name: str) -> None:
        self.__pet_repository.delete_pets(name)