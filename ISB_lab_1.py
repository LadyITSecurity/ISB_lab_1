
import random
import math


def input_with_random(array, count):
    tmp = 0
    for i in range(0, count, 1):
        tmp *= 10
        tmp += random.randint(0, 1)
    return tmp


def test1(array, count):
    s = 0
    for i in array:
        if i == '1':
            s += 1
        else:
            s += -1
    s /= math.sqrt(count)
    print("S = ", s)
    return math.erfc(s / math.sqrt(2))


def test2(array, count):
    z = 0
    for i in range(len(array)):
        if int(array[i]) == 1:
            z += 1
    z /= count
    print("Z = ", z)
    if math.fabs(z - 0.5) >= (2.0 / math.sqrt(count)):
        return 0.0
    else:
        v = 0
        for j in range(len(array) - 1):
            if array[j] != arr[j + 1]:
                v += 1
        print("V = ", v)
        p = math.fabs(v - 2.0 * len(array) * z * (1.0 - z))
        p /= 2 * math.sqrt(2.0 * len(array)) * z * (1.0 - z)
        return math.erfc(p)


def test3(array, count):
    v = [0, 0, 0, 0]
    for i in range(0, len(array), 8):
        max_bit = 0
        max_tmp = 0
        tmp = array[i:i + 8:]
        for j in range(i, i+8, 1):
            if array[j] == '1':
                max_tmp += 1
            else:
                max_tmp = 0
            if max_tmp > max_bit:
                max_bit = max_tmp
        print(tmp, " -> max 1 = ", max_bit)
        tmp = ''
        if max_bit <= 1:
            v[0] += 1
        else:
            if max_bit == 2:
                v[1] += 1
            else:
                if max_bit == 3:
                    v[2] += 1
                else:
                    v[3] += 1
    print('\n\nV1 = ', v[0], '\nV2 = ', v[1], '\nV3 =  ', v[2], '\nV4 = ', v[3],)
    pi = [0.2148, 0.3672, 0.2305, 0.1875]
    x = 0
    for i in range(4):
        x += ((v[i] - 16 * pi[i]) * (v[i] - 16 * pi[i])) / 16 * pi[i]
        print(x)
    return x



#результат на java
#arr = '00101101111001110110001100101110001101111111100010110101100100100010100110011000101101000011101110111001000011110001111000001111'
#результат на C++
#arr = '11111111100001101111101110010101111111000001000101001011001111001001000111111001111001100001011111001010011010110010001110101011'
n = 128
#результат на python
arr = ''
arr = str(input_with_random(arr, n))
print(arr)
print('TEST 1\nP value = ', test1(arr, n))
print('_______________________')
print("TEST 2\nP value = ", test2(arr, n))
print('_______________________')
print("TEST 3\nX^2 = ", test3(arr, n))
print('_______________________')
