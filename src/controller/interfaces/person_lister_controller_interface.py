from abc import abstractmethod, ABC
from typing import Dict, List

from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface

class PetListerControllerInterface(ABC):

    @abstractmethod
    def list(self) -> Dict:
        pass