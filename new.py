
#comments

########333
#
# efse
# efesfesef
print("**********")

#veriables
x=4
y="hi"
print(x)
print(y)

print("**********")

x,y,z="hi","bye",3

print(x,y,z)

print("**********")

print("My name is ", x,"and I am " ,z)

print("**********")

x=0.5
y=10

print(y/x)
print("**********")

a,b=2,3

print(round(a/b))
print("**********")

#starts from 1 not 0
d="hello world!"

print(d[2:])
print(d[:2])
print(d[6:11])

print("**********")

name="Aia Makhruka"

#first name
print(name[:3])
#latname
print(name[4:])
print("**********")

car=["KIA","BMW","Toyota"]
print(car)
print(car[2])
car[0]="Honda"
print(car)
print("**********")

# to delet an item
del car[2]
print("**********")

#to get the leangth
print(len(car))
print("**********")
print(car)
print("**********")
car.remove("Honda")
print(car)
print("**********")
fruit=["banana","orange","apple"]
print(fruit[0])
print(len(fruit))


print("**********")
# loop through array
for x in fruit:
    print(x)



print("**********")

a=100
b=300

if(a>b):
    print("a is biger than b")
else:
    print("a is smaller than b")

print("**********")
name1="Aia"
name2="aia"

if (name1.lower() == name2):
    print("it is the same")
else:
    print("it's not the same")
print("**********")
#loop
for x in range(6):
    print(x)

#starts from 2 insted
for a in range(2,6):
    print(a)

#???????????????????????????
#skips 1
for x in range(0,6,2):
    print("hi",x)

print("**********")
