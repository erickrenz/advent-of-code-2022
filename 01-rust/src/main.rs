use aoc::*;
use color_eyre::Result;
use itertools::Itertools;

fn main() -> Result<()> {
    setup_debug_tools()?;

    let max = include_str!("input.txt")
        .lines()
        .map(|v| v.parse::<u64>().ok())
        .batching(|it| {
            let mut sum = None;
            while let Some(Some(v)) = it.next() {
                sum = Some(sum.unwrap_or(0) + v);
            }
            sum
        })
        .max()
        .unwrap_or_default();
    println!("Part 1 = {max:?}");

    let answer = include_str!("input.txt")
        .lines()
        .map(|v| v.parse::<u64>().ok())
        .coalesce(|a, b| match (a, b) {
            (None, None) => Ok(None),
            (None, Some(b)) => Ok(Some(b)),
            (Some(a), Some(b)) => Ok(Some(a + b)),
            (Some(a), None) => Err((Some(a), None)),
        })
        .flatten()
        .sorted_by_key(|&v| std::cmp::Reverse(v))
        .take(3)
        .sum::<u64>();
    println!("Part 2 = {answer:?}");

    let answer = include_str!("input.txt")
        .lines()
        .map(|v| v.parse::<u64>().ok())
        .batching(|it| it.map_while(|x| x).sum1::<u64>())
        .map(std::cmp::Reverse)
        .k_smallest(3)
        .map(|x| x.0)
        .sum::<u64>();
    println!("Part 2 = {answer:?}");

    Ok(())
}
