#입력 내용을 문자열로 넘기는 함수
def enter() :
    map = [list(input()) for _ in range(13)]
    return (map)

map = enter()

#입력형태가 정사각형이 아니라 한줄씩 변환하는 방법밖에 없다고 생각함
#두번째 줄 변환
for i in range(len(map[1])):
    if map[1][i] == "#":
            map[1][i] = "0"
    elif map[1][i] == "O":
            map[1][i] = "1"
    elif map[1][i] == "o":
            map[1][i] = "2"
    elif map[1][i] == "P":
            map[1][i] = "3"
    elif map[1][i] == "=":
            map[1][i] = "4"

#세번째 줄 변환
for i in range(len(map[2])):
    if map[2][i] == "#":
            map[2][i] = "0"
    elif map[2][i] == "O":
            map[2][i] = "1"
    elif map[2][i] == "o":
            map[2][i] = "2"
    elif map[2][i] == "P":
            map[2][i] = "3"
    elif map[2][i] == "=":
            map[2][i] = "4"

#네번째 줄 변환
for i in range(len(map[3])):
    if map[3][i] == "#":
            map[3][i] = "0"
    elif map[3][i] == "O":
            map[3][i] = "1"
    elif map[3][i] == "o":
            map[3][i] = "2"
    elif map[3][i] == "P":
            map[3][i] = "3"
    elif map[3][i] == "=":
            map[3][i] = "4"

#다섯번째 줄 변환
for i in range(len(map[4])):
    if map[4][i] == "#":
            map[4][i] = "0"
    elif map[4][i] == "O":
            map[4][i] = "1"
    elif map[4][i] == "o":
            map[4][i] = "2"
    elif map[4][i] == "P":
            map[4][i] = "3"
    elif map[4][i] == "=":
            map[4][i] = "4"


#일곱번째 줄 변환
for i in range(len(map[6])):
    if map[6][i] == "#":
            map[6][i] = "0"
    elif map[6][i] == "O":
            map[6][i] = "1"
    elif map[6][i] == "o":
            map[6][i] = "2"
    elif map[6][i] == "P":
            map[6][i] = "3"
    elif map[6][i] == "=":
            map[6][i] = "4"

#여덟번째 줄 변환
for i in range(len(map[7])):
    if map[7][i] == "#":
            map[7][i] = "0"
    elif map[7][i] == "O":
            map[7][i] = "1"
    elif map[7][i] == "o":
            map[7][i] = "2"
    elif map[7][i] == "P":
            map[7][i] = "3"
    elif map[7][i] == "=":
            map[7][i] = "4"

#아홉번째 줄 변환
for i in range(len(map[8])):
    if map[8][i] == "#":
            map[8][i] = "0"
    elif map[8][i] == "O":
            map[8][i] = "1"
    elif map[8][i] == "o":
            map[8][i] = "2"
    elif map[8][i] == "P":
            map[8][i] = "3"
    elif map[8][i] == "=":
            map[8][i] = "4"

#열번째 줄 변환
for i in range(len(map[9])):
    if map[9][i] == "#":
            map[9][i] = "0"
    elif map[9][i] == "O":
            map[9][i] = "1"
    elif map[9][i] == "o":
            map[9][i] = "2"
    elif map[9][i] == "P":
            map[9][i] = "3"
    elif map[9][i] == "=":
            map[9][i] = "4"

#열한번째 줄 변환
for i in range(len(map[10])):
    if map[10][i] == "#":
            map[10][i] = "0"
    elif map[10][i] == "O":
            map[10][i] = "1"
    elif map[10][i] == "o":
            map[10][i] = "2"
    elif map[10][i] == "P":
            map[10][i] = "3"
    elif map[10][i] == "=":
            map[10][i] = "4"

#열두번째 줄 변환
for i in range(len(map[11])):
    if map[11][i] == "#":
            map[11][i] = "0"
    elif map[11][i] == "O":
            map[11][i] = "1"
    elif map[11][i] == "o":
            map[11][i] = "2"
    elif map[11][i] == "P":
            map[11][i] = "3"
    elif map[11][i] == "=":
            map[11][i] = "4"

