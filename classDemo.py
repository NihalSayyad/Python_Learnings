class Computer:
    def __init__(self):
        self.name="Nihal"
        self.age=26

    def compare(self,otehr):
        if self.name == otehr.name:
            if self.age == otehr.age:
                print("They are same")
            else:
                print("They are different")
        else:
            print("They are different")



c1 = Computer()
print(id(c1))

c2 = Computer()
print(id(c2))

c1.compare(c2)
