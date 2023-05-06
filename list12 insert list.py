# a=int(input("enter the number :"))
# b=[]
# i=0
# while i<a:
#     c=int(input("enter the number :"))
#     b.append(c)
#     i=i+1
# print(b)

# x=int(input("enter the number :"))
# a=[]
# i=0
# while i<x:
#     y=input("enter the number : ")
#     a.append(y)
#     i=i+1
# print(a)

a=[2,3,[4,5],6,7]
i=0
sum=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        # sum=sum+a[i][j]
        b.append(a[i][j])
        j=j+1
    i=i+1
print(sum)


# a=[1,2,3,4,5,6,7,8,9,10]
# b=int(input("enter the number :"))
# i=0
# c=[]
# d=[]
# while i<len(a):
#     if a[i]<=b:
#         if a[i]%2==0:
#             c.append(a[i])
#         else:
#             d.append(a[i])
#     i=i+1
# print(c)
# print(d)

# i=249
# while i<259:
#     print(i-248)
#     i=i+1

