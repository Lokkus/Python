def interaktywne_petle():
    while True:
        reply = input("Wpisz tekst...")
        if reply == 'stop':
            break
        elif not reply.isdigit():
            print("Jeszcze raz")
        else:
            print(int(reply) ** 2)


def obsluga_bledow_try_pierwsze_starcie():
    while True:
        reply = input("Wpisz tekst\n")
        if reply == 'stop': break
        try:
            num = int(reply)
        except:
            print('niepoprawnie')
        else:
            print(int(reply) ** 2)
    print('koniec')

if __name__ == '__main__':
    interaktywne_petle()
    obsluga_bledow_try_pierwsze_starcie()