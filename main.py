class Insect:
    __counter = 0
    __name = None
    __speed = None
    __weight = None
    __type_of_insect = None
    __age = None

    @classmethod
    def get_count(cls):
        print(f"\nКількість об'єктів {cls.__counter}\n")

    def __init__(self, name="", speed=None, weight=None, type_of_insect="", color="", age=None):
        self.__name = name
        self.__speed = speed
        self.__weight = weight
        self.__type = type_of_insect
        self.__color = color
        self.__age = age
        Insect.__counter += 1

    def __str__(self):
        return f"name: {self.__name} \nspeed(m/s): {self.__speed} \nweight: {self.__weight} \
               \ntype: {self.__type} \ncolor: {self.__color} \nage in years: {self.__age} \n"

    def __del__(self):
        print("спрацюав деструктор")
        del self


def main():
    obj1 = Insect("цвіркун", 12, 25, "прямокрила", "зелений", 10)
    print(obj1)

    obj2 = Insect("клоп", 6, 60, "напівтвердокрила", "коричневий", 4)
    print(obj2)

    obj3 = Insect("хрущ", 20, 30, "твердокрила", "коричневий", 1)
    print(obj3)

    obj4 = Insect("метелик", 9, 10, "лускокрила", "фіолетовий", 0.5)
    print(obj4)

    obj5 = Insect("бджола", 30, 20, "перетинчастокрилі", "чорно-жовта", 0.09)
    print(obj5)

    Insect.get_count()


if __name__ == "__main__":
    main()
