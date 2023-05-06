# a=[1,2,3,[4,5,6]]
# i=0
# b=[]
# while i<len(a):
#     if type(a)==list:
#         print(a[i])

#         b.append(a[i])
#     j=0
#     while j<3:
#         if type(a[i])==list:
#           b.append(a[i][j])
#         j=j+1
#         else:

#     i=i+1
# print(b)



# a=[1,2,3,[4,5,6]]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             b.append(a[i][j])
#             j=j+1
#     else:
#         b.append(a[i])
#     i=i+1
# print(b)



# a=[1,2,3,4,5]
# b=[2,3,4,5,6]
# i=0
# sum=0
# c=[]
# d=0
# while i<len(a):
#     d=a[i]+b[i]
#     sum=d
#     c.append(sum)
#     i=i+1
# print(c)





# a=[1,2,3,[4,5,6]]
# i=0
# b=[]
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while i<len(a[i]):
#             sum=sum+a[i][j]
#             j=j+1
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum)
# b.append(sum)
# print(b)

# a=["shruti","dhanu","vaishu"]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==str:
#         j=0
#         while j<len(a[i]):
#             if "a" in a[i][j]:
#                 print(a[i])
#                 b.append(a[i])
#             j=j+1
#     i=i+1
# print(b)



# a=["shruti","shraddha","dhanu","soham"]
# i=0
# b=[]
# while i<len(a):
#     if type(a)==str:
#      j=0
#      while j<len(a[i]):
#         if "s" in a[i][j]:
#             print(a[i])
#             b.append(a[i])
#         else:
#             print("s not in a")
#         j=j+1
#     i=i+1
# print(b)



# a=[1,2,3,4,5,6,7,8]
# i=0
# sum=1
# b=[]
# while i<len(a):
#     sum=sum+a[i]
#     b.append(sum)
#     sum=sum+a[i]
#     i=i+1
# print(b)
 

# a=[[1,2,3],[3,4,5],[7,9,8]]
# i=0
# c=[]
# b=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             if a[i][j]>b:
#                 b=a[i][j]
#             j=j+1
#         c.append(b)
#     i=i+1
# print(c)


# a=[1,-2,3,-4,5,-6,-7,-8]
# i=0
# b=[]
# while i<len(a):
#     if a[i]<0:
#         b.append(0)
#     else:
#         b.append(a[i])
#     i=i+1
# print(b)    

# a=[-8,-9,-10,-11,-13,-15]
# i=0
# c=[]
# b=a[i]
# while i<len(a):
#     if a[i]>b:
#         b=a[i]
#     i=i+1
# print(b)


# a=["shruti","grecy","divya"]
# i=0
# b=[]
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



# a=[1,2,3,4,5,6,7,8]
# i=0
# b=0
# c=[]
# while i<len(a):
#     print(a[i:b])
#     c.append(a[i:b])
#     b=b+2
#     i=i+2
# print(c)


# a=[1,2,2,3,4,5]
# b=[2,4,8,9,10,12]
# i=0
# v=0
# c=[]
# while i<len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i=i+1
# print(c)
