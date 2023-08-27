import csv

# # with open("abc.txt","w") as outfile:
# #     outfile.write("Hello guysss")

# file=open("abc.txt","w")
# # print(file.readline())

# file.write("welcome to this place")
# print(file.readlines())


# with open("abc.txt","w") as file:
#     file.write("Hello welcome guyss")

# with open("abc.txt","a") as file:
#     file.write("Yoo guyss")
#     # moment=file.read()
    
# with open("abc.txt") as file:
#     ab=file.readline()
#     print(ab)


a=["harliey quin","Superman","Bruce wayne","Batman"]
with open("abc.txt","w") as file:
    for b in a:
        file.write(b)

with open("abc.txt","r") as file:
    files=file.readlines()
    print(files[0], end=" ")