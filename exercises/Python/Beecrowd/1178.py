x = float(input())
n = [0] * 100
i = 1

n[0] = x
print("N[{}] = {:.4f}".format(0, n[0]))
while i < 100:
	x = x / 2
	n[i] = x
	print("N[{}] = {:.4f}".format(i, n[i]))
	i += 1