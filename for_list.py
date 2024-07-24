#you are given with a space suparated list 
#find no.of even 
#and odd elements in list




my_list=list(map(int,input().split(",")))
count_even=0
count_odd=0
for i in range(0,len(my_list)):
    if(my_list[i]%2==0):
        count_even+=1
    else:
        count_odd+=1
print(count_even,count_odd)

        
    #op:248
    #   135