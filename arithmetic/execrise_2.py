import sys
sys.setrecursionlimit(30000)
table = {}

def ackermann(m, n):
    if not (m,n) in table:
        result = -1
        if m==0:
            result = n+1
        elif n==0:
            result = ackermann(m-1,1)
        else:
            result = ackermann(m-1, ackermann(m, n-1))
        table[(m, n)] = result
        return table[(m, n)]
    else:
        return table[(m, n)]

def akmDP(m, n):
    val = [-1 for i in range(m+1)]
    idx = [-1 for i in range(m+1)]
    idx[0] = 0
    val[0] = 1
    while idx[m] < n:
        val[0] += 1
        idx[0] += 1
        for i in range(1, m+1):
            if idx[i-1] == 1:
                val[i] = val[i-1]
                idx[i] = 0
            if val[i] != idx[i-1]:
                break
            idx[i] += 1
            val[i] = val[i-1]
    # print(val)
    # print(idx)
    return val[m]


if __name__ == '__main__':
	print("look up table(ack(3,1)): " + str(ackermann(1,3)))
	print("DP(ack(3,1)): " + str(akmDP(1,3)))
	print("look up table(ack(4,1)): " + str(ackermann(2,5)))
	print("DP(ack(4,1)): " + str(akmDP(2,5)))
