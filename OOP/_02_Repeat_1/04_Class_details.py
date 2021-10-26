class MixedNames:
    data = 'some text'

    def __init__(self, val):
        self.data = val

    def disp(self):
        print(f'Class attribute: {MixedNames.data}, Instances attribute {self.data}')

def test_MixedNames():
    mn = MixedNames(123)
    mn.disp()

if __name__ == '__main__':
    test_MixedNames()

