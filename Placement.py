##print(" 1.factorial problem ")
##print("using for loop find factorial problem")
##fact=1
##num=int(input("enter the number :"))
##for i in range(1,num+1):
##    fact*=i
##print(fact)
##
##print("using while loop find factorial problem")
##fact=1
##num=int(input("enter the number :"))
##while(num>0):
##    fact*=num
##    num-=1
##print(fact)    
##
##
####print("2.fibonacci series")
##num=10
##a,b=0,1
##for i in range(num):
##    print(a,end=" ")
##    a,b=b,a+b
####    

##print(" 3.LCM")
##num1=int(input("enter the number 1 :"))
##num2=int(input("enter the number 2 :"))
##import math
##print(math.lcm(num1,num2))
##
##print(" 4.GCD")
##num1=int(input("enter the number 1 :"))
##num2=int(input("enter the number 2 :"))
##import math
##print(math.gcd(num1,num2))



##print("5.Factors of Given Number")
##num=int(input("enter the number :"))
##for i in range(1,num+1):
##    if num%i==0:
##        print(i)


##print(" 6.Whether the given number is prime or not")
##num=int(input("enter the number: "))
##if num < 2:
##    print("not prime number..")
##else:
##    for i in range(2,num):
##        if num%i == 0:
##            print(num," is not prime number..")
##            break
##    else:
##        print(num," is prime number")

##print("7.Finding the range of prime number (1-10 -> 2, 3, 5, 7)")
##num=int(input("enter the number: "))
##if num < 2:
##    print()
##else:
##    for i in range(2,num+1):
##        for j in range(2,i):
##            if i%j == 0:
##                break         
##        else:
##            print(i,end=" ")


##print("8.sum of consecutive prime(Prime numbers next-next varradhu)")
##num=int(input("enter the number:"))
##sum=0
##for i in range(2,num+1):
##    for j in range(2,i):
##        if i%j ==0:
##            break
##    else:
##        sum += i
##        print(i)
##print(sum)    

##print(" 9.Find the co prime..(no common factors other than 1.)")
##num1=int(input("enter the number 1 :"))
##num2=int(input("enter the number 2 :"))
##gcd=1
##m=min(num1,num2)
##for i in range(1,m+1):
##    if num1%i==0 and num2%i==0:
##        gcd=i
##        
##if gcd==1:
##    print(num1,num2 ,"its co-prime")
##else:
##    print("not prime")


##print("10.Find the next immediate prime of the given number")
##num=int(input("enter the number:"))
##np = num+1
##while True:
##    for i in range(2,np):
##        if np%i==0:
##            break
##    else:
##        print("next immediate prime number",np)
##        break
##    np+=1    
        

##print(" 11.Find the previous prime of the given number")
##num=int(input("enter the number:"))
##pp=num-1
##while True:
##    for i in range(2,pp):
##        if pp%i==0:
##            break
##        
##    else:
##        print("previous prime number",pp)
##        break
##    pp-=1

##print("12.Prime Factorization")
##num = int(input("Enter a number: "))
##i=2
##while num>1:
##    if num % i==0:
##        print(i,end=" ")
##        num=num//i
##    else:
##        i+=1



###### Reverse a String Using Recursion
####def reverse(s):
####    if len(s) == 0:
####        return s
####    else:
####        return reverse(s[1:]) + s[0]
####  
####def palin(s):
####    if s == reverse(s):
####        return "palindrome"
####    else:
####        return "not palindrome"
####print(palin("ana"))


####sum the list
##def recursive_sum(lst):
##    if len(lst) == 0:       
##        return 0
##    else:
##        return lst[0] + recursive_sum(lst[1:])   
##print(recursive_sum([1, 2, 3, 4, 5]))  

#### max number find the without sort method
def maxn(l):
    if len(l) == 1:
        return l[0]
    else:
        max_v = maxn(l[1:])
        if l[0] < max_v:
            return l[0]
        else:
            return max_v
print(maxn([3, 5, 2, 9, 1]))






        













