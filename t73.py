#-*- coding: UTF-8 -*-
__author__ = 'Childe'
#三角形最小路径
#输入一个三角形，找出一条从顶部到底部的最小路径和，你只能往下移动到相邻的节点

def minimun_total(triangele):
    path=[]
    i=len(triangele)-1
    while i>=0:
        j=0
        while j<=i:
            if i==len(triangele)-1:
                path.append(triangele[i][j])
            else:
                path[j]=triangele[i][j]+min(path[j],path[j+1])
            j+=1
        i-=1
    return path[0]

L=[[2],
   [3,4],
   [6,5,7],
   [8,3,9,2]]
print minimun_total(L)
