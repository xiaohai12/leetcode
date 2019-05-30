num = int(input())
List = [int(x) for x in input().split(' ')]
dic = [10 for i in range(num)]
value = [0 for i in range(num)]
for i in range(1,num):
    j = i-1
    Min = 1000000000
    while j>=0:
        if abs(List[i]-List[j])<=Min:
            dic[i]=j+1
            Min = abs(List[i]-List[j])
        j = j-1
    value[i] = Min

for i in range(1,num):
    print(value[i],dic[i])