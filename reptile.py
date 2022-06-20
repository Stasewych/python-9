from Animal import Animal


class Reptile(Animal):
    def __init__(self, name, sex, legs_count, weight, eggs_count_per_year):
        super(Reptile, self).__init__(name, sex, legs_count, weight)
        self.eggs_count_per_year = eggs_count_per_year

    def __str__(self):
        return super(Reptile, self).__str__() \
               + f"Eggs count per year : {self.eggs_count_per_year} "