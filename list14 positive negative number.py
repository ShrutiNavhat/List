# a=[2,-7,5,-64,-14]
# i=0
# count=0
# count1=0
# while i<len(a):
#     if a[i]>0:
#         print(a[i],"positive number")
#         count=count+1
#     else:
#         print(a[i],"negative number")
#         count1+=1
#     i=i+1
# print(count,"count of positive number")
# print(count1,"count of negative number")
# a=[1,-2,3,-4,5,-6,7,-8]
# i=0
# b=[]
# while i<len(a):
#     if a[i]<0:
#         b.append(a[i])
#     i=i+1
# print(b)


a=["shruti","dhanu","grecy","aapi","biri"]
i=0
b=[]
while i<len(a):
    if type(a[i])==str:
        j=1
        sum=""
        while j<=len(a[i]):
            sum=sum+a[i][-j]
            j=j+1
        b.append(sum)
    i=i+1
print(b)
