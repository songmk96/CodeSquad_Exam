#Stage 2 출력
stage2 = ["  #######","###  O  ###","#    o    #","# Oo P oO #","###  o  ###"," #   O  # "," ########"]
print("Stage 2")
print()
for i in range(len(stage2)):
    print(stage2[i])
print()

stage2_high = 7 #스테이지 세로크기
player = [0,0]     #player[0] => y좌표, player[1] => x좌표

#문자열을 리스트로 변환하는 함수 (문자열은 문자 하나의 값에 접근할 수는 있지만 변경할 수 없기 때문)
def con():
    for i in range(stage2_high):
        stage2[i] = list(stage2[i])

con()

#스테이지를 문자열로 바꿔서 출력하는 함수
def pt():    #print줄임말
    for i in range(stage2_high):
        stage2[i] = "".join(stage2[i])
    for i in range(stage2_high):
        print(stage2[i])
    print()    

#플레이어 위치 찾는 함수
def find():
        
    for i in range(stage2_high):
        for j in range(len(stage2[i])):
            if stage2[i][j] == "P":
                player[0] = i
                player[1] = j
                break

find()

#입력값 받기(q받아서 프로그램 종료될까지)
while True:
    print("SOKOBAN>",end=" ")
    move = list(input())
    print()

#입력값 실행하기
    for i in range(len(move)):

        con()   #문자열 리스트로 변환 (pt)
        find()  #플레이어 위치 찾기: player[0] => y좌표, player[1] => x좌표

        if move[i] == "q":
            print("Bye~")
            exit()

        elif move[i] == "w":
            if stage2[player[0]-1][player[1]] == " ":
                stage2[player[0]][player[1]] = " "
                stage2[player[0]-1][player[1]] = "P"
                pt()
                print(move[i].upper(),": 위쪽으로 이동합니다.")
                
                
            else:
                pt()
                print(move[i].upper(),": (경고!) 해당 명령을 수행할 수 없습니다!")   

        elif move[i] == "a":
            if stage2[player[0]][player[1]-1] == " ":
                stage2[player[0]][player[1]] = " "
                stage2[player[0]][player[1]-1] = "P"
                pt()
                print(move[i].upper(),": 왼쪽으로 이동합니다.")
                
                
            else:
                pt()
                print(move[i].upper(),": (경고!) 해당 명령을 수행할 수 없습니다!")               

        elif move[i] == "s":
            if stage2[player[0]+1][player[1]] == " ":
                stage2[player[0]][player[1]] = " "
                stage2[player[0]+1][player[1]] = "P"
                pt()
                print(move[i].upper(),": 아래쪽으로 이동합니다.")
                
                
            else:
                pt()
                print(move[i].upper(),": (경고!) 해당 명령을 수행할 수 없습니다!")    

        elif move[i] == "d":
            if stage2[player[0]][player[1]+1] == " ":
                stage2[player[0]][player[1]] = " "
                stage2[player[0]][player[1]+1] = "P"
                pt()
                print(move[i].upper(),": 오른쪽으로 이동합니다.")
                
                
            else:
                pt()
                print(move[i].upper(),": (경고!) 해당 명령을 수행할 수 없습니다!")
        
        else:
            print(move[i].upper(),": (경고!) 해당 명령을 수행할 수 없습니다!")
    



