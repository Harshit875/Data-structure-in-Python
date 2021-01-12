class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        level = self.get_level()
        space = " " * level * 3
        prefixes = space + '|__' if self.parent else ''
        print(prefixes + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()


if __name__ == '__main__':
    build_product_tree()

# Building management hierarchy using Tree

class TreeNode:

    def __init__(self, name, designation):
        self.name = name
        self.dsn = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, par):
        level = self.get_level()
        space = " " * level * 3
        prefixes = space + '|__' if self.parent else ''
        if par == 'both':
            print(prefixes + self.name + " (" + self.dsn + ")")
        elif par == "name":
            print(prefixes + self.name)
        else:
            print(prefixes + self.dsn)
        if self.children:
            for child in self.children:
                child.print_tree(par)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_management_tree():
    # CTO Hierarchy
    infra_head = TreeNode("Vishwa", "Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    cto = TreeNode("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Gels", "HR Head")

    hr_head.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    ceo = TreeNode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name")
    root_node.print_tree("designation")
    root_node.print_tree("both")

# Printing tree upto a certain level

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, lev):
        level = self.get_level()
        if level <= lev:
            space = " " * level * 3
            prefixes = space + '|__' if self.parent else ''
            print(prefixes + self.data)
            if self.children:
                for child in self.children:
                    child.print_tree(lev)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_product_tree():
    Global = TreeNode("Global")
    India = TreeNode("India")

    Gujarat = TreeNode("Gujarat")
    Gujarat.add_child(TreeNode("Ahmedabad"))
    Gujarat.add_child(TreeNode("Baroda"))

    Karnataka = TreeNode("Karnataka")
    Karnataka.add_child(TreeNode("Bengaluru"))
    Karnataka.add_child(TreeNode("Mysore"))
    India.add_child(Gujarat)
    India.add_child(Karnataka)

    USA = TreeNode("USA")
    NJ = TreeNode("New Jersey")
    Cal = TreeNode("California")
    NJ.add_child(TreeNode("Princeton"))
    NJ.add_child(TreeNode("Trenton"))
    Cal.add_child(TreeNode("San Francisco"))
    Cal.add_child(TreeNode("Mountain View"))
    Cal.add_child(TreeNode("Palo Alto"))
    USA.add_child(NJ)
    USA.add_child(Cal)
    Global.add_child(India)
    Global.add_child(USA)
    return Global


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree(2)
