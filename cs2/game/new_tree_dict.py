from cs2.game.new_bst import BST


class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ": " + str(self.value)

    def __eq__(self, other):
        return self.key == other.key

    def __ne__(self, other):
        return self.key != other.key

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key <= other.key

    def __gt__(self, other):
        return self.key > other.key

    def __ge__(self, other):
        return self.key >= other.key


class CS2TreeDict:
    def __init__(self):
        self._tree = BST()

    def clear(self):
        self._tree = BST()

    def size(self):
        return self._tree.size()

    def put(self, key, value):
        return self._tree.put(Item(key, value))

    def get(self, key):
        return self._tree.get(Item(key, None))

    def keys(self):
        ret_list = []
        for item in self._tree:
            ret_list.append(item.key)

    def values(self):
        ret_list = []
        for item in self._tree:
            ret_list.append(item.value)

    def items(self):
        ret_list = []
        for item in self._tree:
            ret_list.append((item.key, item.val))
        return ret_list

    def clean(self):
        self._tree.clean_tree()

    def remove(self, key):
        self._tree.remove(Item(key, None))

    def __iter__(self):
        return self._tree.__iter__()

    def __next__(self):
        return self._tree.__next__()

    def __str__(self):
        ret_str = "{"
        for item in self._tree:
            ret_str += str(item.key) + ": " + str(item.value) + ", "
        return ret_str + "}"
