class ClassA:
    def __init__(self, val):
        self.data = val

    def __str__(self):
        return 'This is derived class'

    def __add__(self, other):
        return ClassA(self.data+other)

    def get_data(self):
        return self.data


if __name__ == '__main__':
    d = ClassA('abc')
    x = d + 'xyz'
    print(x.get_data())
