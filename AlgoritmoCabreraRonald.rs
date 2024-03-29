pub fn prime_factors(n: u64) -> Vec<u64> {
    let mut i = 2;
    let mut n = n;
    let mut factors = Vec::new();
    if n == 0 {
        return factors;
    }
    if n == 1 {
        factors.push(1);
        return factors;
    }
    while i * i <= n {
        if n % i != 0 {
            if i != 2 {
                i += 1;
            }
            i += 1;
        } else {
            n /= i;
            factors.push(i);
        }
    }
    if n > 1 {
        factors.push(n);
    }
    factors
}