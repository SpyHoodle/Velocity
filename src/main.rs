use std::time::Duration;

mod terminal;
mod editor;

fn main() {
    let lambda = editor::Editor::new();
    let mut term = terminal::Terminal::new().unwrap();
    loop {
        for line in lambda.buffer.data {
            terminal::Terminal::write(format!("{line}"));
            mut term.cursor.move_to(0, 1);
        };
        std::thread::sleep(Duration::from_secs(3));
        break;
    };
    terminal::Terminal::exit();
}
