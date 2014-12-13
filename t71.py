#-*- coding: UTF-8 -*-
__author__ = 'Childe'
#数组最大和
#输入一个数组A，求其连续子数组的最大和
def max_sub_array(A):
    if len(A)==0:
        return 0
    curr_max=A[0]
    max_value=A[0]
    i=1
    while i<len(A):
        curr_max=max(A[i],curr_max+A[i])
        max_value=max(max_value,curr_max)
        i+=1
    return  max_value

print(max_sub_array([-3,1,-3,4,-1,2,1]))