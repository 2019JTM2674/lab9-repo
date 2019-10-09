#!/usr/bin/python3
#Creation of class Student
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

#Creation of class Student_Base
class Student_Base:
    totalMarks=89
    def __init__(self,roll):
        self.roll=roll
        
    #Add new student 
    def addNewStudent(self,new_nmae):
        pass
        
        
    #Update total marks   
    def displayMarks(self):
        print("Total marks of student with roll no.{} is {}".format(self.roll,Student_Base.totalMarks))

    #Display total marks\n   
    def updateMarks(self,update_marks):
        print("Total marks of student with roll no.{} is {}".format(self.roll,Student_Base.totalMarks))
        Student_Base.totalMarks=update_marks
        print("Updated marks of student with roll no.{} is {}".format(self.roll,Student_Base.totalMarks))

while 1:
    #creating instance of Student object
    student1=Student("krishna","25")
    flag = 0
    user=int(input("Enter\n1.Admin\n2.Student "))

    #User Validation
    if user == 1:
        password=input("Enetr Password ")
        flag=1
        if password == "iitd_1234":
            print("Admin login sucessfull")
    elif user == 2:
        stu_roll = input("Enter Roll no ")
        if stu_roll == "25":
            print("Student login sucessfull")
            s1=Student_Base(stu_roll)
            s1.displayMarks()
    
    #Functionality for admin
    if flag == 1:
        option=int(input("Enetr\n1.Add new student\n2.Update total marks\n3.Display total marks\n "))

        #Add new student
        if option == 1:
            new_name=input("Enter Student Name: ")
            new_roll=input("Enter Roll: ")
            a3=Student_Base(new_roll)
            a3.addNewStudent(new_name)
            new_student=Student(new_name,new_roll)

        #Update total marks
        elif option == 2:
            update_roll=input("Enetr roll number : ")
            a1=Student_Base(update_roll)
            a1.totalMarks = int(input("Enter updated marks : ")) 
            a1.updateMarks(a1.totalMarks)
        
        #Display total marks\n
        elif option == 3:
            disp_roll = input("Enter roll : ")
            a2=Student_Base(disp_roll)
            a2.displayMarks()




    x=int(input("Enetr 1 to exit and 2 to continue\n"))
    if x==1:
        break
    elif x==2:
        continue
    

    
        


