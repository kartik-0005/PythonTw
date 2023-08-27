import csv

def searchBkAuthor():
    author = input("Enter author name:")
    with open("TW3.csv") as outfile:
        reader = csv.reader(outfile)
        result = []
        for row in reader:
            if row[2] == author:
                result.append(row)

        if result == []:
            print("No book found")
        else:
            print("Books with the specified author are...")
        for line in result:
            print(line)

def searchBkPrice():
     price = input("Enter price:")
     with open("TW3.csv") as outfile:
        reader = csv.reader(outfile)
        result = []
        for row in reader:
            if row[3] <= price:
                result.append(row)

        if result == []:
            print("No book found")
        else:
            print("Books with the specified author are...")
        for line in result:
            print(line)

    

def searchBkTitle():
    word=input("Enter words")
    with open("TW3.csv") as outfile:
        reader=csv.reader(outfile)
        result=[]
        for row in reader:
            lstTitle=row[1].split()
            if(word in lstTitle):
                result.append(lstTitle)
        if result==[]:
            print("No book found")
        else:
            print("Books with specified title are...")
        for line in result:
            print(line)
    

def readSaveBookInfo():
    bookLst=[]
    while True:
        bookNo = input("Enter book num:")
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        price = int(input("Enter book price:"))
        price = int(price)
        bookLst.append([bookNo, title,author, price])
        ch = input("Enter Y/N to enter more:")
        if(ch.upper() == "N"):
            with open("TW3.csv","w")as outfile:
                writer = csv.writer(outfile,lineterminator = "\n")
                writer.writerows(bookLst)
            break

def main():
    readSaveBookInfo()
    menuDict = {1:searchBkAuthor, 2:searchBkPrice, 3:searchBkTitle, 4:"Exit" }
    while True:

        choice = int(input("Enter choice \n 1:searchBkAuthor, 2:searchBkPrice, 3:searchBkTitle, 4:Exit :"))
        if choice == 4:
            break
        menuDict[choice]()


if __name__ == "__main__":
    main()
