class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    @staticmethod
    def parac():
        p1 = Person("a_ram2", "z_singh", 25)
        p2 = Person("ram", "a_singh1", 26)
        p3 = Person("m_ram1", "singh2", 20)

        f_list = [p1.firstname, p2.firstname, p3.firstname]
        print(sorted(f_list))
        l_list = [p1.lastname, p2.lastname, p3.lastname]
        print(sorted(l_list))
        age_list = [p1.age, p2.age, p3.age]
        print(sorted(age_list))


class Employee(object):

    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name

    @staticmethod
    def gather_requirement(project_name):
        if project_name == 'ABC Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1']
        return requirement

    # instance method
    def work(self):
        # call static method from instance method
        requirement = self.gather_requirement(self.project_name)
        for task in requirement:
            print('Completed', task)




class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.speed = 0

    def drive(self, speed):
        self.speed = speed
        print(f"The car is driving at {self.speed} mph")

    def stop(self):
        self.speed = 0
        print("The car has stopped")

    def info(self):
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Speed: {self.speed} mph")


if __name__ == '__main__':
    # Person.parac()

    # emp = Employee('Kelly', 12000, 'ABC Project')
    # emp.work()

    car = Car('MKL6541MJKK', 2012)
    car.drive(60)
    car.stop()
    car.info()