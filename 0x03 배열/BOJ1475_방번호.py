# https://www.acmicpc.net/problem/1475

def roomNum(n):
  maxN = 0
  # 0부터 9까지
  num = [0] * 10
  for i in n:
    num[i] += 1
    
  for i in range(len(num)):
    if i == 6 or i == 9: continue
    if num[i] > maxN:
      maxN = num[i]
      
  #idx = 6, 9 값을 제외한 값을 maxN에 넣어주고 이후에 비교해준다.
  #홀수용 +1
  maxN = max(maxN,int(((num[6] + num[9] + 1) / 2)))
  return maxN
    
N = list(input())
for i in range(len(N)):
  N[i] = int(N[i])
print(roomNum(N))

'''
1, 2, 3, 4, 5, 6, 7, 8, 9 < 한 세트
6과 9는 서로 뒤집어서 이용 가능

다솜이의 방 번호를 보고 세트에서 -1함
0이 되면 다른 세트를 들고 온다.
만약 6이나 9면 세트에 여분이 남아있는지 확인

N <= 1,000,000 2초
세트 개수 출력
'''
