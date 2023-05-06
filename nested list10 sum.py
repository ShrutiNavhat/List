# a=[[1,2,3],[2,3,4]]
# b=[]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if type(a[i])==list:
#             sum=sum+a[i][j]
#             b.append(sum)
#         j=j+1
#     i=i+1
# print(sum)
# print(b)





# a=[1,2,3,[2,3,4],4,[1,2,3],[2,4]]
# i=0
# sum=0
# b=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j=j+1
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum)
# b.append(sum)
# print(b)
        
# # a=[1,0,1,0,6,0,9,4]
# # i=0
# # b=[]
# # while i<len(a):
# #     if a[i]>=1:
# #         b.append(a[i])
# #     else:
# #         b.append("*")
# #     i=i+1
# # print(b)




a=[1,2,3,4,5]
b=[4,5,6,7,8]
i=0
sum=0
while i <len(a):
    j=0
    while j<len(b):
        j=j+1
    i=i+1
sum=a[i]+b[j]
print(sum)

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print('*',end='')
#         j=j+1 
#     print()
#     i=i+1


# a=[1,"vaishu",2,"abc",2.1,3,"harshu",1.1]
# i=0
# b=[]
# c=[]
# sum=0
# while i<len(a):
#     if type(a[i])==float:
#         print(a[i])
#         b.append(a[i])
#     i=i+1
# print(b)


# a=[1,"vaishu",2,"abc",2.1,3,"harshu",1.1]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==int:
#         print(a[i])
#         b.append(a[i])
#     i=i+1
# print(b)

# a=[1,"vaishu",2,"abc",2.1,3,"harshu",1.1]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==str:
#         print(a[i])
#         b.append(a[i])
#     i=i+1
# print(b)
        

# a=[1,3,2,8,79,69,56]
# i=0
# b=[]
# c=0
# while i<len(a):
#     if a[i]>c:
#         c=a[i]
#         if c<a[i]:
#             print(a[i])
#     i=i+1

# b.append(c)
# print(b)

# a=input("enter the word : ")
# i=0
# b=[]
# c=[]
# d=[]
# count=0
# count1=0
# count2=0
# while i<len(a):
#     count=count+1
#     b.append(a[i])
#     if a[i]=="a"or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u":
#        c.append(a[i])
#        count1=count1+1
#     else:
#        count2=count2+1
#        d.append(a[i])
#     i=i+1
# print(b,count,"count")
# print(c,count1,"count","it is vowel")
# print(d,count2,"count","it is consonants")


a=["shruti","vaishu"]
i=0
b=[]
while i<len(a):
    str=a[i]
    sum=""
    j=1
    while j<len(a[i])+1:
        sum+=a[i][-j]
        j=j+1
    b.append(sum)
    i=i+1
print(b)

# a=["mom","dad","sister"]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     str=a[i]
#     sum=""
#     j=1
#     while j<len(a[i])+1:
#         sum+=a[i][-j]
#         j=j+1
#     b.append(sum)
#     i=i+1
# print(b)
# if b==a:
#     print("it is palindrome number")
#     # c.append)


# else:
#     print("it is not palidrome number ")


# a=["shruti"]


# i=1
# while i<=5:
#     b=1
#     while b<=1-i:
#         print("    ",end="")
#         b=b+1
#     j=1
#     while j<=b-i:
#         print(i,end="")
#         j=j+1
#     print()
#     i=i+1
