x=int(input("enter the number :"))
a="shruti"
b=[]
j=x
i=0
while i<len(a):
    if a[i] not in b:
        c=a[i]
        b.append(c)
        b.append(j)
        j=j+x
    i=i+1
print(b)


# a=int(input("enter the number :"))
# i=1
# b=[]
# while i<=a:
#     j=1
#     c=[]
#     while j<=10:
#         e=i*j
#         c.append(e)
#         # c.append(b)
#         j=j+1
#     b.append(c)
#     i=i+1
# print(b)


# a=[1,2,0,7,0,8,6,0]
# i=0
# b=[]
# while i<len(a):
#     if a[i]==0:
#         print("1")
#         b.append(a)
#     i=i+1
# print(b)

