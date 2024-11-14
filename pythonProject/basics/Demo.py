from operator import concat

print("Hello")
a=3
print(a)

S="June"
K="test"
print(S)
print()
formatted_string = '{} {}'.format("value is:", a)
print(formatted_string)
print()
print(S+ " Concant with " +K)
print(type(a))
print()


#ist
L=[2,5,6,"Sot",7,8,9]
print(L)
print(L[5])
print(L[-1])
print(L[2:6])
L.insert(4,"test")
print(L)
print(L[2:6])
L.append("Ending")
print(L)
L[3]="Sit"
del L[2]
print(L)

#Tuple immutable
ai=(1,4,6,7)
print(ai[2])

#dictenory
values={"a":4, "b":98}
print(values)
print(values["a"])

#adding values in runtime dicnary
dic={}
dic["name"]="Sudhee"
dic["age"]=23
dic["city"]="South"
print(dic)
