def a_number_of_alphabet(S):
  wordArr = [0] * 26
  
  for i in S:
    wordArr[ord(i)-97] += 1 
    #문자를 아스키 코드 숫자로 변환
  
  for i in wordArr:
    print(i, end = ' ')
    
S = input()
a_number_of_alphabet(S)