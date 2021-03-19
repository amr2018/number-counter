
numbers = [9080 , 500 , 10]

def count_numbers(n):

	count = 0
	numbers_count = {}

	for full_num in n:
		for part_of_num in str(full_num):
			count += 1
		numbers_count[full_num] = count
		count = 0

	print(numbers_count)



count_numbers(numbers)
