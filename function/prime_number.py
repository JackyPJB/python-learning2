#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/23 22:37
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import time

__author__ = 'Max_Pengjb'
start = time.time()
# 下面写上代码块
"""
求不超过某个正整数x内的所有素数，有一个著名的算法——埃拉托斯特尼筛法。其算法描述为：
    先用一个数组vis，把不大于该正整数x的所有正整数标记为0，表示没有访问。
    然后从第一个素数2开始遍历整个区间，如果当前访问的数没有访问过，则可以认为它是一个素数，
那么就将它在该区间内所有的倍数全部标记为已访问，这样就保证外部的循环发现的没有访问过的数都是素数。
其具体实现如下述代码所示：
"""


def prime_numbers_below1(x):
    ss = [0 for _ in range(x + 1)]
    prime = []
    for i in range(2, x + 1):
        if ss[i] == 0:
            prime.append(i)
        for j in range(i * 2, x + 1, i):
            ss[j] = 1
    return prime


# 欧拉筛法，这里只给出其代码实现，希望大家能仔细去体会。
def prime_numbers_below2(x):
    vis = [0 for _ in range(x + 1)]
    prime_table = []
    ln = 0
    for num in range(2, x + 1):
        if vis[num] == 0:
            prime_table.append(num)
            ln += 1
        for j in range(ln):
            if num * prime_table[j] > x:
                break
            vis[num * prime_table[j]] = 1
            if num % prime_table[j] == 0:
                break
    return prime_table


# print(prime_numbers_below1(9999999))
res = prime_numbers_below1(9999999)
print(res)
print(len(res))

# 上面中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))

'''
:type x: int
:rtype : Boolean
'''


def solve(x):
    # 请在此添加代码，实现判断一个数是否是素数
    # ********** Begin *********#

    ll = [0 for _ in range(x + 1)]
    print(ll)

    for i in range(2, x + 1):
        if ll[i] == 0:
            for j in range(i * 2, x + 1, i):
                ll[j] = 1
    print(ll)
    if ll[x] == 1:
        print(ll[x])
        return False
    else:
        print(ll[x])
        return True


solve(6)


def solve2(x):
    '''
    :type x: int
    :rtype : None
    '''
    # 请在此添加代码，实现打印前x行乘法表的内容
    # ********** Begin *********#
    for i in range(1, x + 1):
        for j in range(i, 9):
            print("{}*{}={:>3} ".format(i, j, i * j), end='')
        print("{}*{}={:>3}".format(i, 9, i * 9))


solve2(9)


def solve3(op, num_1, num_2):
    if op == '+':
        re = num_1 + num_2
    elif op == '-':
        re = num_1 - num_2
    elif op == '*':
        re = num_1 * num_2
    else:
        re = num_1 / num_2
    return "{:.2f}".format(re)


print(solve3('+', 1, 1))
