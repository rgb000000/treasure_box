import numpy as np

def check(x, y, R):
    if x == [] or y ==[]:
        return False
    for i in x:
        if i in y:
            return False
    for i in x:
        for j in y:
            if R[i,j] != 1 or R[j,i]!=1:
                return False
    return True

def find(A, idx):
    x = []
    for j in range(len(A)):
        if idx & (1 << j):
            x.append(A[j])
    return x

result = []
length = []
def log_result(x, y):
    length.append(len(x) + len(y))
    result.append({
        'x': x.copy(),
        'y': y.copy()
    })

def backtrack(n, x, y, A, R):
    _y = y.copy()
    if n == len(A):
        return

    if check(x, _y, R):
        log_result(x, _y)
        backtrack(n+1, x, _y, A, R)

    _y.append(A[n])
    if check(x, _y ,R):
        log_result(x, _y)
        backtrack(n+1, x, _y, A, R)


if __name__ == '__main__':
    A = [i for i in range(5)]
    R = np.array(np.random.rand(len(A),len(A))>=0.2, dtype=np.int)
    for i in range(2**(len(A))):
        x = find(A, i)
        backtrack(0, x, [], A, R)
    print(result[np.array(length).argmax()])
    print(R)