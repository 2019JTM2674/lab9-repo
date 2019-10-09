#!/usr/bin/python3

#Creation of class Author
class Author:
    def __init__(self,name,email,gender):   #initialising function
        self.name=name
        self.email=email
        self.gender=gender
        
    def get_name(self):                     #Getter for name
        return self.name
    
    def get_geder(self):                    #Getter for gender
        return self.gender
    
    def set_email(self,new_email):          #Setter for email
        self.email=new_email
    
    def get_email(self):                    #Getter for email
        return self.email
        
    def printinfo(self):                    #print function
        print("{} ({}) at {}".format(self.name,self.gender,self.email))
    
    
    
    

#creating instance of Author object
person1=Author("Krishna","kc@gmail.com","m")
person1.printinfo()
