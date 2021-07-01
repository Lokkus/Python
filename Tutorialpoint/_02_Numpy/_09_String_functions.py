import numpy as np

def numpy_string_functions_test(str1, str2):
    print(f'Concatenate two strings: {np.char.add([str1], [str2])}')
    print(f'{np.char.multiply(str1, 3)}')
    print(f'{np.char.center("hello", 20, fillchar="*")}')
    print(f'Capitalize string: {np.char.capitalize(str1)}')
    print(f'How to change first letters in string to upper case? {np.char.title(np.char.add([str1], [str2]))}')
    s = np.char.add([str1], [str2])
    print(f'Convert to lower case: {np.char.lower(s)}')
    print(f'Convert to upper case: {np.char.upper(s)}')
    l = (np.char.split(s)[0])
    print(l)
    print(np.char.strip('ala ma kota', 'a')) # remove first and last character
    print(f'Join: {np.char.join(":", s)}')
    print(f'Join 2: {np.char.join(["-", "."], [s, s])}')
    print(f'Replace: {np.char.replace(s, "ma", "miala")}')


if __name__ == '__main__':
    numpy_string_functions_test('ala ', 'ma kota')