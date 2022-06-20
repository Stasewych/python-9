class Animal(object):
    def __init__(self, name: str, sex: str, legs_count: int, weight: float) -> None:
        self.name = name
        self.sex = sex
        self.legs_count = legs_count
        self.weight = weight

    def __str__(self):
        return f"Name : {self.name}, Sex : {self.sex}, Legs count : {self.legs_count}, Weight : {self.weight}, "