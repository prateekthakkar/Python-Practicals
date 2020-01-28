from getpass import getpass
import time
import re
def add(number1,number2):
    return number1+ number2

def sub(number1,number2):
    return number1 - number2

def multi(number1,number2):
    return number1 * number2

def div(number1,number2):
    return number1 / number2

def factorial(number):
    fact=1
    for i in range(1,number+1):
        fact=fact*i
    return fact

def prime(number):
    if number > 1:
       for i in range(2,number):
           if (number % i) == 0:
               print(number,"is not a prime number")
               break
       else:
           print(number,"is a prime number")
       
        # if input number is less than
        # or equal to 1, it is not prime
    else:
       print(number,"is not a prime number")
    return(number)

def palinum(number):
    temp=number
    rev=0
    while temp!=0:
        rev=(rev*10)+(temp%10)
        temp=temp//10
    if rev==number:
        print(number,"Is Palindrome")
    else:
        print(number,"Is Not Palindrome")

def palistr(string):
    l=string
    rev=l[::-1]
    if rev==l:
        print(string,"Is Palindrome")
    else:
        print(string,"Is  Not Palindrome")

def pangram(string):
    l=[]
    for i in range(97,123):
        c=chr(i)
        l.append(c)
    s=set(l)
    if s==string:
        print("String Is Pangram")
    else:
        print("String Is Not Pangram")
        
print("---*It's Just Simple Login System*---")
localtime = time.asctime(time.localtime(time.time()))
print(localtime)
def passwords(password):
    # Python program to check validation of password 
    # Module of regular expression is used with search() 
    flag = 0
    while True: 
            if (len(password)<8): 
                    flag = -1
                    break
            elif not re.search("[a-z]", password): 
                    flag = -1
                    break
            elif not re.search("[A-Z]", password): 
                    flag = -1
                    break
            elif not re.search("[0-9]", password): 
                    flag = -1
                    break
            elif not re.search("[_@$]", password): 
                    flag = -1
                    break
            elif re.search("\s", password): 
                    flag = -1
                    break
            else: 
                    flag = 0
                    break

    if flag ==-1: 
            print("Password Is Week")
    return password


for i in range(1000):
    print("1.Register")
    print("2.Login")
    print("3.Exit")
    try :
        choice=int(input("Please Enter Your Choice-"))
    except:
        print("Enter The Number Value")
    try:
        if(choice==1):
            username=input("Enter User Name-")
            First_Name=input("Enter First Name-")
            Last_Name=input("Enter Last Name-")
            password=getpass("Enter Password-")
            passwords(password)
        
        elif(choice==2):
            username1=input("Enter User Name-")
            password1=getpass("Enter Password-")

            if username1==username and password1==password:
                print(username,"Welcome To Simple Login System")
                print("----------Calculator--------------")   
                for i in range(1000): 
                    print("Select operation.")
                    print("1.Add")
                    print("2.Subtract")
                    print("3.Multiply")
                    print("4.Divide")
                    print("5.Factorial")
                    print("6.Prime")
                    print("7.Palindrome Number")
                    print("8.Palindrome String")
                    print("9.Pangram")
                    print("10.Exit")

                    choice=int(input("Enter Your Choice-"))
                    try:
                        if(choice==1):
                            try:
                                number1=float(input("Enter The 1st Number-"))
                                number2=float(input("Enter The 2nd Number-"))
                                print(number1,'+',number2,'=',add(number1,number2))
                            except:
                                print("Please Do Not Enter String Or Special Charcater")

                        elif(choice==2):
                            try:
                                number1=float(input("Enter The 1st Number-"))
                                number2=float(input("Enter The 2nd Number-"))
                                print(number1,'-',number2,'=',sub(number1,number2))
                            except:
                                print("Please Do Not Enter String Or Special Charcater")

                        elif(choice==3):
                            try:
                                number1=float(input("Enter The 1st Number-"))
                                number2=float(input("Enter The 2nd Number-"))
                                print(number1,'*',number2,'=',multi(number1,number2))
                            except:
                                print("Please Do Not Enter String Or Special Charcater")

                        elif(choice==4):
                            try:
                                number1=float(input("Enter The 1st Number-"))
                                number2=float(input("Enter The 2nd Number-"))
                                print(number1,'/',number2,'=',div(number1,number2))
                            except:
                                print("Please Do Not Enter String Or Special Charcater")

                        elif(choice==5):
                            try:
                                number=int(input("Enter The Number-"))
                                print("Factorial Of",number,"Is-",factorial(number))
                            except:
                                print("Please Do Not Enter String Or Special Charcater")

                        elif(choice==6):
                            try:
                                number=int(input("Enter The Number-"))
                                prime(number)
                            except:
                                print("Please Do Not Enter String Or Special Charcater")

                        elif(choice==7):
                            try:
                                number=int(input("Enter The Number-"))
                                palinum(number)
                            except:
                                print("Please Do Not Enter String Or Special Charcater")

                        elif(choice==8):
                            string=input("Enter The String-")
                            palistr(string) 

                        elif(choice==9):
                            string=set(input("Enter The String-").lower())
                            pangram(string)
                            
                        elif(choice==10):
                            break

                        else:
                            print("Please Enter Valid Input")
                    except:
                        print("Please Do Not Enter String Or Special Charcater")
            else:
                print("Enter Correct Username And Password")

        elif(choice==3):
                break
        else:
            print("Please Enter Valid Input")
    except:
        print("Please First Register Then Trying To Login")

