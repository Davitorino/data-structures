from linked_list.list_item import ListItem


class List:

    def __init__(self):
        self.__first: ListItem | None = None
        self.__last: ListItem | None = None
        self.__count = 0

    def get_first(self):
        self.__verify_list_empty()
        return self.__first.value

    def get_last(self):
        self.__verify_list_empty()
        return self.__last.value

    def get_by_pos(self, pos: int):
        self.__verify_list_empty()
        self.__verify_position(pos)
        actual = self.__first
        for cur_pos in range(1, pos+1):
            if cur_pos == pos:
                return actual.value
            actual = actual.next

    def get_by_value(self, value):
        self.__verify_list_empty()
        actual = self.__first
        for _ in range(self.__count):
            if actual.value == value:
                return actual.value
            actual = actual.next
        raise Exception('Value not found')

    def insert_first(self, value):
        item = ListItem(value)
        item.next = self.__first
        self.__first = item
        if self.__last is None:
            self.__last = item
        self.__count += 1

    def insert_last(self, value):
        item = ListItem(value)
        if self.__first is None:
            self.__first = item
        else:
            self.__last.next = item
        self.__last = item
        self.__count += 1

    def insert_by_pos(self, pos: int, value):
        self.__verify_position(pos)
        if pos == 1:
            self.insert_first(value)
            return
        item = ListItem(value)
        actual = self.__first
        for cur_pos in range(1, pos+1):
            if cur_pos+1 == pos:
                item.next = actual.next
                actual.next = item
                self.__count += 1
                if item.next is None:
                    self.__last = item
            actual = actual.next

    def remove_first(self):
        self.__verify_list_empty()
        first = self.__first
        self.__first = self.__first.next
        if self.__first is None:
            self.__last = None
        self.__count -= 1
        return first.value

    def remove_last(self):
        self.__verify_list_empty()
        if self.__first is self.__last:
            return self.remove_first()
        actual = self.__first
        for _ in range(self.__count - 1):
            if actual.next is self.__last:
                last = actual.next
                actual.next = None
                self.__last = actual
                self.__count -= 1
                return last.value
            actual = actual.next

    def remove_by_pos(self, pos: int):
        self.__verify_list_empty()
        self.__verify_position(pos)
        if pos == 1:
            return self.remove_first()
        actual = self.__first
        for cur_pos in range(1, pos):
            if cur_pos+1 == pos:
                removed = actual.next
                actual.next = removed.next
                self.__count -= 1
                if removed is self.__last:
                    self.__last = actual
                return removed.value
            actual = actual.next

    def remove_by_value(self, value):
        self.__verify_list_empty()
        if self.__first.value == value:
            return self.remove_first()
        actual = self.__first
        for _ in range(self.__count - 1):
            if actual.next.value == value:
                removed = actual.next
                actual.next = removed.next
                self.__count -= 1
                if removed is self.__last:
                    self.__last = actual
                return removed
            actual = actual.next
        raise Exception('Value not found')

    def __verify_list_empty(self):
        if self.__first is None:
            raise Exception('List is empty')

    def __verify_position(self, position: int):
        if position < 1 or position > self.__count:
            raise Exception('Position out of bounds')
