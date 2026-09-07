def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        # else runs only if the for loop completes without hitting break
        return True
    return False

N = int(input("Enter N: "))
primes = [str(i) for i in range(2, N + 1) if is_prime(i)]
print(*primes)


