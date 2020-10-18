def larenga(n, k):

    if n < 0 or k < 0:
        return 0

    if n == 0 and k == 0:
        return 1

    else:
        return larenga(n - 1, k) + larenga(n - 1,  k - 1)
