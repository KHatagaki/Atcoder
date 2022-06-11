n,m = map(int,input().split())

a = list(map(int,input().split()))
c = list(map(int,input().split()))
new_a = a[::-1]
new_c = c[::-1]
b = []

n_a = int("".join(map(str, new_a)))
n_c = int("".join(map(str, new_c)))

syou = n_c // n_a
amari = n_c % n_a



    