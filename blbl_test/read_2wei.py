f=open("students.csv","r")
students_ls=[]
for i in f:
    i=i.strip("\n")
    i=i.split(",")
    students_ls.append(i)
f.close()
print(students_ls)