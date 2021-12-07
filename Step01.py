#입력 내용을 문자열로 넘기는 함수
def enter() :
    map = [list(input()) for _ in range(13)]
    return (map)

map = enter()

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

print(map)

