# variable declaration
course = 'Python for Beginners'


# log
print(course)

# variable declaration
first = "Joshua"
last = "Idara"

full = first + ' ' + last

# log
print(full)

# literal string
msg = f'Hello {first} {last}'
print(msg)

# str
# num
# bool
# list
# tuple
# set
# dict


# string methods
print(course.swapcase())
print(course.count('l'))
print(course.startswith('hello'))
print(course.endswith('world'))
print(course.split(' '))
print(course.upper())
print(course.lower())
print(course.title())
print(course.find('beginners'))
print(course.replace('beginners', 'Absolute Beginners'))
# replace('old', 'new')
print('Python' in course)  # True (check if the string is in the variable)
# true (check if the string is in the variable)
print('Development' not in course)

# string slicing
print(course[0:3])
print(course[:3])
print(course[3:])
print(course[-4:])
print(course[:])

# string formatting
print('Hello my name is %s and I am a %s' % (first, last))
print('Hello my name is {} and I am a {}'.format(first, last))
print(f'Hello my name is {first} and I am a {last}')


# number
x = 10
y = 3

print(x + y)
# addition
print(x - y)
# subtraction
print(x * y)
# multiplication
print(x / y)
# division
print(x // y)
# floor division
print(x ** y)
# power (exponentiation)
print(x % y)
# modulus

print('next line')
m = 16
t = m + 3
m += 3
print(t, 't')
print(m, 'm')

# comparison operators
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x == y)
print(x != y)

# logical operators
print(x > 3 and x < 10)
print(x > 3 or x < 10)
print(not (x > 3 and x < 10))

# identity operators
print(x is y)
print(x is not y)

# membership operators
print(x in [1, 2, 3])
print(x not in [1, 2, 3])

# bitwise operators
print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(x << 2)
print(x >> 2)

# ternary operator
print('x') if x > y else print('y')

# assignment operators
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x //= 3
print(x)
x **= 3
print(x)
x %= 3
print(x)

# conditional statements
print('x') if x > y else print('y')

age = 18
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

if x > 0:
    print('x is positive')
elif x < 0:
    print('x is negative')
else:
    print('x is zero')

temperature = 25
if temperature > 30:
    print('It is hot')
elif temperature > 20:
    print('It is warm')
else:
    print('It is cold')
print('Done')

# while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# for loop
# basic
for i in range(1, 11):  # range(start, end, step)
    print(i)
# advance
for i in range(1, 11):
    print(i)

# basic
for i in range(1, 11, 3):  # range(start, end, step)
    print(i)
# advance
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# continue
# basic
for i in range(1, 11):  # range(start, end, step)
    if i == 5:
        continue
    print(i)

# advance
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# and - both conditions must be true
# or - at least one condition must be true
# not - reverse the condition
