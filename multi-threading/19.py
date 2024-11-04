# Create 2 threads where one thread will print odd numbers and another will print even numbers. 

import threading

n = 10

def even_num():
    for i in range(0, n+1, 2):
        print(f"Even: {i}")

def odd_num():
    for i in range(1, n+1, 2):
        print(f"Odd: {i}")

even = threading.Thread(target=even_num)
odd = threading.Thread(target=odd_num)

even.start()
odd.start()

even.join()
odd.join()

print("Finish")