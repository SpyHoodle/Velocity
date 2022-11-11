mod core;
mod terminal;
mod tui;
use std::env;

fn main() {
    // Collect cli arguments
    let args: Vec<String> = env::args().collect();

    let file_path = if args.len() > 1 {
        // Collect the file path
        &args[1]
    } else {
        ""
    };

    

    let lambda = core::editor::Editor::new(file_path);
    let mut screen = terminal::screen::Screen::new().unwrap();
    tui::ui::start(&mut screen, lambda);
}
