
dic={ 1:['1',3], 2:['2',6], 3:['4',2], 4:['5',5], 5:['7',1], 6:['8',4]} 

#dic to find the remainder and quotient of a number when divided by 7

def nthpi(n):
    if(n==1) :
        return '3.1'
    if n==2 :
        return '3.14'
    prev=2
    r=0
    s='3.14'
    while(n-2!=0):
        s=s+dic[prev][0]
        prev=dic[prev][1]
        n-=1
    r=dic[prev][1]
    if r>4:
        s=s[:-1]+str(int(s[-1])+1)
    return s
