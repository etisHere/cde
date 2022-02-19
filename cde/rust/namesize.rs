use std::io::{stdin, stdout, Write};
 
fn read(input: &mut String) {
     stdout().flush()
         .expect("Failed to flush");
    stdin().read_line(input)
        .expect("Failed to read");
}

fn main() {
    let mut name = String::new();
    println!("Your name?:");
    read(&mut name);
    let size = get_length(&name);
    println!("is {} characters big(+ the 0)", size);
}

fn get_length(s: &str) -> usize {
    s.chars().count()
}