#열세번째 줄 변환
for i in range(len(map[12])):
    if map[12][i] == "#":
            map[12][i] = "0"
    elif map[12][i] == "O":
            map[12][i] = "1"
    elif map[12][i] == "o":
            map[12][i] = "2"
    elif map[12][i] == "P":
            map[12][i] = "3"
    elif map[12][i] == "=":
            map[12][i] = "4"

#Stage1 지도
stage1 = [map[1],map[2],map[3]]

#Stage2 지도
stage2 = [map[6],map[7],map[8],map[9],map[10],map[11],map[12]]

#Stage1 가로크기
n = [len(stage1[0]),len(stage1[1]),len(stage1[2])]
n.sort()
stage1_width = n[2]

#Stage2 가로크기
n = [len(stage2[0]),len(stage2[1]),len(map[2]),len(map[3]),len(stage2[4]),len(stage2[5]),len(stage2[6])]
n.sort()
stage2_width = n[6]

#Stage1 세로크기 /함수로 어떻게 나타내야할지 잘 모르겠음
stage1_high = 3

#Stage2 세로크기
stage2_high = 7

#Stage1 구멍의 수
count1_Hall = 0

for i in range(stage1_high):
    for j in range(stage1_width):
        if stage1[i][j] == "1":
            count1_Hall += 1

#Stage2 구멍의 수
count2_Hall = 0

for i in range(stage2_high):
    for j in range(len(stage2[i])):
        if stage2[i][j] == "1":
            count2_Hall += 1

#Stage1 구멍의 수
count1_Ball = 0

for i in range(stage1_high):
    for j in range(stage1_width):
        if stage1[i][j] == "2":
            count1_Ball += 1

#Stage2 구멍의 수
count2_Ball = 0

for i in range(stage2_high):
    for j in range(len(stage2[i])):
        if stage2[i][j] == "2":
            count2_Ball += 1

#Stage1 플레이어 위치
player1_x = 0
player1_y = 0

for i in range(stage1_high):
    for j in range(stage1_width):
        if stage1[i][j] == "3":
            player1_x = i+1
            player1_y = j+1
            break

#Stage2 플레이어 위치
player2_x = 0
player2_y = 0

for i in range(stage2_high):
    for j in range(len(stage2[i])):
        if stage2[i][j] == "3":
            player2_x = i+1
            player2_y = j+1
            break

#저장값을 기호로 변환

#stage1
for i in range(stage1_high):
    for j in range(stage1_width):
        if stage1[i][j] == "0":
                stage1[i][j] = "#"
        elif stage1[i][j] == "1":
                stage1[i][j] = "O"
        elif stage1[i][j] == "2":
                stage1[i][j] = "o"
        elif stage1[i][j] == "3":
                stage1[i][j] = "P"

#stage2
for i in range(stage2_high):
    for j in range(len(stage2[i])):
        if stage2[i][j] == "0":
                stage2[i][j] = "#"
        elif stage2[i][j] == "1":
                stage2[i][j] = "O"
        elif stage2[i][j] == "2":
                stage2[i][j] = "o"
        elif stage2[i][j] == "3":
                stage2[i][j] = "P"

#리스트 문자열로 변환

#stage1
for i in range(stage1_high):
        stage1[i] = "".join(stage1[i])

#stage2
for i in range(stage2_high):
        stage2[i] = "".join(stage2[i])

#출력
print("Stage 1")
print()
for i in range(stage1_high):
        print(stage1[i])
print()
print("가로크기:", stage1_width)
print("세로크기:", stage1_high)
print("구멍의 수:", count1_Hall)
print("공의 수:", count1_Ball)
print("플레이어 위치 (",player1_x,",",player1_y,")")
print()
print("Stage 2")
print()
for i in range(stage2_high):
        print(stage2[i])
print()
print("가로크기:", stage2_width)
print("세로크기:", stage2_high)
print("구멍의 수:", count2_Hall)
print("공의 수:", count2_Ball)
print("플레이어 위치 (",player2_x,",",player2_y,")")