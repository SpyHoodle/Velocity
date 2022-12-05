mod core;
mod terminal;
mod tui;
use std::{env, path::PathBuf};

fn main() {
    // Collect command line arguments
    let args: Vec<String> = env::args().collect();

    // Collect the file path
    let file_path = if args.len() > 1 { PathBuf::from(&args[1]) } else { PathBuf::from("") };

    // Collect the file name
    let file_name = file_path.clone();
    let file_name = if args.len() > 1 { file_name.file_name().unwrap().to_str().unwrap() } else { "" };

    // Initalise a new editor
    let velocity = core::editor::Editor::new(file_path, file_name);

    // Initalise a screen
    let mut screen = terminal::screen::Screen::new().unwrap();

    // Begin lambda
    tui::ui::start(&mut screen, velocity);
}
