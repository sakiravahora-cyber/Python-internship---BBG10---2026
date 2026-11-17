# Corrected Code for Task 6
age = "20"
next_year_age = int(age) + 1
print("Next year I will be " + str(next_year_age))

# Explanation of the problem:
# 1. 'age' is a string ("20"), so 'age + 1' throws a TypeError because Python cannot add an integer (1) directly to a string. Converting it with int(age) fixes this.
# 2. In the print statement, 'next_year_age' becomes an integer (21), which cannot be concatenated directly with a string using '+'. Converting it back with str(next_year_age) fixes the second TypeError.