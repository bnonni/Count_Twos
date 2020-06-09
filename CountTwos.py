#!/usr/bin/env python3
import matplotlib.pyplot as plt
from sys import argv

def num(n):
    s = 0
    while(n > 0):
        if n % 10 == 2:
            s += 1
        n /= 10
        n = int(n)
    return int(s)

def count_twos(s, x, n):
    print('Start!')
    l = []
    while True:
        s += num(x)
        l.append((x, s-x))
        x += 1
        if x == n:
            break
        if x % 100000 == 0:
            print(f'iteration: {x}')
    return l

data = count_twos(int(argv[1]), int(argv[2]), int(argv[3]))

print('Done counting! Splitting x & y!')
x = []
y = []

for i,p in enumerate(data):
    x.append(data[i][0])
    y.append(data[i][1])
    if i % 100000 == 0:
        print(f'iteration: {i}')

print('Plotting data! Please standby!')
plt.plot(x, y)
plt.savefig('countwos.png')
