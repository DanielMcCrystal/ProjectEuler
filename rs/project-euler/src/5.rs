pub fn answer(max: u32) -> u32 {
    let mut factors = Vec::new();
    for mut n in 2..max + 1 {
        for f in &factors {
            if n % f == 0 {
                n /= f;
            }
        }
        if n > 1 {
            factors.push(n);
        }
    }
    return factors.iter().fold(1, |a, b| a * b);
}
