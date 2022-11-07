mod editor;
mod terminal;
mod tui;

fn main() {
    let lambda = editor::Editor::new();
    let mut screen = terminal::Screen::new().unwrap();
    tui::start(&mut screen, lambda);
}
