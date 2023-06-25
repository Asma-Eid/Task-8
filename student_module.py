class Student:
    def __init__(self, name, age, city):
        self.f_name = name
        self.f_age = age
        self.f_city = city

        print(f'Hello  {self.f_name},'
              f'your age is {self.f_age}'
              f'and your are from {self.f_city}.')

    def add_mark(self, *mark):
        summ = sum(mark)
        print(f'your marks sum:{summ}')

    def get_all_marks(self, *mymark):
        print(f'your marks:{mymark}')

    def calc_avg(self, *marks):
        sum = 0
        for mark in marks:
            sum += mark
        my_average = sum // len(marks)
        print(f'your average: {my_average}')

student1 = Student("Asma", 28, "Rafah")
student1.add_mark(20,17,16)
student1.get_all_marks(20,17,16)
student1.calc_avg(20,17,16)
