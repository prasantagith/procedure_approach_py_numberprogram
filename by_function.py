#Prime number
'''def prime(num):
    fc=0
    if num>1:
        for value in range(2,num//2+1):
            if num%value==0:
                return False
        return True

print(prime(int(input('enter num: '))))

#composite number
def composite(num,fc):
    for value in range(1,num+1):
        if num%value==0:
            fc+=1
    if fc>2:
        return True
    else:
        return False
    
print(composite(int(input('enter number:')),0))

#perfect
def perfect(num,d_sum=0):
    for value in range(1,num):
        if num%value==0:
            d_sum+=value
    if num==d_sum:
        return True
    else:
        return False
print(perfect(6))

def pronic(num,n):
    while(n*(n+1))<=num:
        if (n*(n+1))==num:
            return True
        else:
            n+=1
    else:
        return False
print(pronic(int(input('enter number:')),0))

#sunny
def sunny(num,n):
    while(n**2)<=num+1:
        if(n**2)==num+1:
            return True
        else:
            n+=1
    else:
        return False
print(sunny(int(input('enter number :')),0))

#niven number
def niven(num,d_sum):
    copy=num
    while(num>0):
        rem=num%10
        d_sum+=rem
        num//=10
    if num%d_sum==0:
        return True
    else:
        return False
print(niven(int(input('enter numbers:')),0))'''

#ne
            