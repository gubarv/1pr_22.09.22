n = int(input())
n1 = n // 100
n2 = n // 10 % 10
n3 = n % 10
print((n3 + n2 * 10) * 10 + n1)

