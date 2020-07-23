# Lambda means "make" a function for future

(lambda x: x**2)(5) # 25

# To compute something in one line
100 + (lambda x: x**2)(5) + 25  # 150

# To save result for future
x = 10
y = 5
f = lambda: x**2 + y
f() # 105 