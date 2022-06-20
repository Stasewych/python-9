from Animal import Animal


class Bird(Animal):
    def __init__(self, name, sex, legs_count, weight, wing_size):
        super(Bird, self).__init__(name, sex, legs_count, weight)
        self.wing_size = wing_size

    def __str__(self):
        return super(Bird, self).__str__() \
               + f"Wing size : {self.wing_size} "