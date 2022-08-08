'''Tree Data Structures'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent
        
        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")

    laptops = TreeNode("Laptops")
    # Laptops Children
    laptops.addChild(TreeNode("DELL"))
    laptops.addChild(TreeNode("LENOVO"))
    laptops.addChild(TreeNode("HP"))

    cellphones = TreeNode("Cellphones")
    # Cellphones Children
    cellphones.addChild(TreeNode("Samsung"))
    cellphones.addChild(TreeNode("Apple"))
    cellphones.addChild(TreeNode("One+"))
    cellphones.addChild(TreeNode("Motorolla"))
    
    cameras = TreeNode("Cameras")
    cameras.addChild(TreeNode("Canon"))
    cameras.addChild(TreeNode("Nikkon"))
    cameras.addChild(TreeNode("Fuji"))
    
    # Add Children to Root
    root.addChild(laptops)
    root.addChild(cellphones)
    root.addChild(cameras)

    return root

if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
    