pub fn answer(mut n: i64) -> i64 {
    let mut divisor = 2;
    while n > 1 {
        if n % divisor == 0 {
            n /= divisor;
        } else {
            divisor += 1;
        }
    }
    return divisor;
}
