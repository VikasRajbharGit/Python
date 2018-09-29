import os
filename=input("Enter the filename to decrypt")

try:
    file=open(filename,"rb")
except FileNotFoundError as identifier:
    print(identifier)
    os._exit(1)
#file=open("newfile.vikas","rb")
dec=open('decoded1.png','wb')
key1=open('key11.viron','r')
key2=open('key22.viron','r')
key1cont=key1.read()
key2cont=key2.read()
cont=file.read()
bi=bytearray(cont)
new=bytearray(len(bi))
count=0
k2list=list(key2cont.split(' '))
for i in k2list:
    #temp=int(i)
    #print(i)
    #print(bi[int(i)])
     bi[int((int(i)-10)/10)]=int(bi[int((int(i)-10)/10)])-50

dec.write(bi)

