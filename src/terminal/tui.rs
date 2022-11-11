use crate::core::editor::Editor;
use crate::terminal::screen::{Coords, Screen};
use crossterm::style::Stylize;
use crossterm::event::{read, Event, KeyCode, KeyEvent, KeyModifiers};

// Utils
fn with_spaces(text: &str) -> String {
    format!(" {} ", text)
}
fn calc_x(screen_width: usize, item_length: usize) -> usize {
    (screen_width / 2) - (item_length / 2)
}
fn longest_element_in_array(elements: Vec<&str>) -> usize {
    elements.iter().max_by_key(|x: &&&str| x.len()).unwrap().len()
}

pub fn draw_status(screen: &mut Screen, editor: &Editor) -> Result<(), ()> {
    // Calculate where to draw the status bar
    let status_height = screen.size.height - 2;

    // Get the editor logo from the config
    let editor_logo = &with_spaces(editor.config.logo) as &str;
    // Get the current mode into a string
    let mode_string = &with_spaces(editor.mode.as_str()) as &str;
    // Get the current open file name
    let file_name = &with_spaces(editor.buffer.name) as &str;

    // Calculate the total length of all the status bar components
    let total_length = editor_logo.len() + mode_string.len() + file_name.len() + 1;

    // If the screen isn't wide enough, panic as we can't draw the status bar
    if screen.size.width < total_length {
        Err(())

    } else {
        // Write the editor logo
        screen.write_at(
            editor_logo.yellow().bold().reverse().to_string(),
            Coords::from(0, status_height),
        );

        // Calculate where to write the current mode
        let x = editor_logo.len() - 1;
        // Write the current mode
        screen.write_at(
            mode_string.green().bold().reverse().to_string(),
            Coords::from(x, status_height),
        );
        // Calculate where to write the file name
        let x = x + mode_string.len();
        // Write the current file name
        screen.write_at(
            file_name.magenta().bold().reverse().to_string(),
            Coords::from(x, status_height),
        );

        // Draw the rest of the status bar
        let x = x + file_name.len();
        screen.write_at(
            " ".repeat(screen.size.width - x).reverse().to_string(),
            Coords::from(x, status_height),
        );

        Ok(())
    }
}

pub fn draw_welcome(screen: &mut Screen, editor: &Editor) {
    // The welcome message
    let title = format!("{} {}", editor.config.logo, editor.config.friendly_name);
    let message: [&str; 5] = [
        "Hackable text editor for nerds",
        "",
        "Type :help to open the README.md document",
        "Type :o <file> to open a file and edit",
        "Type :q! or <C-c> to quit lambda",
    ];

    // If the screen is big enough, we can draw
    if screen.size.width > longest_element_in_array(message.to_vec()) && screen.size.height > message.len() + 4 {
        // The starting y position in the centre of the screen
        let mut y = (screen.size.height / 2) - (message.len() / 2) - 2;

        // Calculate where to place the title
        let x = calc_x(screen.size.width, title.len());

        // Write the title to the screen
        screen.write_at(title.yellow().to_string(), Coords::from(x, y));

        for line in message {
            // Each line has different width so requires a different x position to center it
            let x = calc_x(screen.size.width, line.len()) ;

            // For each line we move downwards so increment y
            y += 1;

            // Write the line to the screen at position (x, y)
            screen.write_at(line.to_string(), Coords::from(x, y));
        }
    }
}

pub fn start(screen: &mut Screen, editor: Editor) {
    loop {
        // Refresh the screen
        screen.refresh().unwrap();

        // Draw the welcome message
        draw_welcome(screen, &editor);

        // Draw the status bar
        draw_status(screen, &editor).unwrap();

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
