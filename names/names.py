import time


class BSTNode:
    def __init__(self, value):
        self.value = value  # BinarySearchTree value
        self.left = None  # BinarySearchTree
        self.right = None  # BinarySearchTree

    # Insert the given value into the tree
    def insert(self, value):

        # Check if incomming value is lesss than current value
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        elif value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)
        elif target >= self.value:
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    # This is DEPTH FIRST, LIFO
    def for_each(self, fn):
        fn(self.value)
        if self.right is not None:
            # Call passed in function
            self.right.for_each(fn)
        # If there is a left child
        if self.left is not None:
            # Call passed in function
            self.left.for_each(fn)

    def in_order_print(self, node):
        if node is None:
            return
        if node.left:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.right.in_order_print(node.right)


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Return the list of duplicates in this data structure
# STRETCH
duplicates = list(set(names_1).intersection(set(names_2)))

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# my_BST = BSTNode("Cameron")

# for name in names_1:
#     my_BST.insert(name)

# for name in names_2:
#     if my_BST.contains(name):
#         duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
