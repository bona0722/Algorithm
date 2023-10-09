#arr의 idx 자리에다가 num을 넣어라
def insert(idx, num, arr, leng):
    temp = num
    temp2 = 0
    for i in range(len(arr)):
        if i == idx:
            temp = arr[i]
            arr[i] = num
        elif i > idx: 
            temp2 = arr[i]
            arr[i] = temp
            temp = temp2
    arr.append(temp)

    printArr(arr, leng+1)

'''
추가적인 배열을 쓰지 않고 옮기는 법?!
바로 오른쪽부터 옮기는 것!!!
'''
def erase(idx, arr, leng):
    for i in range(len(arr)):
       del arr[idx]
       break
    printArr(arr, leng-1)

'''
추가적인 배열을 쓰지 않고 옮기는 법?!
바로 왼쪽부터 옮기는 것!!!
'''

def printArr(arr,leng):
  print(arr)

def insert_test():
  print("***** insert_test *****\n")
  arr = [10, 20, 30]
  leng = 3
  insert(3, 40, arr, leng) # 10 20 30 40
  insert(1, 50, arr, leng) # 10 50 20 30 40
  insert(0, 15, arr, leng) # 15 10 50 20 30 40


def erase_test():
  print( "***** erase_test *****\n")
  arr = [10, 50, 40, 30, 70, 20]
  leng = 6
  erase(4, arr, leng) #10 50 40 30 20
  erase(1, arr, leng) # 10 40 30 20

def main():
  insert_test()
  erase_test()

if __name__ == "__main__":
    main()