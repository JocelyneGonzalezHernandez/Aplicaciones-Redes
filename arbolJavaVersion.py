class Tree:
    def __init__(self, newValue):
        self.value = newValue
        self.father = None
        self.left = None
        self.right = None

    def add_child(self, newValue):
        if newValue < self.value:
            if self.left == None:
                self.left = Tree(newValue)
                self.left.father = self
            else:
                self.left.add_child(newValue)
        else:
            if self.right == None:
                self.right = Tree(newValue)
                self.right.father = self
            else:
                self.right.add_child(newValue)

    def add_child_tree(self, new_tree):
        if new_tree.value < self.value:
            if self.left == None:
                self.left = new_tree
                new_tree.father = self
            else:
                self.left.add_child_tree(new_tree)
        else:
            if self.right == None:
                self.right = new_tree
                new_tree.father = self
            else:
                self.right.add_child_tree(new_tree)

    def pre_order(self):
        print(self.value, end=" ")
        if self.left != None:
            self.left.pre_order()
        if self.right != None:
            self.right.pre_order()

    def in_order(self):
        if self.left != None:
            self.left.in_order()
        print(self.value, end=" ")
        if self.right != None:
            self.right.in_order()

    def post_order(self):
        if self.left != None:
            self.left.post_order()
        if self.right != None:
            self.right.post_order()
        print(self.value, end=" ")

    def search_value(self, value):
        
        if value == self.value:
            return self
        else:
            if value < self.value:
                if self.left != None:
                    return self.left.search_value(value)
                else:
                    return None
            else:
                if self.right != None:
                    return self.right.search_value(value)
                else:
                    return None
              

    def search_minimum(self):
        if self.left != None:
            return self.left.search_minimum()
        else:
            return self

    def delete(self, value):
        node_to_delete = self.search_value(value)
        if node_to_delete != None:
            print("Deleting node", value)
            the_father = node_to_delete.father
            if the_father:
                if not node_to_delete.left and not node_to_delete.right:
                    if the_father.left == node_to_delete:
                        the_father.left = None
                    else:
                        the_father.right = None
                elif node_to_delete.left and not node_to_delete.right:
                    if the_father.left == node_to_delete:
                        the_father.left = node_to_delete.left
                    else:
                        the_father.right = node_to_delete.left
                    node_to_delete.left.father = the_father
                elif not node_to_delete.left and node_to_delete.right:
                    if the_father.left == node_to_delete:
                        the_father.left = node_to_delete.right
                    else:
                        the_father.right = node_to_delete.right
                    node_to_delete.right.father = the_father
                else:
                    minimum = node_to_delete.right.search_minimum()
                    if minimum == node_to_delete.right:
                        if the_father.left == node_to_delete:
                            the_father.left = minimum
                        else:
                            the_father.right = minimum
                        minimum.father = the_father
                        minimum.add_child_tree(node_to_delete.left)
                    else:
                        node_to_delete.value = minimum.value
                        node_to_delete.right.delete(minimum.value)
            else:
                print("Can not delete a root node!!!")
        else:
            print("There is no node", value, "to delete")


    def __str__(self):
        father_value = self.father.value if self.father else "root"
        left_value = self.left.value if self.left else "-"
        right_value = self.right.value if self.right else "-"
        return f"This: {self.value} Father: {father_value} Left: {left_value} Right: {right_value}"


# Example usage:
if __name__ == "__main__":
    root = Tree('M')
    root.add_child('F')
    root.add_child('E')
    root.add_child('C')
    root.add_child('D')
    root.add_child('I')
    root.add_child('H')
    root.add_child('L')
    root.add_child('R')
    root.add_child('W')
    root.add_child('T')
    root.add_child('S')
    root.add_child('X')
    root.add_child('Z')
    
    print("Pre-order traversal:")
    root.pre_order()
    print("\nIn-order traversal:")
    root.in_order()
    print("\nPost-order traversal:")
    root.post_order()

    root.delete('Z')
    print("\nIn-Order After deleting Z:")
    root.in_order()
