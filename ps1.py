#!/usr/bin/python3
class Author:
    def __init__(self,name,email,gender):
        self.name=name
        self.email=email
        self.gender=gender
        
    def get_name(self):
        return self.name
    
    def get_geder(self):
        return self.gender
    
    def set_email(self,new_email):
        self.email=new_email
    
    def get_email(self):
        return self.email
        
    def printinfo(self):
        #print(self.name,"(",self.gender,") at",self.email)
        print("{} ({}) at {}".format(self.name,self.gender,self.email))
    
    
    
    


person1=Author("Krishna","kc@gmail.com","m")
person1.printinfo()
