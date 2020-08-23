```
# Sequence types in python - We can retrieve elements using indices
# a. mutable sequence types - List,tuple etc
# b. immutable sequence types - string,range,byte etc

# membership operator - in
str1 = "I like python"
s1 = {2,3,4,5,6}
t1 = (1,2,3,4)
l1 = [1,2,10,200,100]
d1 = {'1':"guru",
      '2':"alex",
      '3':"fred"
      }

print("Membership operator in python - in")
print("String - str1 = {}".format(str1))
print('"python" in str1 - {}'.format("python" in str1))
print()

print("Set - s1 = {}".format(s1))
print('2 in s1 - {}'.format(2 in s1))
print()

print("Tuple - t1 = {}".format(t1))
print('2 in t1 - {}'.format(2 in t1))
print()


print("List - l1 = {}".format(l1))
print('2 in l1 - {}'.format(2 in l1))
print()

print("Dict - d1 = {}".format(d1))
print('2 in d1 - {}'.format(2 in d1))
print()

# Retrieve elements of list
l1 = [1,2,3,4]
print("Displaying element in list")
for l in l1:
    print(l)
print("Fetching number of elements in a list {}".format(len(l1)))
print("Maximum element is collection {}".format(max(l1)))
print("Minimum element is collection {}".format(min(l1)))

# print("adding string to number list will make the list non comparable")
# l1.append("python")
# print("{}".format(max(l1)))
# TypeError: '>' not supported between instances of 'str' and 'int'

from decimal import Decimal
l1.append(Decimal(100))
print("Maximum element is collection {}".format(max(l1)))
print("Minimum element is collection {}".format(min(l1)))

#Concatination
l1 = [1,2,3,4]
l2 = [5,6,7,8]
l = l1+l2
print(l)

#Repitation
l = [[0,0]]
a =  l * 2
print("Repitation of mutable object - does shallow copy")
print("Displaying list l {}- ".format(l))
print("Displaying list which is created using repitation {}-".format(a))

print(id(l[0]) ==id(a[0]))
print(id(l[0]) ==id(a[1]))

Output
Membership operator in python - in
String - str1 = I like python
"python" in str1 - True

Set - s1 = {2, 3, 4, 5, 6}
2 in s1 - True

Tuple - t1 = (1, 2, 3, 4)
2 in t1 - True

List - l1 = [1, 2, 10, 200, 100]
2 in l1 - True

Dict - d1 = {'1': 'guru', '2': 'alex', '3': 'fred'}
2 in d1 - False

Displaying element in list
1
2
3
4
Fetching number of elements in a list 4
Maximum element is collection 4
Minimum element is collection 1
Maximum element is collection 100
Minimum element is collection 1
[1, 2, 3, 4, 5, 6, 7, 8]
Repitation of mutable object - does shallow copy
Displaying list l [[0, 0]]- 
Displaying list which is created using repitation [[0, 0], [0, 0]]-
True
True

```
