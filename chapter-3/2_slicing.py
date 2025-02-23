#index starts from 0

#       01234 - index is 4 but length is 5(bcz there are 5 alphabets) of my name 
name = "Hamza"
someCharacters = name[0:3] #taking numbers from 0-3(excluding 3) we wil not get index 3. result will be Ham
print(someCharacters)

# negative slicing
fullName = "Hamza Ahmed"
#          -10       -1
# lastName = fullName[-5:-1]
lastName = fullName[6:10]

print(lastName)

print(fullName[0:]) #0 to end
print(fullName[:-1]) #start to -1



#  --SKIP VALUE--

a = "0123456789"
print(a[1:7:2]) #start from index 1 and end on index 7 and have to skip 2 values - result is 135 why bcz based on indexes our initial pt is 1 and end pont is 6 - we took one bcz it start and will skip 2 values so we get 3 and the skip 2 valus and got 5 and now we cant skip 2 values bcz ending pt in 6



