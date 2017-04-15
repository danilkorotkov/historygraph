import time, datetime
t=time.time()
print (t)
s=datetime.date.fromtimestamp(t)
print (s)
s1=time.ctime(t)
print(s1)
s2=time.gmtime(t)
for i in range(len(s2)):
    print(s2[i])
s3='%s-%s-%s %s:%s:%s' % (str(s2[0]),str(s2[1]),str(s2[2]),str(s2[3]),str(s2[4]),str(s2[5]))
print(s3)
