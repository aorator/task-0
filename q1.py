n = int(input())
numbers = list(map(int, input().split()))

if n > 0:
    largest = numbers[0]
    smallest = numbers[0]
    totalSum = 0
    evenCount = 0
    oddCount = 0

    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

        totalSum += num

        if num % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1

    reversedList = []
    for i in range(n - 1, -1, -1):
        reversedList.append(str(numbers[i]))

    print(f"Largest: {largest}")
    print(f"Smallest: {smallest}")
    print(f"Sum: {totalSum}")
    print(f"Even count: {evenCount}")
    print(f"Odd count: {oddCount}")
    print(f"Reversed: {' '.join(reversedList)}")