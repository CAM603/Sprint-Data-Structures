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
        # Iterative version
        # First previous will be None
        # First node will be the head
        # Set nodes next to its prev
        # prev_node = prev
        # current = self.head
        # while current:
        #     # capture the current node's next node
        #     next_node = current.get_next()
        #     # set the current node's next node to the previous node
        #     current.set_next(prev_node)
        #     # set the previous node to the current node
        #     prev_node = current
        #     # set the current node to the next nnode
        #     current = next_node
        # # Update head as the previous node
        # self.head = prev_node

        # Recursive version
        # If node is none, don't do anything
        # This will happen when we reach the tail node
        # and try to invoke reverse_list with its next_node (which is None)
        if node is None:
            return
        # If the node is the tail, set it to the head
        # The current tail's get next value will be None
        if node.get_next() is None:
            # Set to head
            self.head = node
            # The current node's next node will be its previous
            node.set_next(prev)
            return
        # Capture the current node's next node
        next_node = node.get_next()
        # The current node's next node will be its previous
        node.set_next(prev)
        # Call method again with the next node as the node and the node itself as the previous node
        self.reverse_list(next_node, node)

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next_node


list = LinkedList()
list.add_to_head(5)
list.add_to_head(4)
list.add_to_head(3)
list.add_to_head(2)
list.add_to_head(1)
list.print_list()
list.reverse_list(list.head, None)
list.print_list()
