def primer(prime):
    allnum=[p for p in range(2,prime)]
    prime_list=[k for k in allnum if prime%k==0]
    if any(prime_list):pass
    else:return prime
print(list(filter(primer,range(2,101))))