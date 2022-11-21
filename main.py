
from enums import CoffeeMakers
from factory import CoffeMakerFactory

def main():
    factory = CoffeMakerFactory()

    for make in CoffeeMakers:
        make_type = factory.get_maker(make)
        m = make_type()
        m.brew()


if __name__ == '__main__':
    main()

