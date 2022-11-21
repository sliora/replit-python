# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행한다.
# 단 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다
# N과 K가 주어질 때 N이 1이 될 때까지 총 최소 횟수를 구하라


n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k  # //: 몫 구하기
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k  ## n = n // k  = 5
    print()

result += (n - 1)
print(result)
