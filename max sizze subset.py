def maximizeSubset(N, arr, M, x=0):

	# Base Case
	if (x == M):
		return 0

	# Stores maximum size of valid subset
	ans = 0

	# Traverse the given array
	for i in range(x, M):

		# If N % arr[i] = 0, include arr[i]
		# in a subset and recursively call
		# for the remaining array integers
		if (N % arr[i] == 0):
			ans = max(
				ans, maximizeSubset(
					N // arr[i], arr,
					M, x + 1)
				+ 1)

	# Return Answer
	return ans


# Driver Code
N = 64
arr = [1, 2, 4, 8, 16, 32]
M = len(arr)

print(maximizeSubset(N, arr, M))
