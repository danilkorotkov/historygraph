import os
#ld=os.listdir("/home/pi/Documents/Monkey Studio/My Progect")
ld=os.listdir(os.getcwd())
print ld

lf=[]
for i in range(len(ld)):
    if ld[i].endswith(".txt"):
        lf.append(ld[i])

print lf        
