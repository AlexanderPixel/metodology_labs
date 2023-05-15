class Node:
    def __init__(self, element):
        self.element = element

class LinkedList(list):
    def __init__(self):
        pass

    def append(self, element: str) -> None:
        super().append(Node(element))

    def print(self) -> None:
        if self.get_length == 0:
            print('Nothing to print')
        else:
            for node in self:
                print(node.element)
    

    def get_length(self) -> int:
        return len(self)

    def find_first(self, item:str) -> int:
        for i in range(len(self)):
            if self[i].element == item:
                return i

    def find_last(self, item: str) -> int:
        last_index = -1
        for i in range(len(self)):
            if self[i].element == item:
                last_index = i
        return last_index

    def insert(self, index: int, element: str) -> None:
        if (index >= len(self) or index < 0):
            raise IndexError
        super().insert(index, Node(element))

    def get(self, index:int) -> str:
        if (index >= len(self) or index < 0):
            raise IndexError
        return self[index].element

    def clone(self) -> list:
        new_list = LinkedList()
        for i in range(len(self)):
            new_list.append(self.get(i))
        return new_list

    def reverse(self) -> None:
        super().reverse()

    def extend(self, lst:list) -> None:
        super().extend(lst)

    def delete_all(self, value:str) -> None:
        i = 0
        while i < len(self):
            if self[i].element == value:
                self.delete(i)
                i -= 1
            i += 1

    def delete(self, index: int) -> None:
        if (index >= len(self) or index < 0):
            raise IndexError
        item = self[index]
        del self[index]
        return item.element

    def clear(self) -> None:
        super().clear()

    def _get_node(self, index):
        if (index >= len(self) or index < 0):
            raise IndexError
        return self[index]