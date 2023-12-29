def check_input(n):
    if not isinstance(n, int):
        raise TypeError('n must be a positive int')
    if n < 0:
        raise ValueError('n must be a positive int')
