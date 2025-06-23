import math

def estimate_pi(n):
    """Estimate pi using Ramanujan's formula with n terms."""
    total = 0
    for k in range(n):
        num = math.factorial(4*k) * (1103 + 26390*k)
        den = (math.factorial(k)**4) * (396**(4*k))
        total += num / den
        factor = (2 * math.sqrt(2)) / 9801
        pi_estimate = 1 / (factor * total)
        return pi_estimate
        if abs(pi_estimate - math.pi) < 0.00001:
            break 
    return pi_estimate

estimate_pi(1)

print(estimate_pi(5))






