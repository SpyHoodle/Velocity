mod core;
mod terminal;
mod tui;
use std::{env, path::PathBuf};

fn main() {
    // Collect command line arguments
    let args: Vec<String> = env::args().collect();

    // Collect the file path
    let current_dir = env::current_dir().unwrap();
    let file_path = if args.len() > 1 { PathBuf::from(&args[1]) } else { current_dir.to_path_buf() };

    // Collect the file name
    let file_name = file_path.clone();
    let file_name = if args.len() > 1 { file_name.file_name().unwrap().to_str().unwrap() } else { "" };

    // Collect the directory path
    let dir_path = file_path.parent().unwrap().to_path_buf();

    // Create a new editor
    let lambda = core::editor::Editor::new(dir_path, file_name);

    // Initalise a screen
    let mut screen = terminal::screen::Screen::new().unwrap();

    // Begin lambda
    tui::ui::start(&mut screen, lambda);
}
