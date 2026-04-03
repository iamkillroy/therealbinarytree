class BinarySearchTree:
    """A class for making a binary seach tree, fully self contained"""

    # By Lucas Frias
    class BinaryNode:
        def __init__(self, entry) -> None:
            self._right = None
            self._left = None
            self._entry = entry

        # various functions for returning relevant node data
        def has_left(self):
            return True if self._left is not None else False

        def has_right(self):
            return True if self._right is not None else False

        def branch_count(self):
            return int(self.has_left()) + int(self.has_right())

        def get_left(self):
            return self._left

        def get_right(self):
            return self._right

        def get_entry(self):
            return self._entry

        def set_left(self, node):
            self._left = node

        def set_right(self, node):
            self._right = node

        def set_entry(self, entry):
            self._entry = entry

    def __init__(self) -> None:
        self._root = None
        self._len = 0

    def add(self, entry):
        """This function will add the entry to the BST"""
        if self._root is None:
            self._root = BinarySearchTree.BinaryNode(entry)
            return  # return, we've addded the first element
        self._rec_add(entry, currentNode=self._root)

    def _rec_add(self, entry, currentNode):
        """Recursively adds based on the currentNode"""
        # first, let's check if the current node is == to our value
        if currentNode.get_entry() == entry:
            # that's bad no duplicates allowed
            raise KeyError("Duplciate element cannot be added to BinarySearchTree")

        if currentNode.entry < entry:
            # we wanna go right
            # let's check if we can
            if not currentNode.has_right():
                # we can just set it no fuss and end the add
                currentNode.set_right(BinarySearchTree.BinaryNode(entry))
                return
            else:
                # so there is a right.
                # either the right is bigger than us or we're bigger than it.
                self._rec_add(entry, currentNode.get_right())
        elif currentNode.entry > entry:
            if not currentNode.has_left():
                # we can just set it no fuss and end the add
                currentNode.has_left(BinarySearchTree.BinaryNode(entry))
                return
            else:
                # so there is a right.
                # either the right is bigger than us or we're bigger than it.
                self._rec_add(entry, currentNode.get_left())
        else:
            raise Exception("Incorrect entry type")
        return
