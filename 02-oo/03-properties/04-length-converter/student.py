class LengthConverter:
    def __init__(self):
        self.__distance_in_meter = 0

    @property
    def meter(self):
        return self.__distance_in_meter

    @meter.setter
    def meter(self, value):
        if value >= 0:
            self.__distance_in_meter = value
        else:
            raise ValueError("Mesurement cannot be negative")

    @property
    def feet(self):
        return self.__distance_in_meter * 3.28084

    @feet.setter
    def feet(self, value):
        if value >= 0:
            self.__distance_in_meter = value / 3.28084
        else:
            raise ValueError("Mesurement cannot be negative")

    @property
    def inch(self):
        return self.__distance_in_meter * 39.3701

    @inch.setter
    def inch(self, value):
        if value >= 0:
            self.__distance_in_meter = value / 39.3701
        else:
            raise ValueError("Mesurement cannot be negative")
