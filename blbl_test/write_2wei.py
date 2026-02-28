ls=[
    ["sno","sex","age","name"],
    ["101","man","11","1"],
    ["102","man","12","2"],
    ["103","woman","13","3"],
    ["104","man","14","4"]
    ]
f=open("students.csv","w")
for i in ls:
    f.write(",".join(i)+"\n")
f.close()