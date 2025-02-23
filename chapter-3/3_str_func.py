a = "hamza ahmed"

print("Length of my name:",len(a))

b=a.endswith("za")
print("name ends with za:",b)

c=a.startswith("ha")
print("name starts with Ha:",c)

d=a.capitalize()
print("Capitalize:",d)

e=a.lower()
print("lower:",e)

f=a.upper()
print("upper:",f)

g=a.title()
print("title:",g)

h=a.replace("hamza","khamzaat")
print("replaced",h)


i = "   "#there will bw only space  nothing esle
ii=i.isspace()
print("isSpace:",ii)

j = "123s"
k=j.isdigit() #fals bcz there is alphabet also
print("isDigit",k)


jj = "abc123"
l=jj.isalpha()  #alpha == "abc"
print("isAlpha",l)