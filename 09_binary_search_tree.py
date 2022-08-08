'''Binary Search Tree'''


class BTSTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BTSTreeNode(data)

        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BTSTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # Visit Left Tree
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit Base Node
        elements.append(self.data)

        # Visit Right Tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        # Visit Left Tree
        if self.left:
            elements += self.left.post_order_traversal()

        # Visit Right Tree
        if self.right:
            elements += self.right.post_order_traversal()

        # Visit Base Node
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = []

        # Visit Base Node
        elements.append(self.data)

        # Visit Left Tree
        if self.left:
            elements += self.left.pre_order_traversal()

        # Visit Right Tree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def search(self, value):
        if value == self.data:
            return True

        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False

        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_min(self):
        if not self.left:
            return self.data
        if self.left:
            return self.left.find_min()

    def find_max(self):
        if not self.right:
            return self.data
        if self.right:
            return self.right.find_max()

    def calculate_sum(self):
        sum = self.data
        if self.left:
            sum += self.left.calculate_sum()

        if self.right:
            sum += self.right.calculate_sum()

        return sum

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)

        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    root = BTSTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.addChild(elements[i])

    return root


if __name__ == '__main__':
    countries = [100, 312, 412, 12, 1, 31, 312, 2, 7, 512, 256, 400, 128]
    country_tree = build_tree(countries)
    print("In-Order Traversal Tree", country_tree.in_order_traversal())
    # print("Post-Order Traversal Tree", country_tree.post_order_traversal())
    # print("Pre-Order Traversal Tree", country_tree.pre_order_traversal())
    country_tree.delete(312)
    print("In-Order Traversal Tree", country_tree.in_order_traversal())

    print("Sum: ", country_tree.calculate_sum())
