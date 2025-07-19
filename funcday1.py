# 1 Write a function that takes a list and returns the sum of even numbers. 
def abc() : #SUM TH EEVEN NUMBERS
    op=0
    x=[2,3,4,5,6]  
                  # if (x%2==0) :  this doesnt work bevcause u r havign list sofirst u neeed to unwrap it
    for y in x :
        if (y%2==0 ):
            op+=y 
    return op 
kl=abc()
print(kl) 


#2 3 COUNT THE EVEN NUMBERS 
# Write a function that counts the number of vowels in a string. 
def abc():
    ct=0  #count
    x=input("enter a string ") 
    a="aeiou" 
    # if x in a :   if we use this it checlks for entire strind since we want to check each word we use 
    #     ct+=1  
    for y in x :
        if y in a :
            ct+=1 
    return ct 
a=abc()
print(a) 

# 3 similar to it but the thing is here we print the even n umbers in list 
def abc() :
    op=[]
    x=[2,3,4,5,6] 
    for y in x :
        if(y%2==0) :
            op.append(y)
    
    return op
nkn=abc()            
print(nkn) 

#4 Write a function that returns both sum and average of numbers in a list.

def func() :
    s=0
    a=0
    x=[2,3,4] 
    for y in x : 
        s+=y   # sum 
        op=s/len(x)  #average ,  
    return s,op
k=func()
print(k) 

# using global variable inside the function 
x=20 #global variable 
def a() :
    global x 
    x+=5 
a()

#Use map() with a lambda function to convert a list of strings to uppercase.
li=["apple" , "orange"] 
x=map(lambda a:a.upper() , li)
print(list((x))) 


#Use filter() with lambda to filter out negative numbers from a list.
li=[2,4,-2,-4,-1,1] 
x=filter(lambda a:a<0 ,li)
print(list((x))) 

#Write a function that returns both sum and average of numbers in a list.

def abc() :
    sum=0
    x=[2,3,4,56,6] 
    for y in x :
        sum+=y 
        op=sum/len(x)
    return sum ,op
y=abc()
print(y)    

def abx(a):   # factorial 
    if a == 0 or a == 1:
        return 1
    else:
        return a * abx(a - 1)
for i in range(5) : 
    z=abx(i) 
    print(z)

result = abx(5)  # example: factorial of 5
print(result)    # prints 120

def ab(a) :  # fibonacci series 
    if a ==0 :
        return 0
    elif a==1 :
        return 1 
    else :
        return ab(a-1)+ab(a-2) 
for i in range(5) :
    print(ab(i))
    ""

#Write a recursive function to reverse a string.
# def ami() :# for this code it only print a in amith because after thi swill it will come out of the loop 
#     a="amith"
#     for x in a :
#         return x 
# u=ami()
# print(u)  
#string_to_reversed_list
def ami() :
    x="amith"
    y=x[::-1]
    return y
z=ami()
print(z)   


def ami() :
    x="amith"
    if 
    y=x[::-1]
    return y
z=ami()
print(z)   
        
def ami() :
    s="amith"
    if len(s)==0 :
        return ami(s[1:]) + s[0
ami()
#or

def reverse_string(s):
    if s == "":
        return s
    return reverse_string(s[1:]) + s[0]