use crate::editor::Editor;
use crate::terminal::{Coords, Screen};
use colored::Colorize;
use crossterm::event::{read, Event, KeyCode, KeyEvent, KeyModifiers};

pub fn draw_status(screen: &mut Screen, editor: &Editor) {
    // Calculate where to draw the status bar
    let status_height = screen.size.height - 2;

    // Get the editor logo from the config
    let editor_logo = &format!(" {} ", editor.config.logo) as &str;
    // Write the editor logo
    screen.write_at(
        editor_logo.bright_yellow().bold().reversed().to_string(),
        Coords::from(0, status_height),
    );

    // Get the current mode into a string
    let mode_string = &format!(" {} ", editor.mode.as_str()) as &str;
    // Calculate where to write the current mode
    let x = editor_logo.len() - 1;
    // Write the current mode
    screen.write_at(
        mode_string.green().bold().reversed().to_string(),
        Coords::from(x, status_height),
    );

    // Get the current open file name
    let file_name = &format!(" {} ", editor.buffer.name) as &str;
    // Calculate where to write the file name
    let x = editor_logo.len() + mode_string.len() - 1;
    // Write the current file name
    screen.write_at(
        file_name.magenta().bold().reversed().to_string(),
        Coords::from(x, status_height),
    );
}

pub fn start(screen: &mut Screen, editor: Editor) {
    loop {
        // Draw the status bar
        draw_status(screen, &editor);

        // Check for any key presses
        match read().unwrap() {
            Event::Key(KeyEvent {
                code: KeyCode::Char('q'),
                modifiers: KeyModifiers::CONTROL,
                ..
            }) => break,
            _ => (),
        }
    }

    screen.exit();
}
