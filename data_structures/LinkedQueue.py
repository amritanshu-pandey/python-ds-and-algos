from .exceptions import Empty


class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, _element, _next):
            self._element = _element
            self._next = _next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    @property
    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        new_node = self._Node(e, None)
        if self.is_empty:
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty:
            raise Empty('Queue is empty')
        else:
            return_value = self._head._element
            self._head = self._head._next
            self._size -= 1
        return return_value

    @property
    def first(self):
        if self.is_empty:
            raise Empty('Queue is empty')
        return self._head._element

    @property
    def last(self):
        if self.is_empty:
            raise Empty('Queue is empty')
        return self._tail._element

    def pop(self):
        if self.is_empty:
            raise Empty('Stack is empty')
        return_value = self._head._element
        self._head = self._head._next
        self._size -= 1
        return return_value

    def _print_all_elements(self):
        if self.is_empty:
            return '<empty>'

        temp_ptr = self._head
        return_value = ''
        while(True):
            if return_value:
                return_value = f'{return_value} -> {temp_ptr._element}'
            else:
                return_value = temp_ptr._element
            if temp_ptr._next:
                temp_ptr = temp_ptr._next
            else:
                break
        return return_value

    def __repr__(self):
        return self._print_all_elements()
