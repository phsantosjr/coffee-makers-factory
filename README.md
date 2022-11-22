# Coffee Maker - Factory #
![](https://img.shields.io/badge/Python-3.10.8-blue.svg)

Project to show a simple use of the Factory Design Pattern


### Whats is Factory ?

>In object-oriented programming, the term factory means a class that is responsible for >creating objects of other types. Typically, the class that acts as a factory has an  >object and methods associated with it. The client calls this method with certain  >parameters; objects of desired types are created in turn and returned to the client by >the factory.
>(Giridhar, Chetan - Learning Python Design Patterns)

### How to Run

- create your virtual environment
- install requirements `pip install requirements.txt`
- run tests `pytest`
- run main.py `python main.py`


### What we improved in a real project using Factory

Our system connects in few third part applications to execute some operations.

To make the code clean and easy to maintain we decided to use Factory to create our objects wich connects in these applications.
Each application is a sub-class for a ABC class where were created a shape to represent almost all methods for these applications. Something like that:

```
from abc import ABC


class ThirdPartApplication(ABC):
    def post(self):
        ...

    def get(self):
        ...

    def put(self):
        ...

    def delete(self):
        ...

```

Or you can create the abstract class with a raise error:

```
class ThirdPartApplication(ABC):
    def post(self):
        raise NotImplementedError("This method was not implemented")

```


Each class application was created like that:

```
class ApplicationA(ThirdPartApplication):
    def post(self):
        execute_post()

    def get(self):
        execute_get()

    def put(self):
        execute_put()

    def delete(self):
        execute_get()

```

And so we create our class to handle create the object

```
class Applications(Enum):
    ApplicationA: auto(),
    ApplicationB: auto()


class ThirdPartFactory:
    def get_object(sefl, id_application: Applications):
        list_applications: {
            Applications.ApplicationA: ApplicationA,
            Applications.ApplicationB: ApplicationB,
        }
        return list_applications.get(id_application)

```

Where you need to call your factory, do this.
```
factory = ThirdPartFactory()
app_class = factory.get_object(Applications.ApplicationA)
response = app_class.get()

```

### Source

[Real Python](https://realpython.com/factory-method-python/)

[Refactoring Guru](https://refactoring.guru/design-patterns/factory-method/python/example)

[Learning Python Design Patterns](https://www.amazon.com/Learning-Python-Design-Patterns-Second-ebook/dp/B018XYKNOM/ref=sr_1_1)