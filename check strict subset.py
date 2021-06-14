A = set(input().split())
n = int(input())
result = True

for i in range(n):
    B = set(input().split())
    if not B.issubset(A):
        result = False
    if len(B) >= len(A):
        result = False
        

print(result)
