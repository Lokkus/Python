import sys
import time
reps = 100000
repslist = range(reps)

def timer(func, *args, **kwargs):
    start = time.process_time()
    for i in repslist:
        ret = func(*args, **kwargs)
    elapsed = time.clock() - start
    return (elapsed, ret)


def forloops():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res

def listComp():
    return [abs(x) for x in repslist]

def mapCall():
    return list(map(abs, repslist))

def genExpr():
    return list(abs(x) for x in repslist)

def genFun():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())


if __name__ == '__main__':
    print(sys.version)
    for test in (forloops, listComp, mapCall, genExpr, genFun):
        elapsed, result = timer(test)
        print('-' * 33)
        print('%-9s: %.5f => [%s..%s]' % (test.__name__, elapsed, result[0], result[-1]))