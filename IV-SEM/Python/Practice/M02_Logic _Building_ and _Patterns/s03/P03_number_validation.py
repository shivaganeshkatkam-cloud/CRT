'''
1) writr a python code for the factorial of a number?

n=int(input())
factorial=1
for i in range(1,n+1):
    factorial*=i
print(factorial)
'''
'''
2) write a python code to check whether a number is armstrong or not?
n=int(input())
order=len(str(n))
su=0
temp=n
while temp>0:
    digit=temp%10
    su+=digit**order
    temp//=10
if su==n:
    print("Armstrong")
else: 
    print("Not Armstrong")
'''
''' 3) write a python code to check whether a number is prime or not?
n=int(input())
if n>1:     
    for i in range(2,n):
        if n%i==0:
            print("Not Prime")
            break
    else:

        print("Prime")
       
arr=list(map(int,input().split()))
intc=True
dec=True
for i in range(lng(arr)-1):
    if arr[i]<arr[i+1]:
        dec=False
    if arr[i]>arr[i+1]:
        intc=False
if intc:
    print("Increasing")
elif dec:
    print("Decreasing")
     
#write a code to reverse a integer number?
n=int(input())
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)

#roman to integer
def roman_to_integer(s):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0

    for char in reversed(s):
        value = roman_numerals[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total
roman_num=input()
print(roman_to_integer(roman_num))
'''
#happy numbers
def is_happy_number(n):
    def get_next(number):
        total_sum = 0
        while number > 0:
            digit = number % 10
            total_sum += digit ** 2
            number //= 10
        return total_sum

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1
num = int(input())
if is_happy_number(num):
    print(f"{num} is a happy number.")
else:
    print(f"{num} is not a happy number.")
    