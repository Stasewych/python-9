from Animal import Animal


class Insect(Animal):
    def __init__(self, name, sex, legs_count, weight, eye_count):
        super(Insect, self).__init__(name, sex, legs_count, weight)
        self.eye_count = eye_count

    def __str__(self):
        return super(Insect, self).__str__() \
               + f"Eye count : {self.eye_count} "