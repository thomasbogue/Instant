import random
import math

N = 10000000

roll_count = [ 0 for x in range(20) ]

for i in range(N):
  roll = random.randint(1,20)
  roll_count[roll - 1] += 1

print(roll_count)

expected = N / 20
std = math.sqrt(N / 20)

z_scores = [ (x - expected)/std for x in roll_count ]
print(z_scores)
