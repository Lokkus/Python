def zagniezdzenia():
    a = list( map((lambda x : x**2), filter((lambda x : x % 2 == 0), range(5))))
    print(a)
    # bardziej skomplikowany przyklad
    res = [(x , y) for x in range(10) if x % 2 == 0 for y in range(10) if y % 2 == 1]
    print(res)

    # znowu pierwsze
    p = [i for i in range(2, 10) if all(j % i for j in range(2, i))]
    print(p)
    
    
if __name__ == '__main__':
    zagniezdzenia()
    



