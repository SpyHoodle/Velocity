use std::time::Duration;

mod terminal;
mod editor;

fn main() {
    let lambda = editor::Editor::new();
    let _term = terminal::Terminal::new();
    loop {
        print!("{esc}[2J{esc}[1;1H", esc = 27 as char);
        for line in lambda.buffer.data {
            terminal::Terminal::write(format!("{line}"));
        };
        std::thread::sleep(Duration::from_millis(3000));
        break;
    };
    terminal::Terminal::exit()
}
