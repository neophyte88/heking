def fib():
    n = 10  # int(input("N: "))
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    print(seq)


fib()
