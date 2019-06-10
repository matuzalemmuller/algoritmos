# UFSC - Campus Trindade
# PPGEAS - Introducao a Algoritmos
# Matuzalem Muller dos Santos
# 2019/1
from random import randint

class Node:  
    def __init__(self, level = 0, value = None):
        self.value = value
        self.next = [None]*level

class SkipList:

    def __init__(self):
        self.head = Node()
        self.len = 0
        self.maxlevel = 0

    # 50 percent chance of increasing by one level on each iteration
    def _random_level(self):
        level = 1
        while randint(0, 1) != 1:
            level += 1
        return level

    # Finds and returns node if found
    def _find(self, value, update = None):
        if update == None:
            update = self._update_list(value)
        if len(update) > 0:
            item = update[0].next[0]
            if item != None and item.value == value:
                return item
        return None

    # Returns list of nodes in each level that contains the greatest value
    # that is smaller than the node
    def _update_list(self, value):
        update = [None]*self.maxlevel
        x = self.head
        for i in reversed(range(self.maxlevel)):
            while x.next[i] != None and x.next[i].value < value:
                x = x.next[i]
            update[i] = x
            
        return update

    # Inserts element in skip list
    def insert(self, value):
        _node = Node(self._random_level(), value)

        self.maxlevel = max(self.maxlevel, len(_node.next))
        while len(self.head.next) < len(_node.next):
            self.head.next.append(None)

        update = self._update_list(value)
        find = self._find(value, update)
        if find == None:
            for i in range(len(_node.next)):
                _node.next[i] = update[i].next[i]
                update[i].next[i] = _node
            self.len += 1

    # Remove element from skip list
    def remove(self, value):

        update = self._update_list(value)
        x = self._find(value, update)
        if x != None:
            for i in reversed(range(len(x.next))):
                update[i].next[i] = x.next[i]
                if self.head.next[i] == None:
                    self.maxlevel -= 1
            self.len -= 1

    # Searches node in list
    # Returns True if value if found and False if not found
    def search(self, value):
        find = self._find(value)
        return find != None

    # Print skip list
    def print(self):
        for i in range(len(self.head.next)-1, -1, -1):
            x = self.head
            while x.next[i] != None:
                print(x.next[i].value, end=' ')
                x = x.next[i]
            print('')


if __name__ == '__main__': 
    skip = SkipList()
    skip.insert(1)
    skip.insert(2)
    skip.insert(3)
    skip.insert(4)
    skip.insert(5)
    skip.insert(6)
    skip.insert(7)
    skip.insert(8)
    skip.insert(9)
    skip.insert(10)
    skip.insert(11)
    skip.insert(12)
    skip.insert(13)
    skip.insert(14)
    skip.insert(15)
    skip.insert(16)
    skip.insert(17)
    skip.insert(17)
    skip.insert(19)
    skip.insert(20)

    skip.print()
    skip.remove(2)
    print("===============")
    skip.print()