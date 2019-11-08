from math import *
import numpy as np

def angle_between(dot1, dot2):
    try:
        cos = (dot2[0][0] - dot1[0][0]) / (sqrt( (dot2[0][0] - dot1[0][0])**2 + (dot2[0][1] - dot1[0][1])**2 ))
        if cos==0:
            if dot2[0][1] < dot1[0][1]:
                return -90
            else:
                return 90
        if dot2[0][1] < dot1[0][1]:
            return acos(cos)*180/pi * (-1)
        return acos(cos)*180/pi
    except:
        return 999

def angle_3_dot(a,b,c):
    if b == c:
        return -1
    a = np.array([a[0][0], a[0][1]])
    b = np.array([b[0][0], b[0][1]])
    c = np.array([c[0][0], c[0][1]])
    alen = np.sqrt(np.sum(np.square(b-c)))
    clen = np.sqrt(np.sum(np.square(a-b)))
    blen = np.sqrt(np.sum(np.square(a-c)))
    cosb = (alen**2 + clen**2 - blen**2)/(2*alen*clen)
    return acos(cosb)*180/pi

def convex(dots):
    result = []
    idx = []
    dot_with_min_x_idx = 0
    min_x = 1000
    test = 10
    for i,dot in enumerate(dots):
        if dot[0][0] < min_x:
            if dot in result:
                continue
            min_x = dot[0][0]
            dot_with_min_x_idx = i
    dot_with_min_x = dots[dot_with_min_x_idx]
    result.append(dot_with_min_x)
    idx.append(dot_with_min_x_idx)
    cnt = 1
    while(1):
        angles = []
        if cnt == 1:
            for i,dot in enumerate(dots):
                angles.append(angle_between(dot_with_min_x, dot))
            angles = np.array(angles)
            next_dot = angles.argmin()
        else:
            for i,dot in enumerate(dots):
                print(dots[idx[cnt-2]][1] + "--" + dots[idx[cnt-1]][1] + "--" + dot[1])
                angles.append(angle_3_dot(dots[idx[cnt-2]], dots[idx[cnt-1]], dot))
            print(angles)
            angles = np.array(angles)
            next_dot = angles.argmax()

        if next_dot == idx[0]:
            idx.append(next_dot)
            break
        idx.append(next_dot)
        dot_with_min_x = dots[next_dot]
        cnt += 1
        test -= 1
        if test == 0:
            break
    print(idx)
    return np.array(dots)[idx]

if __name__ == '__main__':
    dots = [((1,1), 'A'), ((2,2), 'B'), ((3,1), 'C'), ((2,1), 'D'), ((1,-5), 'E'), ((-1,-1), 'F'), ((-10,10), 'H')]
    result = convex(dots)
    print("result:\n", result)