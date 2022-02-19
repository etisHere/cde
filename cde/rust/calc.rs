use std::io::{stdin, stdout, Write};
fn read(input: &mut String) {
    stdout().flush()
        .expect("Failed to flush");
    stdin().read_line(input)
        .expect("Failed to read");
}

fn main() {
    println!("Calculator");
//Taking input
    let mut num1 = String::new();
    let mut num2 = String::new();
    let mut operator = String::new();

    println!("First num?: ");
    read(&mut num1);
    println!("Num2?: ");
    read(&mut num2);
    println!("Operator?: ");
    read(&mut operator);

    let num1: f32 = num1.trim().parse().unwrap();
    let num2: f32 = num2.trim().parse().unwrap();
    let operator: char = operator.trim().chars().next().unwrap();
//Seting the operator    
    let operators = String::from("+-*/");
    
//Checking the Operator and if not in string it will print unknown 
    if !operators.contains(operator){
        println!("Unknown Operator");
        return;
    }

    let result = match operator {
        '+' => num1 + num2,
        '-' => num1 - num2,
        '*' => num1 * num2,
        '/' => num1 / num2,
        _ => panic!("Error in operator!")
    };

    println!("The result of {} {} {} = {}", num1, operator, num2, result);

}



