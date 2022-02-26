from random import randint

N = 50
A = []
for i in range(N):
  A.append(randint(-99, 99))

pos_sum = neg_sum = i = j = 0

for n in A:
  if n > 0:
    pos_sum += n
    i += 1
  else:
    neg_sum += n
    j += 1

pos_avg = int(pos_sum / i)
neg_avg = int(neg_sum / i)

print(A)
print(f'Positive average: {pos_avg}')
print(f'Negative average: {neg_avg}')