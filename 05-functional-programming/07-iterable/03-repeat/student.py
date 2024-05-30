class Repeat:
    def __init__(self, value):
        self.__value = value

    def __next__(self):
        return self.__value

    def __iter__(self):
        return self
