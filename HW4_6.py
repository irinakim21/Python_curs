from itertools import cycle, count

v_start = int(input('Start number: '))
v_stop = v_start * 2 + 10 + 1

# a
for i in count(v_start):
    if i >= v_stop:
        break
    else:
        print(i)
del i

# b
my_list = [i for i in range(v_stop)]
count = 0
for b in cycle(my_list):
    if count < v_stop + 10:
        print(b)
        count += 1
    else:
        break
