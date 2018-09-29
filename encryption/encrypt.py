import os
filename=input("Enter the filename to encrypt")
try:
    file=open(filename,"rb")
except FileNotFoundError as identifier:
    print(identifier)
    os._exit(1)
#file=open(filename,"rb")

cont=file.read()
bi=bytearray(cont)
new=bytearray()
key1=[]
key2=[]
count=0
#print(bi[0:10])
for i in bi:
    #sum=int(bi[i])+int(bi[count])/10
    
    if (i>150):
        sum=int(i)
        #sum="{0:x}".format(sum)
        key1.append(count)
        new.append(sum)
    else:
        sum=int(i)+50
        key2.append(count*10+10)
        #sum="{0:x}".format(sum)
        #print("{}={}+{}".format(sum,bi[i],50))
        new.append(sum)
    count=count+1
#print(new)
key1str=" ".join(str(x) for x in key1)
key2str=" ".join(str(x) for x in key2)
#print(type(cont))
#print(new)
#print(type(bi))
newfile=open("newfile1.vikas","wb")
newfile.write(new)
newfile.close()
file.close()
#print(count)
k1=open("key11.viron","w")
k2=open('key22.viron','w')
k1.write(key1str)
k2.write(key2str)
k1.close()
k2.close()