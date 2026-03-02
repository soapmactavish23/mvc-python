from abc import abstractmethod, ABC
from typing import Dict

from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface


class PersonFinderControllerInterface(ABC):
    @abstractmethod
    def find(self, person_id: int) -> Dict:
        pass