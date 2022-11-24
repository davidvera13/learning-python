# We define the input param as int and the return value as int
def fibonnacci(n: int) -> int:
    """Return `n` th Fibonacci number for positive `n` value"""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n-1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonnacci(i))
