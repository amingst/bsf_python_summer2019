import inheritance_example.Restaurant


class IceCreamShop(Restaurant):
    def __init__(self, name):
        self.flavors = []
        super(IceCreamShop, self).__init__(name, 'Ice Cream')

    def print_menu(self):
        print("Menu\n" + "----")
        for flavor in flavors:
            print(flavor)

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def remove_flavor(self, item):
        for flavor in flavors:
            if flavor.lower() == item:
                self.flavors.remove(flavor)
