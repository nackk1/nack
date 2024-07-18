X = 10 
y = 20
Z = 30
# Using 'and' operator
if X < y and y < Z:
    print("x is less than y and y is less than z.") # True

# Using 'or' operator
if X < y or y > Z:
    print("Either x is less than y or y is greater than z.") # True

# Using the 'not' operator
if not (X > y):
    print("x is not greater than y.") # True