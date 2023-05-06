# i=20
# sum=0
# count=0
# while i<=40:
#     count=count+1
#     sum=sum+i
#     print(i)
#     i=i+1
# print("count=",count)
# print("sum=",sum)

# a=[50,40,80,10,20]
# i=0
# sum=0
# count=0
# while i<len(a):
#     sum=sum+a[i]
#     count+=1
#     i=i+1
# print(sum)
# print(count)

# i=20
# a=[]
# b=0
# while i<=40:
#     b=b+1
#     i=i+1
#     print(i)
# print("count=",b)

# a=[2,3,4,5,6]
# i=0
# while i<len(a):
#     if a[i]%2==0:
#         print(a[i],"even number")
#     else:
#         print(a[i],"odd number")
#     i=i+1

# a=["shruti","gaya"]

# a=int(input("enter the number : "))
# i=2
# sum=0
# while i<=a:
#     print(i)
#     sum=sum+i
#     print(sum)
#     sum==a
#     print(1,end="")
#     i=i*2
    

# a=["shruti","gaytri",12,12.3,13+0j,9,10]
# i=0
# b=[]
# while i<len(a):
#     if type (a[i])==int:
#         b.append(a[i])
#     i=i+1
# print(b)




# a=["shruti","gayatri","neha","rani","devyani"]
# i=0
# count=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#        j=j+1
#     print(a[i])
#     print(len(a[i]))
#     k=0
#     while k<len(a[i]):
#         print("*",end="")
#         k=k+1
#     print()
#     i=i+1



# a=[1,2,3,4,5,6,7,8]
# b=[]
# i=0
# c=0
# sum=0
# while i<len(a):
#     sum=a[i]-c
#     b.append(sum)
#     c=c+1
#     i=i+1
# print(b)

# a=[50,40,23,70,56,12,5,10,7]
# i=0
# b=[]
# count=0
# while i<len(a):
#     if a[i]>=20:
#         if a[i]<=40:
#          print(a[i])
#          count=count+1
#     i=i+1
# b.append(count)
# print(b)




# i=10
# while i>=1:
#     print(i)
#     i=i-1



# 

# a=[1,2,3,4,5,6,7,8]
# i=0
# m=1
# sum=0
# while i<len(a):
#     if i<=3:
#         m=m*a[i]
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(m)
# print(sum)

# a=[1,2,3,4,[2,3,4]]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#      j=0
#      while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     i=i+1
# print(sum)

    
A=[4,6,4,3,2]
B=[]
c=[]
i=0
count=0
while i<len(A):
        if A[i] not in B:
            B.append(A[i])
        else:
            c.append(A[i])
        i=i+1
print(B)
print(c)
