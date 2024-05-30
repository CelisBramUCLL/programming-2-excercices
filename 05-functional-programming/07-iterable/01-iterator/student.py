class InclusiveRange:
    def __init__(self, min, max):
        self.__list = [i for i in range(min, max + 1)]

    def __iter__(self):
        return InclusiveRangeIterator(self.__list)


class InclusiveRangeIterator:
    def __init__(self, list):
        self.__elts = list
        self.__current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Check if we reached the end
        if self.__current_index == len(self.__elts):
            # Raise StopIteration to notify user end of list has been reached
            raise StopIteration()
        # Fetch current element
        result = self.__elts[self.__current_index]
        # Move over to next element in list
        self.__current_index += 1
        # Return fetched element
        return result
