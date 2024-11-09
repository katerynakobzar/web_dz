import concurrent.futures
import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def find_primes_single_thread(start, end):
    return [n for n in range(start, end + 1) if is_prime(n)]

def find_primes_multi_thread(start, end):
    mid = (start + end) // 2
    with concurrent.futures.ThreadPoolExecutor() as executor:
        part1 = executor.submit(find_primes_single_thread, start, mid)
        part2 = executor.submit(find_primes_single_thread, mid + 1, end)
        return part1.result() + part2.result()
start, end = 10, 10000

# Один потік
start_time = time.time()
primes_single = find_primes_single_thread(start, end)
single_thread_time = time.time() - start_time

# Багатопоточність
start_time = time.time()
primes_multi = find_primes_multi_thread(start, end)
multi_thread_time = time.time() - start_time

# Перевірка результатів
assert primes_single == primes_multi, "Результати не збігаються!"

print(f"Час виконання однопотокового пошуку: {single_thread_time:.4f} секунд")
print(f"Час виконання багатопотокового пошуку: {multi_thread_time:.4f} секунд")