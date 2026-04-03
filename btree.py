class BinarySearchTree:
    """A class for making a binary seach tree"""
    class BinaryNode:
        def __init__(self, entry ) -> None:
            self._right = None
            self._left = None
            self._entry = entry
        #various functions for returning relevant node data
        def has_left(self): return True if self._left is not None else False
        def has_right(self): return True if self._right is not None else False
        def branch_count(self): return int(self.has_left()) + int(self.has_right())
        def get_left(self): return self._left
        def get_right(self): return self._right
        def get_entry(self): return self._entry
        def set_left(self, node): self._left = node
        def set_right(self, node): self._right = node
        def set_entry(self, entry): self._entry = entry
        
    def __init__(self) -> None:
