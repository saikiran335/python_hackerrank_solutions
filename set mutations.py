n = int(input())

A = set(map(int, input().split()))

N = int(input())

for i in range(N):
    op = input().split()
    if op[0] == 'intersection_update':
        temp = set(map(int, input().split()))
        A.intersection_update(temp)
    elif op[0] == 'update':
        temp = set(map(int, input().split()))
        A.update(temp)
    elif op[0] == 'symmetric_difference_update':
        temp = set(map(int, input().split()))
        A.symmetric_difference_update(temp)
    elif op[0] == 'difference_update':
        temp = set(map(int, input().split()))
        A.difference_update(temp)
    else :
        assert False

print(sum(A))
