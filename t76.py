#-*- coding: UTF-8 -*-
__author__ = 'Childe'
#刷房子
#在一条街上，给H个房子刷墙，要求每个房子刷一种颜色，相邻房子不能刷同一种颜色。每种颜色成本不同，求最小刷墙成本

def min_cost(h,color):
    if h==0 or len(color)==0:
        return 0
    m=9999999999
    d=[[x for x in range(0,len(color))] for y in range(0,h)]
    i=0
    while i<h:
        j=0
        while j<len(color):
            if i==0:
                d[i][j]=color[j]
            else:
                m=9999999999999999
                k=0
                while k<len(color):
                    if k==j:
                        k+=1
                        continue
                    m=min(m,d[i-1][k])
                    k+=1
                d[i][j]=m+color[j]
            j+=1
        i+=1
    m=9999999999999
    j=0
    while j<len(color):
        m=min(m,d[h-1][j])
        j+=1
    return m

print min_cost(9,[x for x in range(1,5)])
