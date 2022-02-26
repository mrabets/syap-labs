from random import randint

N = 10

A = []

for i in range(N):
    A.append([0]*N)

for i in range(N):
    for j in range(N):
        A[i][j] = randint(0, 9)

for i in range(N):
    for j in range(N):
        print(A[i][j], end = ' ')
    print()  

max_num = A[0][0]
index = 0

for i in range(N):
	if A[i][i] > max_num:
		max_num = A[i][i]
		index = i

amount = 0
for i in range(N):
	if A[i][index] > max_num:
		amount += 1

print(f'Max number of main diagonal: {max_num}') 
print(f'Index: {index}')
print(f'Amount: {amount}')     
