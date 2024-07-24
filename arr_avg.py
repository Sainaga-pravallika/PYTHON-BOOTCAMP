replace the elements in an array with avg 
of max and min elements



my_list=list(map(int,input().split()))
num=my_list[0]
 nu=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]<num):
        num=my_list[i]
    if(my_list[i]>nu):
        nu=my_list[i]
print(nu,num)
avg=(num+nu)/2
print(avg)
    
op:
