from abc import abstractmethod, ABC


# -------- Class Implementation --------- #
class Duck:
    def __init__(self, ifly):
        self.ifly = ifly

    def fly(self):
        return self.ifly.fly()


# Fly Interface
class IFly(ABC):

    @abstractmethod
    def fly(self):
        pass


class CityFly(IFly):

    def fly(self):
        print("Flying like a city duck")


class MountainFly(IFly):

    def fly(self):
        print("Flying like a mountain duck")


# -------- Func Implementation --------- #
class Cat:
    def __init__(self, iwalk):
        self.iwalk = iwalk

    def walk(self):
        self.iwalk()


def walk_sneaky_strategy():
    print("Walking like a ninja cat")


def walk_laudly_strategy():
    print("Walking like a floppy cat")


if __name__ == '__main__':
    cat = Cat(walk_sneaky_strategy)
    duck = Duck(CityFly())

    cat.walk()
    duck.fly()

