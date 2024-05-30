class LengthConverter:
    def __init__(self):
        self.__meter = 0

    @property
    def meter(self):
        return self.__meter

    @property
    def feet(self):
        return self.__meter * 3.28084

    @property
    def inch(self):
        return self.__meter * 39.3701

    @meter.setter
    def meter(self, value):
        self.__meter = value

    @feet.setter
    def feet(self, value):
        self.__meter = value / 3.28084

    @inch.setter
    def inch(self, value):
        self.__meter = value / 39.3701
