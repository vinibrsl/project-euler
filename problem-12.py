def divisors_count(n):
  count = 0
  for i in range(1, n+1):
    if (n % i) == 0:
      count += 1
  return count

def triangulate(n):
  y = [int(x) for x in list(str(n))]
  return sum(y)

triangle = 1
while divisors_count(triangle) <= 500:
  triangle += triangulate(triangle)

print(triangle)
