
class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        level = 0

        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def printTree(self, s='both'):
        if s.lower() == "both":
            value = self.name + " (" + self.designation + ")"
        elif s.lower() == "name":
            value = self.name
        elif s.lower() == "designation":
            value = self.designation
            
        spaces = " " * self.getLevel() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.printTree(s)

    


def build_management_tree():
    root = TreeNode('Alamgir', 'CEO')

    cto = TreeNode("Dhaval", "CTO")
    ishead = TreeNode("Vishwa", "Infrastructure Head")
    ishead.addChild(TreeNode("Vishwa", "Cloud Manager"))
    ishead.addChild(TreeNode("Chinmay", "Application Manager"))

    apphead = TreeNode("Waqas", "Application Head")

    hr = TreeNode("Joel", "HR Head")

    hr.addChild(TreeNode("Peter", "Recruitment Manager"))
    hr.addChild(TreeNode("Abhijit", "Policy Manager"))

    cto.addChild(ishead)
    cto.addChild(apphead)


    root.addChild(cto)
    root.addChild(hr)

    return root

if __name__ == '__main__':
    root = build_management_tree()
    root.printTree("designation")
