import concurrent.futures

def sum_range(start, end):
    return sum(range(start, end))

def parallel_sum(n, workers=4):
    step = n // workers
    ranges = [(i * step, (i + 1) * step) for i in range(workers)]
    ranges[-1] = (ranges[-1][0], n + 1)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(lambda r: sum_range(*r), ranges)

    print(f"Total Sum: {sum(results)}")

if __name__ == "__main__":
    N = 1000000  
    parallel_sum(N, workers=5)
