def factorial_mod_m(n, m):
    result = 1
    for i in range(1, n+1):
        result = (result * i) % m
    return result

def nCr_mod_m(n, r, m):
    n_fact = factorial_mod_m(n, m)
    r_fact = factorial_mod_m(r, m)
    n_r_fact = factorial_mod_m(n-r, m)
    return (n_fact // (r_fact * n_r_fact)) % m

# Test cases
n = int(input())
r = int(input())
m = int(input())
print(float(nCr_mod_m(n, r, m)))
