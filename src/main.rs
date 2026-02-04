use std::{fs::read_to_string, str::FromStr};

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

#[derive(Debug)]
enum Turn {
    Left(i32),
    Right(i32),
}

impl FromStr for Turn {
    type Err = String;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        if s.is_empty() {
            return Err("Empty string".to_string());
        }

        let dir = s.chars().next().unwrap();
        let amount: i32 = s[1..].parse().expect("Could not convert step to int.");

        match dir {
            'R' => Ok(Turn::Right(amount)),
            'L' => Ok(Turn::Left(amount)),
            _ => Err(format!("Invalid direction: {}", dir)),
        }
    }
}

fn part1() {
    let filename = "data/day01.txt";
    let lines = read_lines(&filename);

    let mut dial = 50;
    let mut counter = 0;

    for line in lines {
        let turn: Turn = line.trim().parse().unwrap();

        match turn {
            Turn::Left(steps) => dial = (dial - steps).rem_euclid(100),
            Turn::Right(steps) => dial = (dial + steps) % 100,
        }

        if dial == 0 {
            counter += 1
        };
    }

    println!("Part 1: {}", counter)
}

fn part2() {
    let filename = "data/day01.txt";
    let lines = read_lines(&filename);

    let mut dial: i32 = 50;
    let mut counter: i32 = 0;

    for line in lines {
        let turn: Turn = line.trim().parse().unwrap();

        let (dir, mut amount) = match turn {
            Turn::Left(amt) => (-1, amt),
            Turn::Right(amt) => (1, amt),
        };

        while amount > 0 {
            dial = (dial + dir).rem_euclid(100);
            if dial == 0 {
                counter += 1;
            }
            amount -= 1;
        }
    }

    println!("Part 2: {}", counter)
}

fn main() {
    part1();
    part2();
}
