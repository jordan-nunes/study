def maximo(x, y, z):
	if x > y and x > z:
		return(x)
	elif y > z and y > x:
		return(y)
	else: 
		return(z)

maximo(-1, 0, 1)