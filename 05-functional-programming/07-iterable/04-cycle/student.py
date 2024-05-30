class Cycle:
    def __init__(self, iter):
        self.__iter = iter
        self.__current_index = 0

    def __next__(self):
        if self.__current_index == len(self.__iter):
            self.__current_index = 0

        result = self.__iter[self.__current_index]

        self.__current_index += 1

        return result

    def __iter__(self):
        return self
