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

    def printTree(self, level):
        if self.get_level() > level:
            return
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix,self.data)
        if self.children:
            for child in self.children:
                child.printTree(level)


def build_tree():
    root = TreeNode("Global")

    usa = TreeNode("USA")
    new_jersey = TreeNode("New Jersey")
    new_jersey.addChild(TreeNode("Princeton"))
    new_jersey.addChild(TreeNode("Trenton"))


    california = TreeNode("California")
    california.addChild(TreeNode("San Francisco"))
    california.addChild(TreeNode("Mountain View"))
    california.addChild(TreeNode("Palo Alto"))

    usa.addChild(new_jersey)
    usa.addChild(california)


    india = TreeNode("India")
    gujrat = TreeNode("Gujrat")
    gujrat.addChild(TreeNode("Ahmedabad"))
    gujrat.addChild(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.addChild(TreeNode("Bangluru"))
    karnataka.addChild(TreeNode("Mysore"))

    india.addChild(gujrat)
    india.addChild(karnataka)

    root.addChild(usa)
    root.addChild(india)

    return root


if __name__ == "__main__":
    root = build_tree()
    root.printTree(3)