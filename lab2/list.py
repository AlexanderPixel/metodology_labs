class LinkedList:
    class Node:
        def __init__(self, element: str, next_node):
            self.element = element
            self.next_node = next_node

    def __init__(self):
        self.tail = None
        self.length = 0

    def append(self, element: str) -> None:
        if not self.tail:
            self.tail = self.Node(element, None)
            self.tail.next_node = self.tail
            self.length = 1
            return None

        new_node = self.Node(element, self.tail.next_node)

        self.tail.next_node = new_node
        self.tail = new_node

        self.length += 1
    
    def print(self):
        node = self.tail

        if not node:
            print('Nothing to print')
            return None

        for i in range(self.length):
            node = node.next_node
            print(node.element)

    def insert(self, index: int, element: str) -> None:
        if (index >= self.length or index < 0):
            raise IndexError  
            
        if(index == 0):
            previous_node = self.tail
        else:
            previous_node = self._get_node(index - 1)

        node = previous_node.next_node

        new_node = self.Node(element, next_node=node)

        previous_node.next_node = new_node
        
        self.length += 1

    def getLength(self):
        return self.length

    def get(self, index: int) -> str:
        if (index >= self.length or index < 0):
            raise IndexError 
        node = self._get_node(index)
        return node.element
    
    def delete(self, index: int):
        if (index >= self.length or index < 0):
            raise IndexError 

        if self.length <= 1:
            self.length = 0
            value = self.tail.element
            self.tail = None
            return value

        if index == 0:
            previous = self.tail
        else:
            previous = self._get_node(index - 1)
        
        current = previous.next_node
        next = current.next_node

        value = current.element

        previous.next_node = next

        if current == self.tail:
            self.tail == next

        self.length -= 1
        return value

    def deleteAll(self, element):
        i = 0
        while i < self.length:
            value = self.get(i)
            if value == element:
                self.delete(i)
                i -= 1
            i += 1

    def clone(self):
        new_list = LinkedList()
        for i in range(self.length):
            new_list.append(self.get(i))
        return new_list

    def reverse(self):
        if not self.tail or self.length == 1:
            return None

        new_tail = self.tail.next_node

        previous_node = self.tail
        current_node = previous_node.next_node
        next_node = current_node.next_node
        
        for i in range(self.length):
            current_node.next_node = previous_node

            previous_node = current_node
            current_node = next_node
            next_node = current_node.next_node

        self.tail = new_tail

    def findFirst(self, value):
        node = self.tail.next_node
        index = 0

        while index != self.length:
            if node.element == value:
                return index
        
            index += 1
            node = node.next_node
        
        return -1

    def findLast(self, value):
        node = self.tail.next_node
        index = 0
        last_index = -1
        while index != self.length:
            if node.element == value:
                last_index = index
        
            index += 1
            node = node.next_node
        
        return last_index

    def _get_node(self, index):
        if (index >= self.length or index < 0):
            raise IndexError      
        node = self.tail

        for i in range(index + 1):
            node = node.next_node
        return node
    
    def clear(self):
        self.tail.next_node = None
        self.tail = None
        self.length = 0

    def extend(self, lst):
        node = lst.tail.next_node
        while node.next_node != lst.tail.next_node:
            self.append(node.element)
            node = node.next_node
        self.append(lst.tail.element)
        return None