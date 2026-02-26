from abc import abstractmethod, ABC
from typing import List
from sqlalchemy.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable


class PetsRepositoryInterface(ABC):
    @abstractmethod
    def list_pets(self) -> List[PetsTable]:
        pass

    @abstractmethod
    def delete_pets(self, name: str) -> None:
        pass