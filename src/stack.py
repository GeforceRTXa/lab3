class Node:
    def __init__(self, value):
        self.value = value
        self.link = None

class LinkedList:
    """
    Класс связного списка
    """
    def __init__(self):
        self.first = None
        self.min_arr = []

    def pop(self):
        """
        Удаление последнего элемента
        """
        if self.first is None:
            raise IndexError("Empty LinkedList")
        self.min_arr.pop()
        value = self.first.value
        self.first = self.first.link
        return value

    def push(self, value):
        """
        Добавление элемента
        :param value: Элемент, который надо добавить
        """
        if type(value) is not int and type(value) is not float:
            raise ValueError("Incorrect type of argument")
        if len(self.min_arr) == 0:
            self.min_arr.append(value)
        else:
            self.min_arr.append(min(value, self.min_arr[-1]))
        node = Node(value)
        node.link = self.first
        self.first = node

    def is_empty(self):
        """
        Проверка на пустоту массива
        :return: является ли массив пустым. Возвращает boolean
        """
        if self.first is None:
            return True
        return False

    def min(self):
        """
        :return: минимальный элемент списка
        """
        if self.is_empty():
            raise IndexError("LinkedList is empty")
        return self.min_arr[-1]

    def peek(self):
        """
        :return: Последний элемент списка
        """
        if self.is_empty():
            raise IndexError("LinkedList is empty")
        return self.first.value

    def __len__(self):
        """
        :return:  длина списка
        """
        return len(self.min_arr)
