import math
AB=int(input())
BC=int(input())
H = math.sqrt(AB**2 + BC**2)
H = H/2.0
adj = BC/2.0
deg=u"\N{DEGREE SIGN}"

result = int(round(math.degrees(math.acos(adj/H))))

result = str(result)

print(result+deg)
