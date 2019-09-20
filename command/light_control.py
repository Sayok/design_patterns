import abc


class RControl:

    def __init__(self, turn_on, turn_up):
        self._turn_on = turn_on
        self._turn_up = turn_up

    def turn_on(self):
        self._turn_on.execute()

    def turn_off(self):
        self._turn_on.unexecute()

    def turn_up(self):
        self._turn_up.execute()

    def turn_down(self):
        self._turn_up.unexecute()


class ICommand(metaclass=abc.ABCMeta):

    def __init__(self, reciever):
        self._reciever = reciever

    @abc.abstractmethod
    def execute(self):
        pass

    @abc.abstractmethod
    def unexecute(self):
        pass


class TurnOn(ICommand):

    def execute(self):
        self._reciever.light = True

    def unexecute(self):
        self._reciever.light = False


class TurnUp(ICommand):

    def execute(self):
        self._reciever.brightness = 100

    def unexecute(self):
        self._reciever.brightness = 50


class BulbController:

    def __init__(self):
        self._light = False
        self._brightness = 100

        self.__initialized = True

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if hasattr(self, '__initialized') and not key == '__initialized':
            print(f"Print setting {key} to {value}")


def create_controller():
    reciever = BulbController()
    controller = RControl(TurnOn(reciever), TurnUp(reciever))
    return controller
