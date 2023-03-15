"""
# "Given a list of people objects, create a function that sorts the list by an attribute name. The attribute to sort by
# will be given as a string.
# The Person class will only include these attributes in the following order:
# firstname
# lastname
# age
# Examples
# p1 = Person(""Michael"", ""Smith"", 40)
# p2 = Person(""Alice"", ""Waters"", 21)
# p3 = Person(""Zoey"", ""Jones"", 29)
# people_sort([p1, p2, p3], ""firstname"") ➞ [p2, p1, p3]
# # Alice, Michael, Zoey
# people_sort([p1, p2, p3], "lastname") ➞ [p3, p1, p2]
# # Jones, Smith, Waters
# people_sort([p1, p2, p3], "age") ➞ [p2, p3, p1]
# # 21, 29, 40
"""


class Person():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    @staticmethod
    def sort_attributes():
        p1 = Person("Michael", "Smith", 40)
        p2 = Person("Alice", "Waters", 21)
        p3 = Person('Zoey', 'Jones', 29)

        f_name = [p1.firstname, p2.firstname, p3.firstname]
        sort_f_name = sorted(f_name)
        print(sort_f_name)

        l_name = []

        sort_l_name = sorted(l_name)
        print(sort_l_name)

        age_list = []
        age_list.append(p1.age)
        age_list.append(p2.age)
        age_list.append(p3.age)
        for i in range(len(age_list)-1, 0, -1):
            for i in range(i):
                if age_list[i] > age_list[i+1]:
                    temp = age_list[i]
                    age_list[i] = age_list[i+1]
                    age_list[i + 1] = temp

        print(age_list)


if __name__ == '__main__':

    Person.sort_attributes()





