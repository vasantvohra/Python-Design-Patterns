"""Tree like structure."""


class Component(object):
    """Abstract class"""

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


class Child(Component):
    """Concrete class"""

    def __init__(self, *args, **kwargs):
        super(Child, self).__init__(*args, **kwargs)
        self.name = args[0]

    def component_function(self):
        print(f'{self.name}')


class Composite(Component):
    """Concrete class"""

    def __init__(self, *args, **kwargs):
        super(Composite, self).__init__(*args, **kwargs)
        self.name = args[0]
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        print(f'{self.name}')
        for i in self.children:
            i.component_function()


if __name__ == '__main__':
    sub1 = Composite("|-submenu1")
    sub11 = Child(" |-sub_submenu 11")
    sub12 = Child(" |-sub_submenu 12")
    sub1.append_child(sub11)
    sub1.append_child(sub12)
    top = Composite("top_menu")
    sub2 = Child("|-sub_menu2")
    top.append_child(sub1)
    top.append_child(sub2)
    top.component_function()