from typing import List, Any, Optional

class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.prev: Node = None
        self.next: Node = None


class LinkedList:
    def __init__(self, items: List[Any] = None):
        self.head: Node = None
        self.tail: Node = None
        self._size: int = 0

        if items:
            for item in items:
                self.push_back(item)

    def __len__(self) -> int:
        return self._size

    def push_front(self, data: Any):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            # list was empty; tail also becomes new_node
            self.tail = new_node
        self.head = new_node
        self._size += 1

    def push_back(self, data: Any):
        new_node = Node(data)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        else:
            # list was empty; head also becomes new_node
            self.head = new_node
        self.tail = new_node
        self._size += 1

    def pop_front(self) -> Optional[Any]:
        if not self.head:
            raise IndexError("pop_front from empty list")
        node = self.head
        self.head = node.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return node.data

    def pop_back(self) -> Optional[Any]:
        if not self.tail:
            raise IndexError("pop_back from empty list")
        node = self.tail
        self.tail = node.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return node.data

    def __getitem__(self, index: int) -> Any:
        """Return data at position `index`."""
        if index < 0 or index >= self._size:
            raise IndexError("LinkedList index out of range")

        # We can speed up some operations by choosing which
        # direction to walk from. If the index is closer to the start,
        # we walk starting from the beginning, else we walk backwards
        # starting from the end.
        if index < self._size // 2:
            cur = self.head
            for _ in range(index):
                cur = cur.next
        else:
            cur = self.tail
            steps = self._size - 1 - index
            for _ in range(steps):
                cur = cur.prev
        return cur.data
    
    def __setitem__(self, index: int, new_item: Any):
        """Modify data at position `index`."""
        if index < 0 or index >= self._size:
            raise IndexError("LinkedList index out of range")

        # We can speed up some operations by choosing which
        # direction to walk from. If the index is closer to the start,
        # we walk starting from the beginning, else we walk backwards
        # starting from the end.
        if index < self._size // 2:
            cur = self.head
            for _ in range(index):
                cur = cur.next
        else:
            cur = self.tail
            steps = self._size - 1 - index
            for _ in range(steps):
                cur = cur.prev
        cur.data = new_item