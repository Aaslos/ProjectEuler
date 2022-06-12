print("Problem 7")
# Program to check if a number is prime or not

num = 2
limit = 200000
count = 0

while num < limit:
    flag = False

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    # check if flag is True
    if flag == False:
        count+=1
        if count == 10001:
            print(num, count)
    num+=1
