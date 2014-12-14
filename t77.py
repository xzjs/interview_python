#-*- coding: UTF-8 -*-
__author__ = 'Childe'
#数字解码
#给只含有A到Z字符的字符串加密，加密规则为：‘A’->1，‘B’->2,...‘z’->26，现有一个已经加过密的密文（仅含有数字），求其解密的方法个数

def num_decding(s):
    if len(s)==0:
        return 0
    length=len(s)
    dp=[0 for x in range(0,length+1)]
    dp[length]=1
    i=length-1
    while i>=0:
        if s[i]=='0':
            dp[i]=0
        else:
            dp[i]=dp[i+1]
        if i+1<len(s) and (s[i]=='1'or (s[i]=='2' and s[i+1]<='6')):
            dp[i]+=dp[i+2]
        i-=1
    return  dp[0]

print num_decding('123456789')
