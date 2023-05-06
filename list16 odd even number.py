# a=[23,14,56,12,19,9,15,25,31,42,43]
# i=0
# sum=0
# sum1=0
# count=0
# count1=0
# avg=0
# avg1=0
# while i<len(a):
#     if a[i]%2==0:
#         print(a[i],"even number")
#         sum+=a[i]
#         count+=1
#         avg=sum/count
#     else:
#         print(a[i],"odd number")
#         sum1+=a[i]
#         count1+=1
#         avg1=sum1/count1
#     i=i+1
# print(sum,"sum of even number")
# print(count,"count of even number")
# print(avg,"avg of even number")
# print(sum1,"sum of odd number")
# print(count1,"count of odd number")
# print(avg1,"avg og odd number")


# a=[1,3,8,10,7,15,18,20,19,17]
# b=[]
# c=[]
# i=0
# while i<len(a):
#     if a[i]%2==0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i=i+1
# print(b,"(even number )")
# print(c,"(odd number)")



a=["shruti","gayatri","neha"]
i=0
b=[]
c=[]
while i<len(a):
    j=0
    while j<1:
        print(len(a[i]))
        if len(a[i])%2==0:
            print(a[i],"(even number)")
            b.append(a[i])
        else:
            print(a[i],"(odd number)t")
            c.append(a[i])
        j=j+1
    i=i+1
print(b)
print(c)
