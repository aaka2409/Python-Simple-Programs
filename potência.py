n = int(input())
total = 0
for i in range(n):
	num = input()
	total += int(num[0:-1:+1]) ** int(num[-1])
print(total)