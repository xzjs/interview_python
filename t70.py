#-*- coding: UTF-8 -*-
__author__ = 'Childe'
#给出一个数组，第i个元素代表第i天的股票，求最大交易利润。允许最多交易两次
def maxProFitII(prices):
    length=len(prices)
    if length==0:
        return 0
    currProfit=[0 for x in prices]
    futureProfit=[0 for x in prices]
    low=prices[0]
    maxProfit=0
    i=1
    while i<length:
        low=min(low,prices[i])
        currProfit[i]=max(currProfit[i-1],prices[i]-low)
        i+=1
    high=prices[length-1]
    i=length-1
    while i>=0:
        high=max(high,prices[i])
        if i<length-1:
            futureProfit[i]=max(futureProfit[i+1],high-prices[i])
        maxProfit=max(maxProfit,currProfit[i]+futureProfit[i])
        i-=1
    return maxProfit

L=[1,2,3,4,5]
print maxProFitII(L)
