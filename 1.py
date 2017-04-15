file_name="1_1492008329_160.txt"
lines=[]
file=open(file_name)
for line in file:
    lines.append(line.rstrip('\n'))
file.close()

#print lines

cpw=[]
for i in range(len(lines)):
    cpw.append(lines[i].strip().split(','))

#print cpw    

xy=[]
for i in range(len(cpw)):
    xy.append([])
    for j in range(len(cpw[i])):
        xy[-1].append(float(cpw[i][j]))

print xy        
