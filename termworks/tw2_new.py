
def AddCourse(courses):
    course_code=int(input("Enter the course code"))
    course_name=input("Enter course name")
    faculty=input("Enter Faculty Name")
    registrations=int(input("Enter number of registrations"))
    courses[course_code]={'Course Name':course_name,'Faculty Name':faculty,'Registrations':registrations}

def Highest(courses):
    max=-1
    max_name=None
    for course_code,code in courses.items():
        if code['Registrations']>max:
            max=code['Registrations']
            max_name=code['Course Name']
            print(f"Maximum Registrations course is {max_name}")
            


        

def DisplayCourse(courses):
     a=int(input("Enter course code"))
     if a in courses:
        print(courses[a])
     else:
        print("Invalid Course")

    

def DisplayAll(courses):
    print(courses)
    

def main():
    courses={}
    menu={1:AddCourse,2:Highest,3:DisplayCourse,4:DisplayAll}
    while True:
        print("1:Add courses\n 2:Find Highest Registration\n 3:Display Course Details\n 4:Display All courses\n 5:Exit ")
        choice=int(input("Please enter your choice"))
        if choice==5:
            break
        else:
         menu[choice](courses)
if __name__ =="__main__":
    main()

        

