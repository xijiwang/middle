import random
def random_list(num,min,max):
	n = 1
	my_list = []
	while n < num + 1:
		my_list.append(random.randint(min,max))
		n = n + 1
	return my_list

def my_sort(unsorted_list):

	target = 0
	num_compared = 1
	l = len(unsorted_list)
	sorted_list = []
	temp = 0
	while target < l:
		while num_compared < l:
			if unsorted_list[target] < unsorted_list[num_compared]:
				temp = unsorted_list[num_compared]
				unsorted_list[num_compared] = unsorted_list[target]
				unsorted_list[target] = temp

			num_compared = num_compared + 1
		
		target = target + 1				
		num_compared = target + 1
	return unsorted_list

test_list = my_sort(random_list(100,0,100))
print test_list







