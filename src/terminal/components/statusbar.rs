use crossterm::style::Stylize;
use crate::core::editor::Editor;
use crate::terminal::screen::{Coords, Screen};
use crate::terminal::utils;

pub fn draw(screen: &mut Screen, editor: &Editor) -> Result<(), ()> {
    // Calculate where to draw the status bar
    let status_height = screen.size.height - 2;

    // Get the editor logo from the config
    let editor_logo = &utils::with_spaces(editor.config.logo) as &str;
    // Get the current mode into a string
    let mode_string = &utils::with_spaces(editor.mode.as_str()) as &str;
    // Get the current open file name
    let file_name = &utils::with_spaces(editor.buffer.name) as &str;

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