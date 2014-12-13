#-*- coding: UTF-8 -*-
__author__ = 'Childe'
#迷宫路径数
#给出一个m*n矩阵，求从左上角到右下角的总路径数，只能向右向下移动

def unique_paths(m,n):
    dp=[1 for x in range(0,n)]
    i=1
    while i<m:
        j=1
        while j<n:
            dp[j]=dp[j]+dp[j-1]
            j+=1
        i+=1
    return dp[n-1]

print unique_paths(3,4)