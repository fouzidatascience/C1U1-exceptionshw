# I'm pretty sure you guys put the solution instead of the question before, now it's fixed.

a = 12 
s = "hello"

try:
    print(a+s) # This will raise TypeError because a and s aren't from the same type
    print("This message won't be seen") # This instruction won't be executed because the one above will raise an error
except TypeError:
    print("TypeError has been raised")
    print(str(a) +s) # We convert a into a string to not raise TypeError anymore. (aka. this is the correct way to do it)

# Bye
