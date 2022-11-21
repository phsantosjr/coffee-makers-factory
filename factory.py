from dataclasses import dataclass

from enums import CoffeeMakers
from interface import CoffeeMaker


@dataclass
class Aeropress(CoffeeMaker):
    def brew(self):
        super().brew(make='Aeropress')


@dataclass
class AutoDripMachine(CoffeeMaker):
    def brew(self):
        super().brew(make='AutoDripMachine')


@dataclass
class Chemex(CoffeeMaker):
    def brew(self):
        super().brew(make='Chemex')


@dataclass
class Clever(CoffeeMaker):
    def brew(self):
        super().brew(make='Clever')


@dataclass
class CoffeeBag(CoffeeMaker):
    def brew(self):
        super().brew(make='CoffeeBag')


@dataclass
class ColdDrip(CoffeeMaker):
    def brew(self):
        super().brew(make='ColdDrip')


@dataclass
class Cowboy(CoffeeMaker):
    def brew(self):
        super().brew(make='Cowboy')


@dataclass
class Espresso(CoffeeMaker):
    def brew(self):
        super().brew(make='Espresso')


@dataclass
class FrenchPress(CoffeeMaker):
    def brew(self):
        super().brew(make='FrenchPress')


@dataclass
class Ibrik(CoffeeMaker):
    def brew(self):
        super().brew(make='Ibrik')


@dataclass
class Moka(CoffeeMaker):
    def brew(self):
        super().brew(make='Moka')



@dataclass
class Percolator(CoffeeMaker):
    def brew(self):
        super().brew(make='Percolator')


@dataclass
class Siphon(CoffeeMaker):
    def brew(self):
        super().brew(make='Siphon')


@dataclass
class SoftBrew(CoffeeMaker):
    def brew(self):
        super().brew(make='SoftBrew')


@dataclass
class VietnameseDripFilter(CoffeeMaker):
    def brew(self):
        super().brew(make='VietnameseDripFilter')


class CoffeMakerFactory:
    def get_maker(self, coffee_maker: CoffeeMaker):
        list_of_makers = {
            CoffeeMakers.Aeropress: Aeropress,
            CoffeeMakers.AutoDripMachine: AutoDripMachine,
            CoffeeMakers.Chemex: Chemex,
            CoffeeMakers.Clever: Clever,
            CoffeeMakers.CoffeeBag: CoffeeBag,
            CoffeeMakers.ColdDrip: ColdDrip,
            CoffeeMakers.Cowboy: Cowboy,
            CoffeeMakers.Espresso: Espresso,
            CoffeeMakers.FrenchPress: FrenchPress,
            CoffeeMakers.Ibrik: Ibrik,
            CoffeeMakers.Moka: Moka,
            CoffeeMakers.Percolator: Percolator,
            CoffeeMakers.Siphon: Siphon,
            CoffeeMakers.SoftBrew: SoftBrew,
            CoffeeMakers.VietnameseDripFilter: VietnameseDripFilter,
        }
        return list_of_makers.get(coffee_maker)