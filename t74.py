#-*- coding: UTF-8 -*-
__author__ = 'Childe'
#爬楼梯
#假设有n个阶梯的楼梯，每次你只能爬上一个或两个台阶，计算出多少种不同的方法爬到顶部

def climb_stairs(n):
    if n==0 or n==1:
        return 1
    dp=[x for x in range(0,n+1)]
    dp[0]=1
    dp[1]=1
    i=2
    while i<n+1:
        dp[i]=dp[i-1]+dp[i-2]
        i+=1
    return dp[n]

print climb_stairs(9)

