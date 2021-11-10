#####################################################
class Wrapper:
    def __init__(self, object):
        self.wrapper = object

    def __getattr__(self, item):
        print(f'sledzenie: {item}')
        return getattr(self.wrapper, item)

def test_wrapper():
    x = Wrapper([1, 2, 3, 4])
    x.append(5)
    print(x.wrapper)

    x = Wrapper({1: 'ala', 2: 'ma kota'})
    print(x.keys())

#####################################################


if __name__ == '__main__':
    test_wrapper()