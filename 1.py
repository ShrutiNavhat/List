# a=[1,2,3,[2,3,4],4,[1,2,3],[2,4]]
# i=0
# sum=0
# count=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if type(a[i])==list:



# i=10
# while i>=1:
#     print(i)
#     i=i-1



# i=1
# sum=0
# while i<=10:
#     sum=sum+i
#     print(i)
#     i=i+2
# print(sum)


# a=int(input("enter the number:"))
# i=0
# while a>0:
#     i=(i*10)+a%10
#     a=a//10
# print("reverse=",i)

# i=0
# a=int(input("enter the number:"))
# x=a
# while a>0:
#    i=(i*10)+a%10
#    a=a//10
#    print(i*10) 





# a=[1,2,3,4,5,6,7,8,10]
# b=int(input("enter the number :"))
# i=0
# sum=0
# c=[]
# d=[]
# while i<len(a):
#     if b<=a[i]:
#         c.append(a[i])
#         sum=sum+a[i]
#     i=i+1
# d.append(sum)
# print(d)
# print(c)




# a=[1,2,9,8,3,4,7,6]
# i=0
# b=[]
# max=0
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     max+=1
#     i=i+1
# print(max)



a=[1,2,[3,4],5]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j])
        j+=1
i+=1    