import  time
import calendar

def czas():
    ticks = time.time()
    print(f'Number of tickst since 12:00am, January 1, 1970: {ticks}')

    localtime = time.localtime(time.time())
    for t in localtime:
        print(t)
    x1 = ['Year', 'Month', 'Day', 'Hour', 'Minute', 'Second']
    x2 = list(localtime)
    x3 = dict(zip(x1, x2))
    print(x3)

def sformatowany_czas():
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)

def wyswietl_miesiac():
    cal = calendar.month(2021, 6)
    print(cal)

def delay():
    for i in range(10):
        time.sleep(1)
        print(i)



if __name__ == '__main__':
    #czas()
    #sformatowany_czas()
    #wyswietl_miesiac()
    delay()