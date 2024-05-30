from datetime import date


class Calendar:
    def __init__(self):
        pass

    @property
    def today(self):
        return date.today()


class CalendarStub:
    def __init__(self, today):
        self.__today = today

    @property
    def today(self):
        return self.__today

    @today.setter
    def today(self, value):
        self.__today = value
