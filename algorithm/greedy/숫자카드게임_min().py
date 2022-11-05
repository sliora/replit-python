"""
[숫자카드게임]
- 숫자 카드 게임은 여러 개의 숫자 ㅏ드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
- 단 게임의 룰을 지켜서 뽑아야 함
- N X M 형태로 놓인 카드로 N은 행의 개수 M은 열의 개수
- 먼저 뽑고자 하는 카드가 포함 되어 있는 행을 선택
- 그다음 선택된 해엥 포함된 카드들 중 가장 숫자가 낮은 카드 뽑음
- 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 함
"""

n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)
