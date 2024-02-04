#PRIME NUMBER
num=int(input('enter number:'))
fact_count=0
for value in range(1,num+1):
    if num%value==0:
        fact_count+=1
if fact_count==2:
    print('prime')
else:
    print('not prime')
   
 #Composite   
num=int(input('enter num: '))
if num>1:
    for value in range(2,num//2+1):
        if num%value==0:
            print('Composite')
            break
    else:
        print('Notcompositr') 
        
#perfect 
num=int(input('Enter num :'))
d_sum=0
for value in range(1,num):
    if num%value==0:
        d_sum+=value
if num==d_sum:
    print('Perfect')
else:
    print('no Prefect')
    
    

#peonic
num=int(input('enter num:'))
n=0
while(n*(n+1))<=num:
    if (n*(n+1))==num:
        print('pronic')
        break
    else:
        n+=1
else:
    print('not pronic')
    
#sunny number
num=int(input('enter num:'))
n=1
while(n**2<=num+1):
    if (n**2==num+1):
        print('sunny')
        break
    else:
        n+=1
else:
    print('not sunny')
    
#niven number [if a number div with sum of digit ex num =21 (2+1==3,21%3==0)]
num=int(input('enter numbers:'))
d_sum=0
copy=num
while(num!=0):
    rem=num%10
    d_sum+=rem
    num//=10
if(copy%d_sum==0):
    print('Niven')
else:
    print('Not Niven')
    
#Spy [A spy number is a number in which the Sum of the digits is equal to the product of the digit]
num=int(input('enter number:'))
product=1
d_sum=0
while(num!=0):
    rem=num%10
    d_sum+=rem
    product*=rem
    num//=10
if d_sum==product:
    print('spy number')

else:
    print('not spy')    
    
#Neon number 
num=int(input('enter numbers:'))
sq=num**2
d_sum=0
while(sq!=0):
    rem=sq%10
    d_sum+=rem
    sq//=10
if d_sum==num:
    print('Neon')
else:
    print('not neon')
    
#Palidrome 
num=int(input('enter numbers:'))
rev=0
copy=num

while(num!=0):
    rem=num%10
    rev=rev*10+rem
    num//=10
if rev==copy:
    print('palidrome')
else:
    print('not palidrome')
    
#Armstrong 
num=int(input('enter number:'))
p=len(str(num))
copy=num
d_sum=0
while(num!=0):
    rem=num%10
    d_sum+=rem**p
    num//=10
if d_sum==copy:
    print('armstrong')
else:
    print('not armstrong')
    
#Disarium
num=int(input('enter num:'))
d_sum=0
p=len(str(num))
copy=num
while(num!=0):
    rem=num%10
    d_sum+=rem**p
    num//=10
    p-=1
if d_sum==copy:
    print('disarium ')
else:
    print('not disarium ')
    
#emirp 

num=int(input('enter number:'))
rev,f_c1,f_c2=0,0,0
copy=num
while(num!=0):
    rem=num%10
    rev=rev*10+rem
    num//=10
for value in range(1,copy+1):
    if copy%value==0:
        f_c1+=1
    
for value in range(1,rev+1):
    if rev%value==0:
        f_c2+=1
if rev!=copy and f_c2==2 and f_c1==2:
    print('Emirp')
else:
    print('Not emirp')

#Palyprime 
num=int(input('enter num: '))
rev=0
fc=0
copy=num
while(num!=0):
    rem=num%10
    rev=rev*10+rem
    num//=10
for value in range(1,copy+1):
    if copy%value==0:
        fc+=1
if rev==copy and fc==2:
    print('palyprime')
else:
    print('not palyprime')
    
    
#Strong number
num=int(input('enter number:'))
d_sum=0
copy=num
while(num>0):
    rem=num%10
    fact=1
    for value in range(rem,0,-1):
        fact*=value
    d_sum+=fact
    num//=10
if d_sum==copy:
    print('strong number')
else:
    print('not strong')
    
#evile number 
num=int(input('enter num:'))
d_sum=0

while(num!=0):
    rem=num%2
    d_sum+=rem
    num//=10
    
if d_sum==1:
    print('evile')
else:
    print('not evile')
    
#AutoMorphic
num=int(input('enter number:'))
sq=num**2
p=len(str(num))
rem=sq%(10**p)
if rem==num:
    print('auto morpic')
else:
    print('not auto morpic')
#Try morphic
num=int(input('enter numbers:'))
cu=num**3
p=len(str(num))
rem=cu%(10**p)
if num==rem:
    print('trymorphic')
else:
    print('Not try morphic')
    
#Happy number 
num=int(input('enter number:'))
while(num>9):
    d_sum=0
    while(num!=0):
        rem=num%10
        d_sum+=rem**2
        num//=10
    num=d_sum
if num==1:
    print('happy')
else:
    print('not happy')
    
#Decimal to binary
num=15
bin=0
p=1
while(num!=0):
    rem=num%2
    bin+=rem**p
    num//=2
    p*=10
print(bin)

#Binary to decimal
num=1111
dec=0
p=1
while(num!=0):
    rem=num%10
    dec+=rem**p
    num//=10
    p*=2
print(dec)

#TECH number 
num=2025
copy=num
d_sum=0
p=len(str(num))//2
while(num!=0):
    rem=num%(10**p)
    d_sum+=rem
    num//=(10**p)
if (d_sum*d_sum)==copy:
    print('tech')
else:
    print('not tech')