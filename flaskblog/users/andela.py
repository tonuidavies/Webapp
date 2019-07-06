def Sorting(lst): 
    lst2 = sorted(lst, key=len, reverse=True) 
    print (lst2)
states = ["Abia", "Adamawa", "Anambra", "Akwa Ibom", "Bauchi", "Bayelsa", "Benue", "Borno", "Cross River", "Delta", "Ebonyi", "Enugu", "Edo", "Ekiti", "Gombe", "Imo", "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun", "Oyo", "Plateau", "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara"]
Sorting(states)


# getMissingNo takes list as argument 
def getMissingNo(A): 
    n = len(A) 
    total = (n+1)*(n+2)/2
    sum_of_A = sum(A) 
    return total - sum_of_A 
  
# Driver program to test above function 
A = [1, 2, 4, 5, 6] 
miss = getMissingNo(A) 
print(miss) 
# This code is contributed by Pratik Chhajer 


# Python program to print  
# duplicates from a list  
# of integers 
def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated 
  
# Driver Code 
list1 = [10, 20, 30, 20, 20, 30, 40,  
         50, -20, 60, 60, -20, -20] 
print (Repeat(list1)) 
      



      # Python program to find largest, smallest, 
# second largest and second smallest in a 
# list with complexity O(n) 
def Range(list1): 
	largest = list1[0] 
	lowest = list1[0] 
	largest2 = None
	lowest2 = None
	for item in list1[1:]:	 
		if item > largest: 
			largest2 = largest 
			largest = item 
		elif largest2 == None or largest2 < item: 
			largest2 = item 
		if item < lowest: 
			lowest2 = lowest 
			lowest = item 
		elif lowest2 == None or lowest2 > item: 
			lowest2 = item 
			
	print("Largest element is:", largest) 
	print("Smallest element is:", lowest) 
	print("Second Largest element is:", largest2) 
	print("Second Smallest element is:", lowest2) 


# Driver Code 
list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4] 
Range(list1) 
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
def sot(l):
	return set(l)
t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
print sot(t)



#Quicksort

# Python program for implementation of Quicksort Sort 

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
	i = ( low-1 )		 # index of smaller element 
	pivot = arr[high]	 # pivot 

	for j in range(low , high): 

		# If current element is smaller than or 
		# equal to pivot 
		if arr[j] <= pivot: 
		
			# increment index of smaller element 
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 
def quickSort(arr,low,high): 
	if low < high: 

		# pi is partitioning index, arr[p] is now 
		# at right place 
		pi = partition(arr,low,high) 

		# Separately sort elements before 
		# partition and after partition 
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
	print ("%d" %arr[i]), 

# This code is contributed by Mohit Kumra 


for num in range(1,21):
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)


txt = "Hello World"[::-1]
print(txt)