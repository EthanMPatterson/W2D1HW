def prime_100():
    for x in range(2, 100 + 1):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            print(f"The prime numbers are : ", x)
print("Prime Numbers between 1 - 100 are")
prime_100()            