from Animal import Animal


class Mammal(Animal):
    def __init__(self, name, sex, legs_count, weight, is_pregnant):
        super(Mammal, self).__init__(name, sex, legs_count, weight)
        self.is_pregnant = is_pregnant

    def __str__(self):
        return super(Mammal, self).__str__() \
               + f"Is pregnant : {self.is_pregnant} "