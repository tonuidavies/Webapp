def calcSum(arg):
	multiples = []
	x = 0
	while x < arg:
		if x % 3 == 0 and x % 5 == 0:
			multiples.append(x)
		x += 1
	return sum(multiples)

# print(calcSum(50))


def swapZeros(arg):
	org_list = arg[:]
	temp_list = []
	for key, value in enumerate(org_list):
		if value is 0:
			zero = org_list.pop(key)
			temp_list.append(zero)
	# temp_list.extend(org_list)
	return temp_list


def move_zeros(array):
    original_array = array[:]
    num_items_moved = 0

    for index, item in enumerate(original_array):
        try:
            if int(item) == 0 and not (item is False):
                value = int(array.pop(index - num_items_moved))
                array.append(value)
                num_items_moved += 1
        except Exception as exception:
            continue

    return array

alist = [0, 4, 0, 3]

# swapZeros(alist)
# print(alist)
# print(move_zeros(alist))

def palindrome(n):
	step = 0
	isNotPalindrome = True
	while isNotPalindrome:
		alist = list(str(n))
		alist.reverse()
		alist = "".join(alist)
		num = int(alist)
		if num == n:
			isNotPalindrome = False
			break;
		else:
			step += 1
			n = n + num
			
			# return palindrome(n)
	return step

def palindrome_chain_length(n):
# parameter n is a positive integer
# your function should return the number of steps
	t=0
	while str(n)!=str(n)[::-1]:
		n+=int(str(n)[::-1])
		t+=1
	return t

# print(palindrome_chain_length(87))

def validate(n):
	length = len(list(str(n)))
	if length > 16:
		return False

	alist = list(str(n))
	if length % 2 == 0:
		# even
		for x in range(0, len(alist), 2):
			alist[x] = intval(alist[x]) * 2

		for x in range(len(alist)):
			if alist[x] > 9:
				alist[x] = intval(alist[x]) - 9

		sum_digits = sum(alist)

		if sum_digits % 10 == 0:
			return True
		else:
			return False
	else:
		# odd
		for x in range(1, len(alist), 2):
			alist[x] = alist[x] * 2

		for x in range(len(alist)):
			if alist[x] > 9:
				alist[x] = intval(alist[x]) - 9

		sum_digits = sum(alist)

		if sum_digits % 10 == 0:
			return True
		else:
			return False

# print(validate(891))
# add = lambda x,y:x+y
# print add(2, 3) 

# list = ["1", "4", "0", "6", "9"]
# list = [int(i) for i in list]
# list.sort()
# print (list)

# def c_to_f(c_temp):
#   f_temp = c_temp*(9/5)+32
#   return f_temp
#   c0_in_fahrenheit = c_to_f(0)
# c_to_f(0)

def missing_number(A):
	n = len(A)
	total = (n+1)*(n+2)/2
	sum_digits = sum(A)
	return total-sum_digits
miss_digit = [1,2,3,4,5,6,7,8,9,10]
# print missing_number(miss_digit)

def remove_duplicates(t):
	return set(t)
	sort(t)
t = ['1', '1', '2', '2','3','3']
# print remove_duplicates(t)

def remove(duplicates):
	final_list=[]
	for x in duplicates:
		if x not in final_list:
			final_list.append(x)

	return final_list

t = ['1', '1', '2', '2','3','3']
# print remove(t)
# Python prog to illustrate the following in a list 
def find_len(list1): 
    length = len(list1) 
    list1.sort() 
    print("Largest element is:", list1[length-1]) 
    print("Smallest element is:", list1[0]) 
    print("Second Largest element is:", list1[length-2]) 
    print("Second Smallest element is:", list1[1]) 
  
# Driver Code 
# list1=[12, 45, 2, 41, 31, 10, 8, 6, 4] 
# Largest = find_len(list1)   
#   
def find_largest(list1):
	length = len(list1)
	list1.sort()
	print (list1[length-1])
	print (list1[0])


# list1=[12, 45, 2, 41, 31, 10, 8, 6, 4] 
# print (find_largest(list1))

# Python3 implementation of simple method 
# to find count of pairs with given sum. 

# Returns number of pairs in arr[0..n-1] 
# with sum equal to 'sum' 
def getPairsCount(arr, n, sum): 
	
	count = 0 # Initialize result 

	# Consider all possible pairs 
	# and check their sums 
	for i in range(0, n): 
		for j in range(i + 1, n): 
			if arr[i] + arr[j] == sum: 
				count += 1
	
	return count 

# Driver function 
arr = [1, 5, 7, -1, 5] 
n = len(arr) 
sum = 6
print("Count of pairs is", 
	getPairsCount(arr, n, sum)) 

# This code is contributed by Smitha Dinesh Semwal 
def sort_array(num):
    num.sort()
    return (num)
num = ['5','4','3', '2', '1']
print(sort_array(num))


#FiZZBuZZ

for i in range(50):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        continue
    elif i % 3 == 0:
        print("fizz")
        continue
    elif i % 5 == 0:
        print("buzz")
        continue
    print(i)



def F(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
	   return F(n-1) + F(n-2)
print (F(10))


def reverse_list(num):
    num.reversed()
    return (num)
num = ['5','4','3', '2', '1']
print(sort_array(num))

#count the number capital letters 

# count sum(1 for line in fh for character in line if character.isupper())

from random import shuffle
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)
print(x)


# Calculate percentile

# import numpy as np
# a = np.array([1,2,3,4,5])
# p = np.percentile(a, 50)  #Returns 50th percentile, e.g. median
# print(p)


# Fibonacci
def F(n):
    if n < 2: return n
    else: return F(n-1)+F(n-2)
print (F(9))

# Fibonacci series:
# the sum of two elements defines the next
# Function for nth Fibonacci number 

def Fibonacci(n): 
	if n<0: 
		print("Incorrect input") 
	# First Fibonacci number is 0 
	elif n==0: 
		return 0
	# Second Fibonacci number is 1 
	elif n==1: 
		return 1
	else: 
		return Fibonacci(n-1)+Fibonacci(n-2) 

# Driver Program 

print(Fibonacci(9)) 

#This code is contributed by Saket Modi 

# for index, fibonacci_number in zip(range(10), fib()):
#      print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))