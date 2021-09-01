


def truncable(number):
    number=str(number)
    right_side=[number[:i] for i in range(1,len(number)+1)]
    left_side=[number[j:] for j in range(len(number))]
    sag,sol=True,True
    for prime in right_side:
        primes=prime
        prime=int(prime)
        allnum = [p for p in range(2, prime)]
        prime_list = [k for k in allnum if prime % k == 0]
        if prime==1 or ("0" in primes):sag=False
        elif any(prime_list):sag=False
    for prime in left_side:
        primes = prime
        prime=int(prime)
        allnum = [p for p in range(2, prime)]
        prime_list = [k for k in allnum if prime % k == 0]
        if prime == 1 or ("0" in primes):sol = False
        elif any(prime_list):sol=False
    return sag,sol
right,left=truncable(139)
if (right and left):print("both")
elif left:print("left")
elif right:print("right")
else:print(False)













