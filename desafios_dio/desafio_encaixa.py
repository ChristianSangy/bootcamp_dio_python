N = int (input())

while N > 0:
    caixa_a, caixa_b = input().split()

    if caixa_a.endswith (caixa_b):
     print("encaixa")

    else:
     print("nao encaixa")

    N -= 1
