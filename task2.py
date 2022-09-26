n = int(input())
n3 = n%10
n1 = n // 100
if n3 == n1:
    print('палиндромом')
else:
    print('не палиндромом')