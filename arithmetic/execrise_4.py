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

def findY(A, idx, x, R):
    y = []
    for j in range(len(A)):
        if idx & (1 << j):
            y.append(A[j])
            if check(x, y, R) == False:
                return False
    return y

def backtrack(A, R):
    x = []
    y = []
    result = []
    length = []
    for i in range(2**(len(A))):
        x = find(A, i)
        for k in range(2**(len(A))):
            y = findY(A,k, x, R)
            if y:
                result.append({'x':x, 'y':y})
                length.append(len(x) + len(y))
                print('x --- ' + str(x))
                print('y --- ' + str(y))
                print()
            y = []
        x = []
    print(result[np.array(length).argmax()])
    print(R)

if __name__ == '__main__':
    A = [i for i in range(10)]
    R = np.array(np.random.rand(len(A),len(A))>=0.5, dtype=np.int)
    backtrack(A, R)