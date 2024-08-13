from string import ascii_letters


class Person:
    S_RUS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя-"
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, ps, age, weight):
        self.verify_fio(fio)
        self.verify_ps(ps)
        self.verify_age(age)
        self.verify_weight(weight)
        self.__fio = fio
        self.__ps = ps
        self.__age = age
        self.__weight = weight

    @classmethod
    def verify_fio(cls, x):
        if type(x) != str or len(x.split()) != 3:
            raise TypeError("INCORRECT INPUT(FIO)")
        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for i in x.split():
            if len(i) < 1:
                raise TypeError("INCORRECT INPUT")
            elif len(i.strip(letters)) != 0:
                raise TypeError("Use only letters and dash!")
            elif i[0] != i[0].upper():
                raise TypeError("FIO must start with a capital letter")

    @classmethod
    def verify_ps(cls, y):
        if type(y) != str or len(y.split()) != 2:
            raise TypeError("INCORRECT INPUT(PASSPORT)")
        elif len(y.split()[0]) != 6 or len(y.split()[1]) != 4:
            raise TypeError("INCORRECT INPUT(PASSPORT)")
        elif not y.split()[0].isdigit() or not y.split()[1].isdigit():
            raise TypeError("INCORRECT INPUT(PASSPORT)")

    @classmethod
    def verify_age(cls, z):
        if type(z) != int or z < 14 or z > 120:
            raise TypeError("Age must be integer and greater than 13 and lower than 121")

    @classmethod
    def verify_weight(cls, i):
        if type(i) != float or 150 < i < 25:
            raise TypeError("Weight must be a float number and be greater than 24")

    @property
    def FIO(self):
        return self.__fio

    @FIO.setter
    def FIO(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def Password(self):
        return self.__fio

    @Password.setter
    def Password(self, ps):
        self.verify_ps(ps)
        self.__ps = ps

    @property
    def Age(self):
        return self.__age

    @Age.setter
    def Age(self, age):
        self.verify_age(age)
        self.__age = age

    @property
    def Weight(self):
        return self.__age

    @Weight.setter
    def Weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight


p = Person("Фокин Александр Андреевич", "456123 7329", 18, 75.0)
p.FIO = "Mike Vasovskiy Yeap"
p.Weight = 45.4
p.Age = 1204
p.Password = "987654 1234"

print(p.__dict__)
