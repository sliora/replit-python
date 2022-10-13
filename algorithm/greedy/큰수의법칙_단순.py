"""
[큰 수의 법칙]
- 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
- 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
- 첫째 줄에 배열크기 N, 숫자가 더해지는 횟수 M, 최대 연속 수 K를 공백으로 구분하여 입력
- 둘째 줄에 N개의 자연수를 공백으로 입력
- 반복문을 이용한 단순한 방식
"""

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
print(result)
