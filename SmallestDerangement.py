# Python3 program to generate 
# smallest derangement
# using priority queue.
def generate_derangement(N) :
	
	# Generate Sequence and insert
	# into a priority queue.
	S = [i for i in range(N + 1)] 
	PQ = [] 
	for i in range(1, N + 1) :	 
		PQ.append(S[i])
		
	# Generate Least Derangement
	D = [0] * (N + 1) 
	PQ.sort() 
	for i in range(1, N + 1) :	 
		PQ.sort()	 
		d = PQ[0]
		del PQ[0]	 
		if (d != S[i]) or (i == N) :		 
			D[i] = d		 
		else :		 
			PQ.sort()
			D[i] = PQ[0]
			del PQ[0]
			PQ.append(d)		 
	if D[N] == S[N] :	 
		t = D[N - 1]
		D[N - 1] = D[N]
		D[N] = t
		
	# Print Derangement
	for i in range(1, N + 1) :
		print(D[i], end = " ")	 
	print()
	
generate_derangement(10)
