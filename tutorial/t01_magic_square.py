"""Magic Square
"""

import itertools

N = 3
cnt = 0

for m in itertools.permutations([i + 1 for i in range(N*N)], N*N):
    # initial
    total = sum([m[i] for i in range(0, N*N, N)])

    # horizontal
    horizontal = True
    for offset in range(N):
        if total != sum([m[offset*N + i] for i in range(N)]):
            horizontal = False
            break
    if not horizontal:
        continue

    # vertical
    vertical = True
    for offset in range(N):
        if total != sum([m[offset + i] for i in range(0, N*N, N)]):
            vertical = False
            break
    if not vertical:
        continue

    # diagonal
    diagonal = True
    if total != sum([m[i*N + i] for i in range(N)]):
        diagonal = False
    if total != sum([m[(N-1-i)*N + i] for i in range(N)]):
        diagonal = False
    if not diagonal:
        continue

    # result
    for i in range(N):
        print(m[i*N:(i+1)*N])
    print()
    cnt += 1

# cnt
print('cnt= =', cnt)
