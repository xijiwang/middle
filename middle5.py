def middle(a,b,c,d,e):
	
	count = 0
	if a > b:
		count = count + 1
	if a > c:
		count = count + 1
	if a > d:
		count = count + 1
	if a > e:
		count = count + 1
	if count == 2:
		return a

	count = 0
	if b > a:
		count = count + 1
	if b > c:
		count = count + 1
	if b > d:
		count = count + 1
	if b > e:
		count = count + 1
	if count == 2:
		return b

	count = 0
	if c > b:
		count = count + 1
	if c > a:
		count = count + 1
	if c > d:
		count = count + 1
	if c > e:
		count = count + 1
	if count == 2:
		return c

	count = 0
	if d > b:
		count = count + 1
	if d > c:
		count = count + 1
	if d > a:
		count = count + 1
	if d > e:
		count = count + 1
	if count == 2:
		return d

	count = 0
	if e > b:
		count = count + 1
	if e > c:
		count = count + 1
	if e > d:
		count = count + 1
	if e > a:
		count = count + 1
	if count == 2:
		return e


print middle(7,1,8,4,17)
print middle(7,1,50,4,17)
print middle(7,12,8,34,17)
print middle(5,100,81,54,17)
print middle(711,1452,876,4123,147)




