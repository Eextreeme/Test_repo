'going to histiry main  '
class Musician:
    def __init__(self, name_of_group, honorar, age):
        """
        Constructor of groups
        """
        self.__name_of_group = name_of_group
        self.__honorar = honorar
        self.__age = age

    def __del__(self):
        print(f"Group {self.__name_of_group} has been removed")
        print('breanch')

    def get_name_of_group(self):
        return self.__name_of_group

    def get_honorar(self):
        return self.__honorar

    def get_age(self):
        return self.__age

    def set_name(self, name_of_group):
        self.__name_of_group = name_of_group

    def set_honorar(self, honorar):
        self.__honorar = honorar

    def set_age(self, age):
        self.__age = age

    def __str__(self):
        return f"Група: {self.get_name_of_group()}\nГонорар: {self.get_honorar()}\nВік групи: {self.get_age()}"
    
    def __repr__(self):
        return f"({self.get_name_of_group()}, {self.get_honorar()}, {self.get_age()})"


class MusicFestival:
    def __init__(self, max_budget, group_list):
        self.group_list = group_list
        self.max_budget = max_budget

    def __str__(self):
        for element in self.group_list:
            return str(element)

    def __del__(self):
        """
        Destructor
        """
        print('hello world')

        pass
        


if __name__ == "__main__":
    group_1 = Musician("AC/DC", 25000, 20)
    group_2 = Musician("BabyMetal", 30000, 5)
    group_3 = Musician("Rammstein", 50000, 24)

    festival = MusicFestival(100000)

    print(f"\n{str(group_1)}\n")
    print(f"{str(group_2)}\n")
    print(f"{str(group_3)}\n")
    print(festival.group_list)
    print('hello branch')
    print('crazy')