##Number guessing Game
import math
import random
## Taking input of range of number
a=int(input("Enter lower limit of number="))
b=int(input("Enter upper limit of number="))
##cjecking whether limits are valid or not
if a==b or a>b:
   print("ERROR,both limit can't be same ,or lower limit can't be greater than upper limit")
if a<b:
## selecting a random number
    num=random.randint(a,b)
## calculating number of attempts
    count=round(math.log(b-a+1,2))
    print("You have {} attempts ".format(count))
    i=0
    if i<count:
        while i<count:
            i+=1
            ## Taking input Of guessed number by user
            num1 = int(input("Enter your guess="))
            ## check whether guessed number is right or not
            if num1==num:
                print("***************************")
                print(" you guess the right number in your {} attempt".format(i))
                print("***************************")
                break

            elif num1<num:
                print("the guessed number is too less ")
            elif num1>num:
                print("the guessed number is too large ")
            print("You have ",count-i,"attempts left.")


        ## message for failed attempt
        if i>=count:
            print("*************************************")
            print("\nOOPS!you have reached maximum attempts limit")
            print("\nthe number was {}".format(num))
            print("\nbetter luck next time!!")
            print("*************************************")
print("\n***Thank You***")
