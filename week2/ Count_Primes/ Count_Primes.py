class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 1 or n == 0:
            return 0
        prime = [1]*n
        prime[0] = 0
        prime[1] = 0
        first_prime = 2
        while first_prime < n:
            find_not_prime = first_prime
            if prime[find_not_prime] == 1:
                find_not_prime += first_prime
                while find_not_prime < n:
                    prime[find_not_prime] = 0
                    find_not_prime += first_prime
            first_prime += 1
        return sum(prime)