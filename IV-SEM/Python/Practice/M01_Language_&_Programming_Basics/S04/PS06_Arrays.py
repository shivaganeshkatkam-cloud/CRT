'''
Arrays:
1.List ==> bulit -in data structure
    2. list is mutable,heterogenous,indexed,ordered and allows dupicate values
2.Arrays using array module
3.array using numpay module

li=[1,"shiva",3,3+4]
print(li,type(li))
#no.of elements in list len()
print(len(li))
#update
li[2]=5
print(li)
#adding element in list
li.append(34)
print(li)
# insert 
li.insert(2,"ganesh")
print(li)
li.insert(28,73)
print(li)
li.extend([23,5443,97])#extend will add the element in last or end of the list
print(li)
#Remove element from the list
li.pop(4)
print(li)
#li.pop(48)
#print(li)
#li.remove(5333333)
#print(li)
li.clear()
print(li)

#copy()
l1=[1,3,4,5]
l2=l1
l3=l1.copy()
'''
from array import array
ara=array('f',[1.98,23.85,834.098])
print(ara,type(ara))
ara.append(23)
