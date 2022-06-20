from Bird import Bird
from Fish import Fish
from Insect import Insect
from Mammal import Mammal
from Reptile import Reptile


def main():
    mammal1 = Mammal("Wolf", "male", 4, 70., False)
    fish1 = Fish("Shark", "female", 0, 40., 20.)
    bird1 = Bird("Eagle", "male", 2, 10., 2.)
    insect1 = Insect("Fly", "male", 6, 0.01, 2)
    reptile1 = Reptile("Snake", "female", 0, 3, 10)
    print(mammal1.__str__())
    print(fish1.__str__())
    print(bird1.__str__())
    print(insect1.__str__())
    print(reptile1.__str__())


if __name__ == '__main__':
    main()