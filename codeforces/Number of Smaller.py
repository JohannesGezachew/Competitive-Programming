x,y = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

count_list = []
count = 0

left = 0
right = 0
    
while right< y:
        if left< x and  arr1[left] <arr2[right]:
            left+=1
            count +=1
            
        else:
              count_list.append(count)
              count = left
              right += 1

    
print(*count_list)

