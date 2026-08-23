# Abhishek_jadhav_69137
# Assignment_9

import requests
import time
from concurrent.futures import ThreadPoolExecutor


urls = [
    "https://jsonplaceholder.typicode.com/users/1",
    "https://jsonplaceholder.typicode.com/users/2",
    "https://jsonplaceholder.typicode.com/users/3",
    "https://jsonplaceholder.typicode.com/users/4",
    "https://jsonplaceholder.typicode.com/users/5",
    "https://jsonplaceholder.typicode.com/users/6",
    "https://jsonplaceholder.typicode.com/users/7",
    "https://jsonplaceholder.typicode.com/users/8",
    "https://jsonplaceholder.typicode.com/users/9",
    "https://jsonplaceholder.typicode.com/users/10"
]


def fetch_url(url):
    response = requests.get(url)

    print(url, response.status_code)


print("===== SEQUENTIAL APPROACH =====")

start = time.time()

for url in urls:
    fetch_url(url)

sequential_time = time.time() - start

print(f"Sequential Time: {sequential_time:.2f} seconds")


print("\n===== MULTITHREADED APPROACH =====")

start = time.time()

with ThreadPoolExecutor() as executor:
    executor.map(fetch_url, urls)

multithreaded_time = time.time() - start

print(f"Multithreaded Time: {multithreaded_time:.2f} seconds")


print("\n===== TIME COMPARISON =====")

print(f"Sequential Time: {sequential_time:.2f} seconds")
print(f"Multithreaded Time: {multithreaded_time:.2f} seconds")