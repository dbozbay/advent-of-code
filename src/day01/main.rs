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
        let steps: i32 = s[1..].parse().expect("Could not convert step to int.");

        match dir {
            'R' => Ok(Turn::Right(steps)),
            'L' => Ok(Turn::Left(steps)),
            _ => Err(format!("Invalid direction: {}", dir)),
        }
    }
}

fn main() {
    let filename = "data/day01.txt";
    let lines = read_lines(&filename);

    let mut dial = 50;
    let mut result = 0;

    for line in lines {
        let turn: Turn = line.trim().parse().unwrap();

        match turn {
            Turn::Right(steps) => dial += steps,
            Turn::Left(steps) => dial -= steps,
        }

        dial = dial.rem_euclid(100);

        if dial == 0 {
            result += 1
        };
    }

    println!("Result: {}", result)
}
