'''
Exercise #1
Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.
'''
def cubed_num():
    i = 1
    cubed = 0
    while cubed < 1000:
        cubed = i ** 3
        print(cubed)
        i += 1
cubed_num()

'''
Exercise #2
Get first prime numbers up to 100
'''
def prime():
    prime_num_list = []
    for i in range(1, 101):
        if i == 1:
            continue
        count = 1
        for j in range(2, i):
            if i%j == 0:
                count = 0
        if count == 1:
            prime_num_list.append(i)
    return prime_num_list

print(prime())

'''
Exercise 3
Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors
'''
def how_old():
    age = int(input("What is your age? (enter a number greater than 0): \n"))
    if age < 0:
        return "please input a number greater than 0"
    elif age < 18:
        return "kids"
    elif age < 65:
        return "adults"
    else:
        return "seniors"
    
print(how_old())
