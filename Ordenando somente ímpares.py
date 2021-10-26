n = int(input())
nums = [int(x) for x in input().split()]
impares = []
for i in nums:
	if i % 2 != 0:
		impares.append(i)
impares.sort()
for j in nums:
	if j % 2 == 0:
		impares.append(j)
for z in impares:
	print(z, end=" ")