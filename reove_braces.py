remove all the () from the exp..


p="HellO123(){}[])"
a=p.replace("(){}[])","")
print(a)






p="HellO123()} {["
a=0
for i in p:
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
        pass
    else:
        print(i,end="")
print()