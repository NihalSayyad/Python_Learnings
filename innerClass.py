
class Student:

    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollNo)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)



s1  = Student('Nihal', 101)
s2  = Student('Saurabh', 100)

print(s1.name, s1.rollNo)
print(s2.name, s2.rollNo)

s1.show()
s2.show()
