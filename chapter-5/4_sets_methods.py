set = {"Hamza", False, 1, 1, 2, 2, 3, 3, True, "Ahmed"}

# set.add("ABC") # To add anything   
# set.remove(2)      # remove elements
# set.discard(1)    # remove any element if not fond so No error, even if 1 is not in the set
# set.pop()        # remove RANDOM element 
# set.clear() # clear all elements

# print(set, type(set))





s1 = {1, 1, 2, 2, 3, 3, 4, 5, 6}
s2 = {3, 3, 4, 4, 5, 6}

# #UNION 
# print(s1.union(s2)) # result-->{1, 2, 3, 4, 5, 6} it sum up all elements 

# #INTERSECTION
# print(s1.intersection(s2)) # result-->{3, 4, 5, 6} the only element which is present in both sets

# # SUBSET
# print(s1.issubset(s2)) #fale
# print(s2.issubset(s1)) #true

# #SUPERSET
# print(s1.issuperset(s2)) #true
# print(s2.issuperset(s1)) #false