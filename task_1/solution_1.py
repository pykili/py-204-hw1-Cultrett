#1.sorting the list in ascending order and printing the last element:
mylist = [3,5,0,7,9]
mylist.sort()
print("largest element is:", mylist[-1])

#2.using (max):
mylist= [3,5,0,7,9]
print("largest element is:", max(mylist))

#3. (Как надо)
a = input()
b=0
q = len(a)
for i in range (1, q):
  if int(a[i]) > int(b):
    b=a[i]
print(b)
