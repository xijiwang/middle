import my_library
import random
my_list = my_library.random_list(random.randint(10,50),-100,100)
l = len(my_list)
checking = 0
checker = 1
temp = 0
while checking < l:
	while checker < l:
		if my_list[checking] > my_list[checker]:
			temp = my_list[checker]
			my_list[checker] = my_list[checking]
			my_list[checking] = temp
		print checker
		checker = checker + 1
	checking = checking + 1
	checker = checking + 1



print my_list

