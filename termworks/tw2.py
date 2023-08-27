''' 
Store the following information in a dictionary:
Course code: Course Name, Faculty Name, Number of registrations.
Perform the following operations using functions:
a. Find course name that has highest number of registrations.
b. Given the course code, display the associated details.
Display details of all courses
'''

def AddData(courses):
    cc,cname,fac,num=input("Enter the course code, course name,faculty name and no of registrations").split()
    num=int(num)
    courses[cc]=[cname,fac,num]
    


def HighestReg(courses,cc):
    max_registration=0
    max_registration_name=none
    for cc,x in courses:
       if x['num']>max_registration:
          max_registration=x['num']
          max_registration_name=x['cname']
          print(max_registration,max_registration_name)
       
    
    print("Highest")

def DisplayDetails(courses):
    if len(courses)==0:
     print("No courses exist")   
     return
    ccode=input("Enter course code")
    if ccode in courses:
       print(ccode,' ', courses[ccode])
    else:
       print("No course with that code")

def DisplayAll(courses):
    if len(courses)==0:
       print("Courses dont exist")
       return
    print("Courses are: ")
    for x,y in courses.items():
       print(x,' ',y)
        

def main():
    courses={}
    menuDict={1:AddData,2:HighestReg,3:DisplayDetails,4:DisplayAll}
    while True:
        choice=int(input("Enter 1)AddData, 2) HighestReg, 3)DisplayDetails, 4)DisplayAll, 5) Exit \n "))
        if(choice)== 5:
            break
        menuDict[choice](courses)
    print("End of program")


if __name__=="__main__":
 main()

