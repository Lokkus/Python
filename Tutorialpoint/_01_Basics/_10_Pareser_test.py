import argparse

def argparse_test():
    parser = argparse.ArgumentParser(description='Process some integers')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='An integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    x = argparse_test()

    print(x.accumulate(x.integers))
