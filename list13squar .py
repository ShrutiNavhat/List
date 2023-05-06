# a=[9,1,1,9]
# i=0
# b=""
# while i<len(a):
#     b+=str(a[i])
#     print(a[i]*a[i],end="")
#     i=i+1



# i=0
# while i<=6:
#     i=i+1
#     if  i==3:
#         pass
# print(i)


a=["my ","name ","shruti  "]
i=0
count=0
b=[]
while i <len(a):
    # if type(a[i])==str:
    j=0
    sum=""
    while j<len(a[i]):
        if a[i][j]==" ":
            count=count+1
        else:
            sum+=a[i][j]
        j=j+1
    b.append(sum)
    i=i+1
print(b)
print(count)
