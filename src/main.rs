mod terminal;
mod editor;

fn main() {
    let lambda = editor::Editor::new();
    println!("{}", lambda.buffer.data[0]);
    let term = terminal::Terminal::new();
    println!("{:?}", term);
    terminal::Terminal::exit();
}
