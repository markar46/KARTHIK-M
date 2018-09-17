#program to cheak age for vote 
#input a from keyboard 
a=int(input("a:"))
#print a from keyboard 
#input b from keyboard 
b=int(input("b:"))
#print b from keyboard
print("a:",a)
if(a>b):
	print(a,"is greater",b)
elif(a==b):
	print(a,b,"are equal")
else:
	print(b,"is greater",a)