'''
Let's say we want to check below condition:
a < b < c

Most common syntax:
if a < b and b < c:
    # do smth

In Python, there is a better way to do this:
if a < b < c:
    # do smth
Like in math and doesn't load b on a stack again
'''

x = 25
print(5 < x < 100) # True
print(25 < x+10 < 50) # True
print(25 == x > 10) # True
print(20 > x <= 30) # False