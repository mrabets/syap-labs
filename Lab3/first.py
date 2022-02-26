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

pos_avg = abs(int(pos_sum / i))
neg_avg = abs(int(neg_sum / i))

if pos_avg > neg_avg:
  print(f'Positive average is greater')
elif  pos_avg < neg_avg:
  print(f'Negative average is greater')
else:
  print(f'Negative and postitive averages are equal')