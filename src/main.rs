mod core;
mod terminal;

fn main() {
    let lambda = core::editor::Editor::new();
    let mut screen = terminal::screen::Screen::new().unwrap();
    terminal::tui::start(&mut screen, lambda);
}
