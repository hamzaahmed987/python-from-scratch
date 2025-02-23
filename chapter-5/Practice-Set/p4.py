set = set() #empty set
set.add(10)
set.add(10.0)
set.add(10.00)
set.add("10")

print(set) # result-->{10, '10'} floating types didnt add bcz there value was same no matter here of data type
