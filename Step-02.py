#Stage 2 출력
stage2 = ["  #######","###  O  ###","#    o    #","# Oo P oO #","###  o  ###"," #   O  # "," ########"]
print("Stage 2")
print()
for i in range(len(stage2)):
    print(stage2[i])
print()

#입력값 받기
print("SOKOBAN>",end=" ")
#x = input()

#문자열을 리스트로 변환 (문자열은 문자 하나의 값에 접근할 수는 있지만 변경할 수 없기 때문)
for i in range(len(stage2)):
    stage2[i] = list(stage2[i])

print(stage2)