import sys


def mex(k):
    new_k = set(k)
    m = max(new_k)
    for i in range(m+2):
        if i not in new_k:
            return i
        
    
def func(i, l, r):
    global data

    new = data[l-1:r]
    mex_result = mex(new)

    data[i-1] = mex_result
    return 0

    
if __name__ == "__main__":
    n = int(input())

    data = list(map(int,list(input())))

    table = [1 if i + 1 == data[i] else 0 for i in range(n)]

        


# 31425
# 31025
# 32025
# 12025
# 12325
# 12305
# 12345

# 7253641
# 7250641
# 1250641
# 1230641
# 1230541
# 1230546
# 1234546
# 1234566
# 1234567