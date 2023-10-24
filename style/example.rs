let odd_square_sum: i32 = (0..100)
    .filter(|num| num % 2 == 1)
    .map(|num| num * num)
    .sum();