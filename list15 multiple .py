# a=[6,1,3,5,6,3,1]
# b=[]
# m=1
# i=0
# while i<len(a):
#     if a[i] not in b:
#        b.append(a[i])
#        m*=b[i]
#     i=i+1
# print(b)
# print(m)

# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# m=1
# b=[]
# sum=0
# while i<len(a):
#     if a[i]<=a[4]:
#         m*=a[i]
#     if a[i]>=a[5]:
#         sum=sum+a[i]
#     i=i+1
# print(m)
# print(sum)
        
# a=int(input("enter the number :"))
# c=input("enter the word :")
# i=0
# b=[]
# while i<=1:
#     i=i+1
# print(a*c)
# b.append(a*c)
# print(b)


# a=[1,2,3,3,4,4,5]
# i=0
# b=[]
# while i<len(a):
#     count=0
#     j=0
#     while j<len(a):
#         if a[i]==a[j]:
#             count+=1
#         j=j+1
#     if count==1:
#         b.append(a[i])
#     i=i+1
# print(b)

    
# x=1
# i=1
# while i<=4:
#     j=1
#     while j<=5-i:
#         print(" ",end=" ")
#         j=j+1
#     b=1
#     while b<=x:
#         print("*",end=" ")
#         b=b+1
#     x=x+2
#     print()
#     i=i+1


# def fun(n):
#     shared=5
#     cumulative=0
#     for i in range(1,n+1):
#         liked=shared//2
#         cumulative+=liked
#         shared=liked*3
#     print(cumulative)
# n=int(input("enter the number : "))
# fun(n)
    

# a=[1,22,3,14,6,17,8,9,10]
# i=0
# c=0
# c1=0
# while i<len(a):
#     if a[i]%2==0:
#         c=c+1
#         p=c/10*100
#     else:
#         c1=c1+1
#         p1=c1/10*100
#     i=i+1
# print(p,"%")
# print(p1,"%")



        
a=15
b="14"
b=int(b)
c="mehak"
d="5+6j"
e=7.5
f=15
print(a+b+c+d+e)

