from dataclasses import dataclass
from abc import ABC

@dataclass
class CoffeeMaker(ABC):
    def brew(self, make: str):
        print(f'Making your coffee in {make}')

