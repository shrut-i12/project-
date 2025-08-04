import re
n, m = map(int, input().split())
matrix = [input().ljust(m) for _ in range(n)]

text = ''.join(matrix[row][col] for col in range(m) for row in range(n))

print(re.sub(r'(?<=\w)[^a-zA-Z0-9]+(?=\w)', ' ', text))
