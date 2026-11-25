import time

now = time.monotonic()

while True:
    check_time = input("t to check time")
    if check_time == "t":
        print(now)
    if check_time == "e":
        break
    print(time.monotonic)

