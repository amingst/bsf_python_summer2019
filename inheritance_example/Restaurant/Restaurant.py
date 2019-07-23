class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.is_open = False

    def describe(self):
        print("Name: " + self.name + " | Cuisine: " + self.cuisine)

    def get_is_open(self):
        if self.is_open:
            print("Open for business")
        else:
            print("Closed")

    def open_close_restaurant(self):
        if self.is_open:
            self.is_open = False
        else:
            self.is_open = True
