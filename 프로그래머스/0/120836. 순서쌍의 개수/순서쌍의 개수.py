def solution(n):
    a = 0
    pairs = []
    for a in range(1, n+1):
        if n % a == 0:
            b = n // a
            pairs.append((a, b))
    return len(pairs)