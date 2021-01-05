x=int(input())
num=0
num_count=0

while num_count<x:
    num+=1
    num_count+=num
num_count-=num

if num%2==0:
    i=x-num_count
    j=num-(x-num_count)+1
else:
    i=num-(x-num_count)+1
    j=x-num_count
print('{}/{}'.format(i,j))
