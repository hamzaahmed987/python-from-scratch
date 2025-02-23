"""
Rules of Variables in Python

1. Variable names must start with a letter (a-z, A-Z) or an underscore (_), but not a number.
2. The rest of the variable name can contain letters, numbers (0-9), and underscores (_).
3. Variable names are case-sensitive (myVar, MyVar, and MYVAR are different).
4. Reserved keywords cannot be used as variable names (e.g., class, def, if, else, etc.).
5. Variable names should be meaningful and descriptive.
6. Spaces are not allowed in variable names.
7. Special characters (except _) are not allowed in variable names.
8. Variables can hold different data types.
"""

# Rule 1: Must start with a letter or underscore
valid_var = "Hello"  # ✅ Valid
_validVar = 42       # ✅ Valid
# 1st_var = 10       # ❌ Invalid (cannot start with a number)

# Rule 2: Can contain letters, numbers, and underscores
var_123 = "Python"   # ✅ Valid
myVar1 = 50          # ✅ Valid

# Rule 3: Case-sensitive
myvar = "lowercase"
MyVar = "Uppercase"
print(myvar)  # Output: lowercase
print(MyVar)  # Output: Uppercase

# Rule 4: Cannot use reserved keywords
# def = 5      # ❌ Invalid (def is a reserved keyword)
# class = "Python"  # ❌ Invalid

# Rule 5: Meaningful names
age = 25       # ✅ Good practice
x = 25         # ❌ Bad practice (not descriptive)

def calculate_total(price, tax):
    return price + tax  # ✅ Good practice (descriptive function and variables)

# Rule 6: No spaces allowed
# my variable = "Python"  # ❌ Invalid (spaces not allowed)
my_variable = "Python"    # ✅ Valid

# Rule 7: No special characters except underscore
# price$ = 100  # ❌ Invalid
price_value = 100  # ✅ Valid

# Rule 8: Variables can hold different data types
a = 10         # Integer
b = 3.14       # Float
c = "Hello"    # String
d = True       # Boolean
list_var = [1, 2, 3]  # List
dict_var = {"key": "value"}  # Dictionary

print(a, b, c, d, list_var, dict_var)
