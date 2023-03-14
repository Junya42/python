import time
#■▢▢▢▢▢▢▢▢▢ 10%
#■□□□□□□□□□ 10%
#▰▱▱▱▱▱▱▱▱▱ 10%


def ft_progress(lst):
    size = len(lst)
    i = 0
    eta = 0
    start = time.time()
    ret = 0
    loads = {
        0 : '▱▱▱▱▱▱▱▱▱▱',
        1 : '▰▱▱▱▱▱▱▱▱▱',
        2 : '▰▰▱▱▱▱▱▱▱▱',
        3 : '▰▰▰▱▱▱▱▱▱▱',
        4 : '▰▰▰▰▱▱▱▱▱▱',
        5 : '▰▰▰▰▰▱▱▱▱▱',
        6 : '▰▰▰▰▰▰▱▱▱▱',
        7 : '▰▰▰▰▰▰▰▱▱▱',
        8 : '▰▰▰▰▰▰▰▰▱▱',
        9 : '▰▰▰▰▰▰▰▰▰▱',
        10 : '▰▰▰▰▰▰▰▰▰▰',
    }
    for i in lst:
        ret = time.time() - start
        percent = round(i * 100 / size, 2)
        print(f"ETA: {eta}s [ {percent}%] {i}/{size} | {loads[round(percent / 10)]} | elapsed time {round(ret, 2)}")
        print('\033[1A', end='\x1b[2K')
        if i == 1:
            eta = round((time.time() - start) * (size - 1), 2)
        yield i
        i += 1
    print(f"ETA: {eta}s [ 100%] {size}/{size} | {loads[10]} | elapsed time {round(ret, 2)}")
        

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)