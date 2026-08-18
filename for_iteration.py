
my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)
# Using a for loop with a range:


for i in range(5):
    print(i)
# Using a for loop with a range and a step:


for i in range(0, 10, 2):
    print(i)
# Using a for loop with a range and a negative step:


for i in range(10, 0, -1):
    print(i)
# Using a for loop with a range and a variable to store the index:


my_list = [1, 2, 3, 4, 5]

for i, item in enumerate(my_list):
    print(i, item)


# while loop
i = 0

while i < 5:
    print(i)
    i += 1

is_running = True

while is_running:
    # do something
    # check if is_running is still True
    # if not, set is_running to False to exit the loop
    pass

i = 0

while True:
    print(i)
    i += 1
    if i >= 5:
        break

    i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)


for number in range(1, 10):
    if number % 2 == 0:
        continue
    print(number, 'is odd')


for number in range(1, 10):
    if number % 2 == 1:
        continue
    print(number, 'is even')


count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number, 'is even')
print(f'There are {count} even numbers')
