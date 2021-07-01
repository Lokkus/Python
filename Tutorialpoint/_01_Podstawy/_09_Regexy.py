import re

def simple_example():
    line  = 'Cats are smarter than dogs'

    matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

    if matchObj:
        print(f'matchObj.group(): {matchObj.group()}')
        print(f'matchObj.group(1): {matchObj.group(1)}')
        print(f'matchObj.group(2): {matchObj.group(2)}')
    else:
        print('No match')

def search_exmaple():

    line = 'Ala ma 12323452345 wlosy, 444234523452345 zeby i 562345234523457 palcow'
    searchObj = re.search(r'([0-9]+)\s[a-z]+,\s([0-9]+)\s[a-z]+\s.\s([0-9]+) ', line)
    if searchObj:
        for i in range(4):
            print(f'searchObj.group({i}): {searchObj.group(i)}')


def replace_example():
    # 1. Otworz plik
    # 2. Zmodyfikuj plik tak, aby zostaly tylko numery sciezek i nazwy plikow (uzyj regex)
    # 3. Kazdy wyraz powinien zaczynac sie z wielkiej litery w nazwie pliku
    # 4. Zapisz zmiany do innego pliku

    # otworz plik
    with open('folder/moj_plik3.txt', 'r') as read_file:
        with open('folder/moj_plik4.txt', 'w') as write_file:
            for rf in read_file.readlines():
                temp_str = re.search(r'([a-zA-Z]+\s.\s[0-9]+\s.\s([a-zA-Z]+\s)+.\s)(\d+\s.\s([a-zA-Z]+(\s|.mp3|\([a-zA-Z]|\)+)+)+)', rf)
                str2 = re.search(r'\s\d{2}\s.\s([a-zA-Z]+(\s|.mp3|\([a-zA-Z]+\))+)+', rf)
                print(str2.group().rstrip())
                song = temp_str.group(3).title()
                song = re.sub(r'Mp3', 'mp3', song)
                write_file.write(song)

def sub_example():
    # 1. wygenreuj sciezki w licie
    # 2. Uzywajac group, znajdz te grupy ktore bedzie mozna wykorzystac do podmiany danych w sciezkach
    # 3. Zmodyfikuj sciezki

    path_list = []
    x = []
    change_from = ['/net/8k3/e0fs01/irods', '1-Raw']
    change_to = ['/HPCC', '2-Sim']


    path_list.append('/net/8k3/e0fs01/irods/PLKRA-PROJECTS/ADCAM/1-Raw/CONTI/2020/12/19/'
                     '20201219T194041_000000_LJ21405/20201219T194041_000000_LJ21405_BN_FASETH/1FASETH.MF4')
    path_list.append('/net/8k3/e0fs01/irods/PLKRA-PROJECTS/ADCAM/1-Raw/CONTI/2020/12/19/'
                     '20201219T194041_000000_LJ21405/20201219T194041_000000_LJ21405_BN_FASETH/2FASETH.MF4')
    path_list.append('/net/8k3/e0fs01/irods/PLKRA-PROJECTS/ADCAM/1-Raw/CONTI/2020/12/19/'
                     '20201219T194041_000000_LJ21405/20201219T194041_000000_LJ21405_BN_FASETH/3FASETH.MF4')

    # zamien /net/8k3/e0fs01/irods na /HPCC
    for i in range(len(path_list)):
        for j in range(len(change_from)):
            path_list[i] = re.sub(change_from[j], change_to[j], path_list[i])

    for path in path_list:
        print(path)





if __name__ == '__main__':
    #simple_example()
    #search_exmaple()
    #replace_example()
    sub_example()