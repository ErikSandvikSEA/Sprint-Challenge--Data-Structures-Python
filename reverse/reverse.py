class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # check for empty
        if not node:
            return None

        # check for just a single node
        if not node.next_node and not prev:
            return node
        # check to see if we're at the tail
        if not node.next_node:
            # set the tail to the head (first flip)
            self.head = node

            # swap the next and prev
            node.next_node = prev

            return

        # if we're not yet to the tail of the list ..
        # capture a temp next variable
        temp_next = node.next_node

        # swap prev and next
        node.next_node = prev

        # then call recursively on the next node
        self.reverse_list(temp_next, node)
