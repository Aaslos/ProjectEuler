print("Problem 6")
#The sum of the squares of the first ten natural numbers is,
#The square of the sum of the first ten natural numbers is,
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def squarenum(num):
    return num*num

i = 1
totalsquare = 0
totalsum = 0
while i < 101:
    totalsquare += squarenum(i)
    totalsum += i
    i+=1

print(squarenum(totalsum))
print(totalsquare)
print(squarenum(totalsum)-totalsquare)