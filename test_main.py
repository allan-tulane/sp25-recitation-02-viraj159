from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(1, 2, 2) == 1 # Base case
	assert simple_work_calc(50, 2, 3) == 110
	assert simple_work_calc(15, 5, 3) == 65
	

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(16, 2, 2, lambda n: n // 2) == 32
	assert work_calc(25, 4, 5, lambda n: n * 2) == 122
	assert work_calc(12, 3, 3, lambda n: n + 1) == 46
	

def test_compare_work():
	# Create different work functions based on f(n) = n^c for different values of c
	work_fn1 = lambda n: work_calc(n, 2, 2, lambda n: n**0.5)  # c < log_2(2) = 1
	work_fn2 = lambda n: work_calc(n, 2, 2, lambda n: n**1.5)  # c > log_2(2) = 1
	work_fn3 = lambda n: work_calc(n, 2, 2, lambda n: n)       # c = log_2(2) = 1

	# Compare results for different values of n
	res = compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000])

	# Print results to observe trends
	print("n\tW(n) for c < log_b(a)\tW(n) for c > log_b(a)\tW(n) for c = log_b(a)")
	for row in res:
		print(f"{row[0]}\t{row[1]}\t{row[2]}\t{work_fn3(row[0])}")
	
	
def test_compare_span():
	# Define different span functions with different f(n)
	span_fn1 = lambda n: span_calc(n, 2, 2, lambda n: 1)  # f(n) = 1 -> O(log n)
	span_fn2 = lambda n: span_calc(n, 2, 2, lambda n: n)  # f(n) = n -> O(n)

	# Compare the spans for different values of n
	res = compare_span(span_fn1, span_fn2)
