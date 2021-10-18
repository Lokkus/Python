import os
import  time

def czytanie_raw_input():
    str = input('Enter your input: ')
    print('Received input is: ', str)

def otwieranie_pliku_do_czytania():
    fo = open('folder/moj_plik.txt', 'r')
    for f in fo.readlines():
        print(f, end='')
    fo.close()

def zapis_do_pliku():
    fo = open('folder/moj_plik.txt', 'a')
    fo.write('Metallica - 1996 - Load\n')
    fo.close()

    #sprawdzamy
    otwieranie_pliku_do_czytania()

def funkcja_read():
    fo = open('folder/moj_plik.txt', 'r')
    print(fo.read(12))
    fo.close()

def open_with():
    with open('folder/moj_plik.txt', 'r') as fo:
        for f in fo:
            print(f, end='')

def tell_and_seek():
    # open a file
    fo = open('folder/moj_plik.txt', 'r')
    str = fo.read(10)
    # check current position
    pos = fo.tell()
    print(f'Current position: {pos}')

    # reposition pointer at the beginning pos
    pos = fo.seek(13)
    str = fo.read(12)
    print(f'String: {str}')
    fo.close()

def os_module():
    # get pwd
    print(os.getcwd())

    # create dir
    try:
        os.mkdir('Test')
    except FileExistsError:
        print('folder exist')

    # remove created folder
    os.removedirs('Test')

if __name__ == '__main__':
    #czytanie_raw_input()
    #otwieranie_pliku_do_czytania()
    #zapis_do_pliku()
    #funkcja_read()
    open_with()
    #tell_and_seek()
    #os_module()
