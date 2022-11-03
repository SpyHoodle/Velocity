use std::time::Duration;

mod terminal;
mod editor;

fn main() {
    let lambda = editor::Editor::new();
    println!("{}", lambda.buffer.data[0]);
    let term = terminal::Terminal::new();
    for _ in [0..1000000000] {
        println!("{:?}", term);
        std::thread::sleep(Duration::from_millis(2000));
    };
    terminal::Terminal::exit()
}
