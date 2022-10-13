"""
[거스름돈]
- 카운터에 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전히 무한히 존재
- 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하라
- 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.
"""

n = int(input())
count = 0
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin
print(count)
