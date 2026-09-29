import time

print("AutoDev Index Test Started")

items = ["apple", "banana", "orange"]

for i in range(len(items)):
    print(f"Reading index: {i}")
    time.sleep(1)

    print(items[i])

print("Processing completed")
