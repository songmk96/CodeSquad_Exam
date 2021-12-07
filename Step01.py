#입력 내용을 문자열로 넘기는 함수
def enter() :
    map = [input() for _ in range(13)]
    return (map)

print(enter())