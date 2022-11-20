initialNum = list(map(int,input()))
if(len(initialNum) == 1): # 한 자리 숫자만 입력하면
    initialNum.insert(0, 0) # 0번째 index에 숫자 0 추가

count = 1 # 비교 수 리스트 생성할 때 한번 계산하기 때문에 count 값을 1로 설정
compareNum = [initialNum[1], sum(initialNum) % 10]

while(compareNum != initialNum):
    compareSum = sum(compareNum) # 아래 식에서 compareNum[0] 값이 변하기 때문에 sum() 값을 미리 선언 해야 함
    compareNum[0] = compareNum[1]
    compareNum[1] = compareSum % 10
    count += 1

print(count)