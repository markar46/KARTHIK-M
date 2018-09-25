#program to check the value of numbers
#input a from keyboaed
a=int(input("enter value of a:"))
#print b from keyboaed
b=int(input("enter value of b:"))
#print value of a
print("a:",a)
#input value of b
print("b:",b)
if(a>b):
	print(a,"is greater ")
elif(b>a):
	print(b,"is greater")
else:
	print("both are equal")