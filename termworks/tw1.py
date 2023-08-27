''' 
Develop a menu driven program to implement a queue.The operations would be 
a) Add an item
b) Delete an item
c) Display an item
'''

def AddQ(queue):
    item=input("Enter a element to be stored in the queue")
    queue.append(item)
    print("Item:"+item+" added")
    

def DelQ(queue):
    if len(queue)==0:
       print("Queue is empty")
    else:
     item=queue.pop(0)
     print("item:" +item+" is deleted")

def DispQ(queue):
    if len(queue)==0:
       print("Queue is empty")
    else:
     print(queue)
    

def main():
    queue=[]
    while True:
     choice=int(input("Enter 1.Add 2.Delete 3.Display 4.Exit\n"))
     if choice==1:
        AddQ(queue)
     elif choice ==2:
        DelQ(queue)
     elif choice==3:
        DispQ(queue)
     else:
        break
        print("End of program") 
if __name__ == "__main__":
    main()

    

