mod core;
mod terminal;
mod tui;

fn main() {
    let lambda = core::editor::Editor::new();
    let mut screen = terminal::screen::Screen::new().unwrap();
    tui::ui::Ui::run(&mut screen, lambda);
}
