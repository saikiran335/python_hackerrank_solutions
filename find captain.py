import math
from collections import Counter

n = input()
b = input().split()

k = Counter(b)

d = dict(k)

print (min(d, key=lambda k: d[k]))
