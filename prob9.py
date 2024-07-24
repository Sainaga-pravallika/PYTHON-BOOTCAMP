find the element present i K+n th element k=3,n=2
ip
3 6 8 4 61 2
op:2



my_list=list(map(int,input().split()))
n=int(input())
k=int(input())

if(len(my_list)!=k+n):
    print("error")
else:
    for i in range(0,len(my_list)):
        print(my_list[k+n])
        break