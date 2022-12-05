use crate::core::editor::Editor;
use crate::core::buffer::BufferKind;
use crate::terminal::screen::Screen;
use crate::tui::components;
use crossterm::event::{read, Event, KeyCode, KeyEvent, KeyModifiers};

pub fn start(screen: &mut Screen, editor: Editor) {
    // Main screen loop, runs until the program exits
    loop {
        // Refresh the screen
        screen.refresh().unwrap();

        // Draw the welcome message only if it is a scratch buffer
        if editor.buffer.kind == BufferKind::Scratch {
            components::welcome::draw(screen, &editor);
        };

        // Draw the status bar
        components::statusbar::draw(screen, &editor).unwrap();

        // Check for any key presses
        match read().unwrap() {
            Event::Key(KeyEvent {
                code: KeyCode::Char('q'),
                modifiers: KeyModifiers::CONTROL,
                ..
            }) => break,
            Event::Key(KeyEvent {
                code: KeyCode::Char('c'),
                modifiers: KeyModifiers::CONTROL,
                ..
            }) => break,
            _ => (),
        }
    }

    screen.exit();
}
