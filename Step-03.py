import sys

sys.stdin = open('map.txt')

for i in range(39):
    print(sys.stdin.readline())