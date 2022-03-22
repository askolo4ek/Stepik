def multiply(a, now, n, st, col):
    cnt = 0
    for i in range(n):
        cnt += now[st][i] * a[i][col]
    return cnt


def make_a(a, n, power):
    now = a[:]
    for k in range(power - 1):
        res = [[multiply(a, now, n, j, i) for i in range(n)] for j in range(n)]
        now = res[:]
    return now


n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
power = int(input())
a_pow = make_a(a, n, power)
for i in range(n):
    print(*a_pow[i])