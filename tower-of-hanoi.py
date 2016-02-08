def towers(n, a, b, c):
    while n > 0:
        towers(n - 1, a, c, b)
        print 'a -> b'
        towers(n - 1, c, b, a)