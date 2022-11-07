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
    let x = x + mode_string.len();
    // Write the current file name
    screen.write_at(
        file_name.magenta().bold().reversed().to_string(),
        Coords::from(x, status_height),
    );

    // Draw the rest of the status bar
    let x = x + file_name.len();
    screen.write_at(
        " ".repeat(screen.size.width - x).reversed().to_string(),
        Coords::from(x, status_height),
    );
}

pub fn draw_welcome(screen: &mut Screen, editor: &Editor) {
    // The welcome message
    let message: [&str; 6] = [
        &"λ Lambda".yellow() as &str,
        "Hackable text editor for nerds",
        "",
        "Type :help to open the README.md document",
        "Type :o <file> to open a file and edit",
        "Type :q! or <C-c> to quit lambda",
    ];

    // The starting y position in the centre of the screen
    let mut y = (screen.size.height / 2) - (message.len() / 2) - 2;

    for line in message {
        // Each line has different width so requires a different x position to center it
        let x = (screen.size.width / 2) - (line.len() / 2);

        // For each line we move downwards so increment y
        y += 1;

        // Write the line to the screen at position (x, y)
        screen.write_at(line.to_string(), Coords::from(x, y));
    }
}

pub fn start(screen: &mut Screen, editor: Editor) {
    loop {
        // Draw the welcome message
        draw_welcome(screen, &editor);

        // Draw the status bar
        draw_status(screen, &editor);

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
