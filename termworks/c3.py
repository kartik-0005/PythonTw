
def AddData(courses):
    cc,cname,fac,num = input("Enter Course Code, Course Name, Faculty, Num of regs").split()
    num = int(num)
    courses[cc] = [cname,fac,num]
    #print(courses)

def HighestReg(courses):
    max=0
    for key,val in courses.items():
        if val[2]>max:
            max=val[2]
    
    hcourses=[]
    for key,value in courses.items():
        if value[2]==max:
            hcourses.append([key,value])
            break
    print(hcourses[0])


def DispAssDetails(courses):
    if len(courses)==0:
        print("Courses dont exist")
        return
    ccode=input("Enter code: ")
    if ccode in courses:
        print(ccode,'   ', courses[ccode])
    else:
        print("No Course with that code")

def DispAllDetails(courses):
    if len(courses)==0:
        print("Courses dont exist")
        return
    print("Courses are: ")
    for x, y in courses.items():
        print(x,'   ',y)


def main():
    courses=[]
    #courses ={"20CS43":["Python","PVT",20], "20CS42":["Math", "DIG",20] }
    menuDict = {1:AddData, 2:HighestReg,3:DispAssDetails,4:DispAllDetails}
    while True:
        choice = int(input("Enter 1.AddData 2.HighestReg 3.DispAssDetails 4.DispAllDetails 5.Exit\n"))
        if choice == 5:
            break
        menuDict[choice](courses)
    print("End of program")
        
if __name__ == "__main__":
    main()



        
