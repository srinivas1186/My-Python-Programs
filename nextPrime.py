'''
Program to find the next prime number
'''

def isPrime(n):    #program to find if a number is prime or not
    s= n**0.5
    s= round(s)
    for i in range(3,s+1,2):
        if n%i==0:
            return False
    return True

def nextPrime(n):       #Function to find nextPrime number
    if n==0 or n==1 :
        return 2
    if(n%2==0):
        n=n+1
    else:
        n=n+2
    while isPrime(n)==False:
        n+=2
    return n
