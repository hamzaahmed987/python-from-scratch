#List is mutable 


abc = ["hamza", 123, True,  123.098 ,"Amir"]
print(abc)

abc.append("Khan") #append means add something in the end
print(abc)

l1 = [8, 2, 1, 9, 5, 3, 7]
l1.sort() #it sorts the list
print(l1)

l2 = [1, 2, 3, 5, 7, 8, 9]
l2.reverse() #this method reverse the list
print(l2)

l3 =  [1, 2, 3, 5, 7, 8, 9]
l3.insert(3,4) #insert "4" on index 3
print(l3)

l4 = [1, 2, 3, 5, 7, 8, 9]
value = l4.pop(6) #remove index 6
print("value after popped",l4)
print("pooped value",value) 


l5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l5.remove(8) #remove the integer you want
print(l5)