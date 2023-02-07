pub fn answer(max: i32) -> i32 {
    let mut sum = 0;
    let (mut a, mut b) = (1, 2);
    while b < max {
        if b % 2 == 0 {
            sum += b;
        }
        let next_val = a + b;
        a = b;
        b = next_val;
    }
    sum
}
