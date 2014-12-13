#-*- coding: UTF-8 -*-
__author__ = 'Childe'
#二维数组最小路径和
#给出一个二维m*x矩阵grid，含有非负整数。找出一条路径从左上角到右下角，使之经过元素之和最小，假定只能向右或向下移动
def min_path_sum(grid):
    m=len(grid)
    n=len(grid[0])
    path=[[0 for x in y] for y in grid]
    path[0][0]=grid[0][0]
    i=1
    while i<m:
        path[i][0]=path[i-1][0]+grid[i][0]
        i+=1
    j=1
    while j<n:
        path[0][j]=path[0][j-1]+grid[0][j]
        j+=1
    i=1
    j=1
    while i<m:
        while j<n:
            path[i][j]=min(path[i][j-1]+grid[i][j],path[i-1][j]+grid[i][j])
            j+=1
        i+=1
        j=1
    return path[m-1][n-1]

L=[[1,2,3],
   [4,5,6],
   [7,8,9]]
print(min_path_sum(L))
