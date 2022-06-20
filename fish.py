from Animal import Animal


class Fish(Animal):
    def __init__(self, name, sex, legs_count, weight, max_depth):
        super(Fish, self).__init__(name, sex, legs_count, weight)
        self.legs_count = 0
        self.max_depth = max_depth

    def __str__(self):
        return super(Fish, self).__str__() \
               + f"Max depth : {self.max_depth} "