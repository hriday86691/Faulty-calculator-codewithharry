#Faulty calculator

# Design a calculator which will correctly solve all the problems except the following ones:
# 45 * 3 = 555, 56 + 9 = 77, 95-7=44, 56 / 6 = 4

print("enter first no : ")
n1=input()
print("enter second no : ")
n2=input()
print("operator=  1.plus , 2.minus , 3.multiply , 4.divided , 5.percentage ")
op=input()
#Fulty calculate
if n1=="45" and n2=="3" and op=="3":
	print(n1,"+",n2,"=",555)
elif n1=="56" and n2=="9" and op=="1":
	print(n1,"-",n2,"=",77)
elif n1=="95" and n2=="7" and op=="2":
	print(n1,"*",n2,"=",44)
elif n1=="56" and n2=="6" and op=="4":
	print(n1,"/",n2,"=",10)

#correct calculate

elif op=="1":
	print(n1,"+",n2,"=",float(n1)+float(n2))
elif op=="2":
	print(n1,"-",n2,"=",float(n1)-float(n2))
elif op=="3":
	print(n1,"*",n2,"=",float(n1)*float(n2))
elif op=="4":
	print(n1,"/",n2,"=",float(n1)/float(n2))
elif op=="5":
	per=float(n2)/float(100)*float(n1)
	print(n1,"%",n2,"=",float(n1)-float(per))
else :
	print(" INVALID KEYWORD")
