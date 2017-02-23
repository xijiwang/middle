import random
n = 1
my_list = []
while n < 6:
	my_list.append(random.randint(1,100))
	n = n + 1

# while n < 101:
# 	my_list.append(random.randint(1,100))
# 	n = n + 1
print my_list
target = 0
num_compared = 1
c = 5

temp = 0
while target < 5:
	while num_compared < c:
		if my_list[target] < my_list[num_compared]:
			temp = my_list[num_compared]
			my_list[num_compared] = my_list[target]
			my_list[target] = temp
		print target , " " , num_compared

		num_compared = num_compared + 1
	
	target = target + 1				
	num_compared = target + 1
	 			


print my_list
