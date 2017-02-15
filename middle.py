def middle(a,b,c):
	if a > b:
		if b > c:
			return b
		else:
			if a > c:
				return c
			else:
				return a
	else:
		if c > a:
			if c > b:
				return b
			else:
				return c
		else:
			return a

print middle(100,111,103)
