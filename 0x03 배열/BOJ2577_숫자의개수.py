nums = [0] * 10
A = int(input()) 
B = int(input())
C = int(input())
result = str(A * B * C)
#숫자를 string으로 변환해서 아스키코드로 변환
for i in result:
  nums[ord(i)-48] += 1
  
for j in nums:
  print(j, end='\n')
