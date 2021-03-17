userNumber = int(input("Please insert a number: "))
 
def fibonacci(userNumber):
    preFib = 0
    nextFib = 1
    sumFib = 0
    while (nextFib < userNumber):
        sumFib = nextFib + sumFib
        nextNumb = preFib + nextFib
        preFib = nextFib
        nextFib = nextNumb
    print(sumFib)

def primeNumber(userNumber):
    for i in range(2,userNumber):
      if (userNumber%i==0):
        print(userNumber,"is not a prime number")
        return
    else:
        print(userNumber,"is a prime number")
        return

def binary(userNumber):
     if userNumber >= 1:
       binary(userNumber//2)
     print(userNumber % 2,end="")
     return

def main(userNumber):
    fibonacci(userNumber)
    primeNumber(userNumber)
    binary(userNumber)
main(userNumber)
