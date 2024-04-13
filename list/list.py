from list_item import ListItem


class List:

    def __init__(self):
        self.__first = None
        self.__last = None

    def get_first(self):
        return self.__first

    def get_last(self):
        return self.__last

    def get_from_pos(self, pos: int):
        if pos <= 0:
            raise Exception('Invalid position')
        self.__verify_list_empty()
        if pos == 1:
            return self.__first
        counter = 2
        actual = self.__first
        while actual.next:
            if pos == counter:
                return actual.next
        raise Exception('Position out of range')

    def insert_first(self, value):
        item = ListItem(value)
        item.next = self.__first
        self.__first = item
        if self.__last is None:
            self.__last = item

    def insert_last(self, value):
        item = ListItem(value)
        if self.__first is None:
            self.__first = item
        else:
            self.__last.next = item
        self.__last = item

    def remove_first(self):
        self.__verify_list_empty()
        self.__first = self.__first.next
        if self.__first is None:
            self.__last = None

    def remove_from_pos(self, pos: int):
        if pos <= 0:
            raise Exception('Invalid position')
        self.__verify_list_empty()
        if pos == 1:
            return self.remove_first()
        counter = 2
        actual = self.__first
        while actual.next:
            if counter == pos:
                actual.next = actual.next.next
                if actual.next is None:
                    self.__last = actual
                return
            actual = actual.next
            counter += 1
        raise Exception('Position out of range')

    def __verify_list_empty(self):
        if self.__first is None:
            raise Exception('List is empty')
