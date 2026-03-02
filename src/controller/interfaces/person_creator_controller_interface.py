import re
from abc import abstractmethod, ABC
from typing import Dict

from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface


class PersonCreatorControllerInterface(ABC):

    @abstractmethod
    def create(self, person_info: Dict) -> Dict:
        pass