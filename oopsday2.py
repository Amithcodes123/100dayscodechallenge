class Amith :                                         #class
    name=1000                                         #class atribute
    def __init__(self , name ,marks, age) :  #age=30            #constructor and default paramter
        self.name=name                                 #attributes
        self.age=age
        self.__marks=marks                          #private attribute , encapsulation 
       # print(self.x) #ERROR -> u cnt use methods self in attribute 


    def bha(self,x) :                                  #method
        self.x=x                                  #if u dont use self then u cannot use thi sin method 
        print(self.name)
        print(self.x)                             # u can also use method inside methood 
        print(self.name) 
        print(self.__marks) 

#print(self.name)  ERROR because  it is outside the function  

    @staticmethod                                   #static method 
    def se(nith) :
        #  print(self.name)                    #ERROR u cant do this in staticemthod 
        return nith*2 
    @property 
    def pop(self) : 
        print(self.age + 2)

obj1=Amith("amith" ,98 , 19)                                     #object 
obj2=Amith("bha",99,21)                                   #to check default paramater
print(obj1.se(300) )                              # this is for static method 
print(obj1.pop)                                    # with the property 
print(obj1.name)
#print(obj1.__marks)                      ERROR u cant access directly u shld use method 
print(obj1.bha(90900))          #  acessing  private attribbute using method 
print(obj1._Amith__marks)      # using name mangling 
obj1.bha(2345)
obj2.bha(23)
v=obj2.age 
print(v) 

class b (Amith) :
    def __init__(self , name ,marks, age , gender) :
        super().__init__( name ,marks, age) 
        self.gender=gender 
    def ji(self,nit) :   #method
        super().bha("nkn") 
        self.nit=nit 
        return(self.nit) 
    
objec=b("suma" ,65,26,"male") 
print(objec.ji("sastha")) 

# we can pass methods valuw by assigning value 
class bha :
    def __init__(self,name):
        self.name=name 
        print(self.name)
        self.x=self.bh(1000)    # we can write this  also self.x = 1000 
        print(self.x)           # 
    def bh(self,x) :
        return x     #def bh(self, x):   use this when u r Doing some logic or calculation
                      #return x * 2

on=bha("amith") 


#QUESTOION 
class Student :
    def __init__(self ,name, marks) :
        self.name=name
        self.marks=marks 
    def avg(self) :
        return sum(self.marks)/len(self.marks) 
    
obj=Student("amith" ,(2,3,4)) 

# create account class with 2 attributes balance and account number , 
# create method for debit,credit and printing balance 

class Account :
    def __init__(self,balance, accountno) :
        self.balance=balance
        self.accountno=accountno 
    def debit(self,deducted) : 
        self.balance-=deducted 
        return self.balance
    def credit(self,added) : 
        self.balance+=added 
        return self.balance

obj1=Account(10000,123) 
print(obj1.debit(500))


