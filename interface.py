from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class CoffeeMaker(ABC):
    @abstractmethod
    def brew(self, make: str):
        print(f'Making your coffee in {make}')

