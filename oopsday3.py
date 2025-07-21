class A : # example of method overriding 
    def __init__(self, name) :
        self.name=name 

    def n(self,net) :
        self.net=net 
        print(self.net)

    def bha(self ,age) :
        self.age=age
        print("self.age") 
    def __str__(self) :    # in str use only return  and also self 
        return self.name  
    def __add__(self,other) :  # dunder function 
        return self.name +other.name 

obj1=A("amithu") 
obj1.n("networth")
print(obj1)    # if we try to print object then we will get op but
#<__main__.A object at 0x00000234817D6A50>  as a result we use __str__
obj2=A("bhargav")  
p=obj1+obj2   # print  two objects 
print(p)

class B(A) :
    def __init__(self,name,sef) :
        super().__init__(name) 
        self.sef=sef
    
    def nit(self,weird) :
        self.weird=weird 
        super().bha(23) 

    def n(self,net):
        self.net=net
        print(self.net)
obj2=B("bhargav", "defff",)
obj2.n("worthnet") 


class c : 
    def __init__(self, name) :
        self.name=name 
    

from abc import ABC , abstractmethod 
class A(ABC) :  # abstract class 
    @abstractmethod 
    def bha(self , key) :
        pass 

class b(A) :
    def bha(self ,ey) :   # see here ey is there but in abstractmethod key
        self.ey=ey    #that is not problem bust paramater no worries  but method name should be same 
        print(self.ey) 
obj=b() 
obj.bha("koko")

   #CLASS METHOD  
"""class c :     # thi scode works without abstract nmetho dwe can increment but  
    increment =10000       we use abstract method , bcs thi sworks only for instance metod 
    def __init__(self,name) : nj() not for other methods so we use classmetod
        self.namee=name 
    def nj(self ,lo) :
        self.lo=lo 
        print(self.increment +10000 )
        
obj=c("amith") 
obj.nj("looooooop") """

class c :      
    increment =10000        
    def __init__(self,name) : 
        self.namee=name 
    @classmethod
    def nj(cls,lo) :
        cls.lo=lo 
       # return(cls.increment +=10000 )     # if u simply write like cls.increment+10000 it wont  update in other methods
        cls.increment+=100000
        return cls.increment
    def ji(self) :   # afer creating classmethod i am trying if it works will it also get 20k
        return(self.increment) # nope it wont 
    @classmethod
    def qw(cls) :
        return cls.increment
    
obj1=c("bhatgav") 
print(obj1.nj("pooil"))  
print(obj1.ji())   # see here i ma just using self in ji() method so it is =gibving me op ad 1ok
print(obj1.qw())
