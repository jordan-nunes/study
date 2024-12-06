x = int(input())
i = 6

if(x % 2 != 0):
	while i > 0:
		print(x)
		x += 2
		i -= 1
else:
	x+=1
	while i > 0:
		print(x)
		x += 2
		i -= 1