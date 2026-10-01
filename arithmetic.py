# addition
print(3+2+5) 


# substraction
print(10-3)

# multiplication
print(3*10)

# division
print(7/2)

# floor division
print(7//2)


# modulus
print(7%3)


# exponential
print(2**10)


# Basic comparisons
print(10 == 10) # → True
print(10 != 5) # → True
print(10 > 20) # → False

# Chained comparisons — unique to Python, reads like maths
x = 5
print(1 < x < 10) # → True (x is between 1 and 10)
print(0 <= x <= 5) # → True
print(5 < x < 10) # → False (x is not greater than 5)


# String comparisons — lexicographic (letter by letter)
print("apple" < "banana") # → True ('a' < 'b' in Unicode)
print("Python" == "python") # → False (case-sensitive!)


# Comparing booleans with numbers
print(1 == True) # → True (True equals 1 in Python)
print(0 == False) # → True (False equals 0 in Python)
print(1 == "1") # → False (int and str are different types)


# Swap variables — Pythonic way, no temporary variable needed
a, b = 10, 20
a, b = b, a # swap!
print(a, b) # → 20 10

# and - both conditions must be true
username = "Saksham"
password = "Alu"
print(username and password)


# or - atleast one condition must be true
card = 1234
password1 = 0
print(card or password1)

# Short-circuit with 'and' — right side skipped if left is False
print(False and 1/0) # → False (no ZeroDivisionError!)


# Short-circuit with 'or' — right side skipped if left is True
print(True or 1/0) # → True (no ZeroDivisionError!) 
# or ko case ma false rakhyoo bhane error aaucha kina ki aauta false bhaye pani arko check garchha ani ma 1/0 cha ani thats not possiblle

# &
print(5&3) 
# &
print(5&3)

# ^
print(5^3)
