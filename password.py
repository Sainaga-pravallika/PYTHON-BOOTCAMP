password verifier
mr x trying to create password
conditions:
1 min len-8,max len-15
2 only@,/ is alloved in password
3 nospaces are alloved
4 alpha ,numerics  alloved
5 u are supposed to print week if len-==8
*mediam len(8-12)
*strong len(12-15)



p=input("create password\n")
if(len(p)<8):
    print("please follow the condition")
elif(len(p)==8):
    print("weak password")
elif(len(p)>=8 and (p)<12):
    print("medium range password")
elif(len(p)>=12 and (p)<=15):
    print("strong password")
count=0
str[0]=="@"
str[1]=="/"
for(i in str[0] or i in str[1] and i !=" " ):
    count+=1
    break

