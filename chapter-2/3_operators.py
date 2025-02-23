#Arithmetic Operators

a = 10
b = 90
c = a + b
 
print(c)  # 100



#Assignment Operators

d = 20-10 # Now 20-10 is assign to "d"
d += 30  # Increment / add 30 into "d" and then assign to "d"
# d -= 2
# d *= 3
# d /= 2
print(d)  # == 40



#Comparison Operators   ---> ALWAYS RETURN BOOLEAN

x = "hamza"
y = "9"
z = x == y 
print(z)  # False

e = 5<4
print(e) # False

f = 10>=10 # true
print(f)

q = 5!=5
print(q) #false 5 is equal to 5



#Logical Operators

#or
print("True or True -->",True or False)
print("True or False -->",False or False)
print("False or False -->",False or False)

print("--------------------------")

#and
print("True and True -->",True and True)
print("True and False -->",True and False)
print("False and False -->",False and False)
print("True and True -->",True and True)

print("--------------------------")

#not
print(not(True)) #FALSE