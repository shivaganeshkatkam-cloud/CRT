'''
1) find Largest number(using max())
2) Check palindrome(using reversed() and join()functions)
3) Count even numbers (using filter())
4) Remove duplicates(using set())
5) Sum of digits(using sum())
6) sort word alphabetically (using sorted())
7) Find common elements (using set())
8) Index with value (using enumerate())
9) pair two list (using zip())
10) find the second largest number (using sorted())
'''
#1
ar=[10,23,43,54,65]
print(max(ar))
#2
word="madam"
if word=="".join(reversed(word)):
    print("palindrome")
else:
    print("not a palidrome")
#3
arr=[2,4,5,6,34,76]
res=list(filter(lambda x:x%2==0,arr))
print(arr)
#4
ass=[1,2,3,4,2,3,4,3,1,4,]
print(ass.set())
#5
auu=[1,2,3,4,5,6,7]
print(sum(auu))
#6
asr=['q','r','a','b']
print(asr.sorted())
#7
arr1=[1,23,4,5,6,7,8]
arr2=[2.45,3,3,4,3,6,8,9,3,5,7]
a=set(arr1)
b=set(arr2)
print(a.intersection(b))
#8

