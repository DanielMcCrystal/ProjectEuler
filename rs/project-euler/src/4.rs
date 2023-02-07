fn is_palindrome(mut n: u32) -> bool {
    let mut digits = Vec::new();
    while n > 0 {
        digits.push(n % 10);
        n /= 10;
    }
    for i in 0..digits.len() / 2 {
        if digits[i] != digits[digits.len() - i - 1] {
            return false;
        }
    }
    return true;
}

pub fn answer(n_digits: u32) -> u32 {
    let base: u32 = 10;
    let max = base.pow(n_digits) - 1;

    let mut a = max;
    let mut b;
    let mut i = 0;
    let mut prod;
    while a > 0 {
        for pass in 0..1 {
            a = max - i;
            b = max - i - pass;
            for _ in 0..i + 1 {
                prod = a * b;
                if is_palindrome(prod) {
                    return prod;
                }
                a += 1;
                b -= 1;
            }
        }
        i += 1;
    }
    return 0;
}
