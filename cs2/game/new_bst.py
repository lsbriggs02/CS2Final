class BST:
    def __init__(self, init_vals=None):
        self._root = None
        self._size = 0
        self._pull_from_left = True
        if init_vals is not None:
            for val in init_vals:
                self.add(val)

    def add(self, value):
        if self._root is None:
            self._root = _Node(value)
            self._size += 1
            return True
        return self._add(self._root, _Node(value))

    def _add(self, sub_root, node):
        if node.val == sub_root.val:
            return False
        elif node.val < sub_root.val:
            if sub_root.lc is None:
                sub_root.lc = node
                node.par = sub_root
                self._size += 1
                return True
            return self._add(sub_root.lc, node)
        else:
            if sub_root.rc is None:
                sub_root.rc = node
                node.par = sub_root
                self._size += 1
                return True
            return self._add(sub_root.rc, node)

    def contains(self, value):
        if self._root is None:
            return False
        return self._contains(self._root, _Node(value))

    def _contains(self, sub_root, node):
        if sub_root is None:
            return False
        elif node.val == sub_root.val:
            return True
        elif node.val < sub_root.val:
            return self._contains(sub_root.lc, node)
        return self._contains(sub_root.rc, node)

    def level(self, value):
        if self._root is None:
            return -1
        return self._level(self._root, _Node(value), 1)

    def _level(self, sub_root, node, level):
        if sub_root is None:
            return -1
        elif node.val == sub_root.val:
            return level
        elif node.val < sub_root.val:
            return self._level(sub_root.lc, node, level + 1)
        return self._level(sub_root.rc, node, level + 1)

    def in_order_traversal(self):
        t_list = []
        if self._root is None:
            return t_list
        self._in_order_traversal(self._root, t_list)
        return t_list

    def _in_order_traversal(self, sub_root, t_list):
        if sub_root is None:
            return
        self._in_order_traversal(sub_root.lc, t_list)
        t_list.append(sub_root.val)
        self._in_order_traversal(sub_root.rc, t_list)

    def reverse_order_traversal(self):
        t_list = []
        if self._root is None:
            return t_list
        self._reverse_order_traversal(self._root, t_list)
        return t_list

    def _reverse_order_traversal(self, sub_root, t_list):
        if sub_root is None:
            return
        self._reverse_order_traversal(sub_root.rc, t_list)
        t_list.append(sub_root.val)
        self._reverse_order_traversal(sub_root.lc, t_list)

    def pre_order_traversal(self):
        t_list = []
        if self._root is None:
            return t_list
        self._pre_order_traversal(self._root, t_list)
        return t_list

    def _pre_order_traversal(self, sub_root, t_list):
        if sub_root is None:
            return
        t_list.append(sub_root.val)
        self._pre_order_traversal(sub_root.lc, t_list)
        self._pre_order_traversal(sub_root.rc, t_list)

    def post_order_traversal(self):
        t_list = []
        if self._root is None:
            return t_list
        else:
            self._post_order_traversal(self._root, t_list)
            return t_list

    def _post_order_traversal(self, sub_root, t_list):
        if sub_root is None:
            return
        self._post_order_traversal(sub_root.lc, t_list)
        self._post_order_traversal(sub_root.rc, t_list)
        t_list.append(sub_root.val)

    def size(self):
        return self._size

    def clear(self):
        self._root = None
        self._size = 0

    def remove(self, value):
        if not self.contains(value):
            return -1
        elif self._size == 1:
            self._root = None
            self._size = 0
            return None
        self._size -= 1
        dead_node = self.useful_contains(value)
        if dead_node.par is None:
            is_lc = False
        else:
            is_lc = dead_node.par.lc == dead_node
        if dead_node.lc is None:
            if is_lc:
                dead_node.par.lc = dead_node.rc
                if dead_node.rc is not None:
                    dead_node.rc.par = dead_node.par
            else:
                if dead_node.par is None:
                    self._root = self._root.rc
                    self._root.par = None
                else:
                    dead_node.par.rc = dead_node.rc
                    if dead_node.rc is not None:
                        dead_node.rc.par = dead_node.par
        elif dead_node.rc is None:
            if is_lc:
                if dead_node.par is not None:
                    dead_node.par.lc = dead_node.lc
                dead_node.lc.par = dead_node.par
            else:
                if dead_node.par is not None:
                    dead_node.par.rc = dead_node.lc
                else:
                    self._root = dead_node.lc
                dead_node.lc.par = dead_node.par
        else:
            if self._pull_from_left:
                pointer = dead_node.lc
                while self._pull_from_left:
                    if pointer.rc is None:
                        self._pull_from_left = False
                    else:
                        pointer = pointer.rc
                dead_node.val = pointer.val
                if dead_node == pointer.par:
                    dead_node.lc = pointer.lc
                else:
                    pointer.par.rc = pointer.lc
                if pointer.lc is not None:
                    pointer.lc.par = pointer.par
            else:
                pointer = dead_node.rc
                while not self._pull_from_left:
                    if pointer.lc is None:
                        self._pull_from_left = True
                    else:
                        pointer = pointer.lc
                    dead_node.val = pointer.val
                if dead_node == pointer.par:
                    dead_node.rc = pointer.rc
                else:
                    pointer.par.lc = pointer.rc
                if pointer.rc is not None:
                    pointer.rc.par = pointer.par

    def get(self, value):
        if self._root is None:
            return None
        return self._get(self._root, value)

    def _get(self, sub_root, value):
        if sub_root is None:
            return None
        elif value == sub_root.val:
            return sub_root.val
        elif value < sub_root.val:
            return self._get(sub_root.lc, value)
        return self._get(sub_root.rc, value)

    def put(self, value):
        if self._root is None:
            self._root = _Node(value)
            self._size += 1
            return value
        return self._put(self._root, _Node(value))

    def _put(self, sub_root, node):
        if node.val == sub_root.val:
            hold = sub_root.val
            sub_root.val = node.val
            return hold
        elif node.val < sub_root.val:
            if sub_root.lc is None:
                sub_root.lc = node
                node.par = sub_root
                self._size += 1
                return node.val
            return self._put(sub_root.lc, node)
        else:
            if sub_root.rc is None:
                sub_root.rc = node
                node.par = sub_root
                self._size += 1
                return node.val
            return self._put(sub_root.rc, node)

    def useful_contains(self, value):
        if self._root is None:
            return False
        return self._useful_contains(self._root, _Node(value))

    def _useful_contains(self, sub_root, node):
        if sub_root is None:
            return False
        elif node.val == sub_root.val:
            return sub_root
        elif node.val < sub_root.val:
            return self._useful_contains(sub_root.lc, node)
        return self._useful_contains(sub_root.rc, node)

    def width(self, sub_root):
        if sub_root is None:
            return 0
        return self.width(sub_root.lc) + len(str(sub_root.val)) + self.width(sub_root.rc)

    def useful_in_order_traversal(self):
        t_list = []
        if self._root is None:
            return t_list
        self._useful_in_order_traversal(self._root, t_list)
        return t_list

    def _useful_in_order_traversal(self, sub_root, t_list):
        if sub_root is None:
            return
        self._useful_in_order_traversal(sub_root.lc, t_list)
        t_list.append(sub_root)
        self._useful_in_order_traversal(sub_root.rc, t_list)

    def find_all_at_level(self, level):
        t_list = []
        if self._root is None:
            return t_list
        self._find_all_at_level(self._root, t_list, level)
        return t_list

    def _find_all_at_level(self, sub_root, t_list, level):
        if sub_root is not None:
            if self.level(sub_root.val) == level:
                t_list.append(sub_root)
            else:
                self._find_all_at_level(sub_root.lc, t_list, level)
                self._find_all_at_level(sub_root.rc, t_list, level)

    def relation(self, sub_root1, sub_root2, greatness):
        if sub_root1.par == sub_root2.par:
            return greatness
        return self.relation(sub_root1.par, sub_root2.par, greatness + 1)

    def absolute_width(self, sub_root):
        return self.width(sub_root.lc) + self._absolute_width(sub_root)

    def _absolute_width(self, sub_root):
        if sub_root.par is None:
            return 0
        elif sub_root.par.lc == sub_root:
            return self._absolute_width(sub_root.par)
        else:
            return self.width(sub_root.par.lc) + len(str(sub_root.par.val)) + self._absolute_width(sub_root.par)

    def visualize(self, level, master):
        upper_current = 0
        lower_current = 0
        upper_str = ""
        lower_str = ""
        for trip in master:
            if trip[1] == level:
                lower_delta = trip[2] - lower_current
                lower_str += lower_delta * " " + str(trip[0].val)
                lower_current += lower_delta + len(str(trip[0].val))
                par_abs = -1
                i = 0
                if trip[0].par is None:
                    upper_str += trip[2] * " "
                else:
                    while par_abs < 0:
                        if master[i][0].val == trip[0].par.val:
                            par_abs = master[i][2]
                        i += 1
                    upper_delta = abs(trip[2] - par_abs)
                    if trip[0] == trip[0].par.lc:
                        if trip[0].par.rc is not None:
                            upper_str += (trip[2] - upper_current) * " " + "┌" + "─" * (upper_delta - 1) + "┴"
                            upper_current += len((trip[2] - upper_current) * " " + "┌" + "─" * (upper_delta - 1) + "┴")
                        else:
                            upper_str += (trip[2] - upper_current) * " " + "┌" + "─" * (upper_delta - 1) + "┘"
                            upper_current += len((trip[2] - upper_current) * " " + "┌" + "─" * (upper_delta - 1) + "┴")

                    elif trip[0].par.lc is not None:
                        upper_str += "─" * (upper_delta - 1) + "┐"
                        upper_current += len("─" * (upper_delta - 1) + "┐")
                    else:
                        upper_str += (trip[2] - upper_delta - upper_current) * " " + "└" + "─" * (upper_delta - 1) + "┐"
                        upper_current += len((trip[2] - upper_delta - upper_current) * " " + "┴" + "─" *
                                             (upper_delta - 1) + "┐")
        if lower_current == 0:
            return ""
        return upper_str + "\n" + lower_str + "\n" + self.visualize(level + 1, master)

    def clean_tree(self):
        if self._size <= 2:
            return None
        order = self.in_order_traversal()
        self.clear()
        new = [order[len(order) // 2]]
        for item in self._clean_tree(order[:len(order)//2]):
            new.append(item)
        for item in self._clean_tree(order[len(order)//2 + 1:]):
            new.append(item)
        for item in new:
            self.add(item)

    def _clean_tree(self, order):
        if len(order) == 1:
            return [order[0]]
        elif len(order) < 1:
            return []
        new = [order[len(order) // 2]]
        for item in self._clean_tree(order[:len(order)//2]):
            new.append(item)
        for item in self._clean_tree(order[len(order)//2 + 1:]):
            new.append(item)
        return new

    def __str__(self):
        if self._size == 0:
            return ""
        master = []
        for node in self.useful_in_order_traversal():
            master.append((node, self.level(node.val), self.absolute_width(node)))
        return self.visualize(1, master)

    def __iter__(self):
        self._list = self.in_order_traversal()
        self._int = 0
        return self

    def __next__(self):
        if self._int < self._size:
            self._int += 1
            return self._list[self._int - 1]
        raise StopIteration


class _Node:
    def __init__(self, value):
        self.val = value
        self.par = None
        self.lc = None
        self.rc = None
