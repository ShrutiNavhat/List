# name= ["n","i","t","i","n"]
# b=[]
# # a=len(name)
# i=1
# while i<=len(name):
#     b.append(name[-i])
#     i=i+1
# print(b)
# if b==name:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")




d=int(input("enter the day :"))
m=int(input("enter the month :"))
y=int(input("enter the year :"))
m1=(1,2,3,4,5,6,7,8,9,10,11,12)
if d==29 and m==2:
    print(1,"/",m+1,"/",y)
elif d==30 and m in (4,6,9,11):
    print(1,"/",m+1,"/",y)
elif d==31 and m in (1,3,5,7,8,10):
    print(1,"/",1,"/",y)
elif d==31 and m==12:
    print(1,"/",1,"/",y+1)
elif m not in m1:
    print("error in month")
else:
    print(d+1,"/",m,"/",y)