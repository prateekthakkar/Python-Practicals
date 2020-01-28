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
        for i in range(2,number//2):
            if (number % 2) == 0:
                print("number is not prime")
                break
        else:
            print("number is prime")
    else:
        print("number is not prime")
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

def fibonacci(number):
    number1,number2=0,1
    counter=0
    if number <= 0:
        print("Please Enter Positive Number")
    while(counter<number):
        print(number1)
        number3=number1+number2
        number1 = number2
        number2 = number3
        counter += 1


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
    print("10.Fibonacci")
    print("11.Exit")

    choice=int(input("Enter Your Choice-"))
    if(choice==1):
        number1=float(input("Enter The 1st Number-"))
        number2=float(input("Enter The 2nd Number-"))
        print(number1,'+',number2,'=',add(number1,number2))

    elif(choice==2):
        number1=float(input("Enter The 1st Number-"))
        number2=float(input("Enter The 2nd Number-"))
        print(number1,'-',number2,'=',sub(number1,number2))

    elif(choice==3):
        number1=float(input("Enter The 1st Number-"))
        number2=float(input("Enter The 2nd Number-"))
        print(number1,'*',number2,'=',multi(number1,number2))

    elif(choice==4):
        number1=float(input("Enter The 1st Number-"))
        number2=float(input("Enter The 2nd Number-"))
        print(number1,'/',number2,'=',div(number1,number2))

    elif(choice==5):
        number=int(input("Enter The Number-"))
        print("Factorial Of",number,"Is-",factorial(number))

    elif(choice==6):
        number=int(input("Enter The Number-"))
        prime(number)

    elif(choice==7):
        number=int(input("Enter The Number-"))
        palinum(number)

    elif(choice==8):
        string=input("Enter The String-")
        palistr(string) 

    elif(choice==9):
        string=set(input("Enter The String-").lower())
        pangram(string)
    
    elif(choice==10):
        number=int(input("Enter The Number-"))
        fibonacci(number)

    elif(choice==11):
        exit()

    else:
        print("Please Enter Valid Input")
    
