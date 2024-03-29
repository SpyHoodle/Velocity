use crossterm::style::Stylize;
use crate::core::editor::Editor;
use crate::terminal::screen::{Coords, Screen};
use crate::tui::utils;

pub fn draw(screen: &mut Screen, editor: &Editor) -> Result<(), ()> {
    // Calculate where to draw the status bar
    let status_height = screen.size.height - 2;

    // Get the editor logo from the config
    let editor_logo = &utils::with_spaces(editor.config.logo) as &str;
    // Get the current mode into a string
    let mode_string = &utils::with_spaces(editor.mode.as_str()) as &str;
    // Get the current open file name
    let file_name = &utils::with_spaces(editor.buffer.name) as &str;
    // Get the current buffer kind
    let buffer_kind = &utils::with_spaces(editor.buffer.kind.as_str()) as &str;

    // Calculate the total length of all the status bar components
    let total_length = editor_logo.len() + mode_string.len() + file_name.len() + buffer_kind.len() + 1;

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

        let x = x + mode_string.len();
        // Draws the file name if it has a length, if not then it will draw the buffer type
        if editor.buffer.name.len() > 0 {
            screen.write_at(
                file_name.magenta().bold().reverse().to_string(),
                Coords::from(x, status_height),
            );
        } else {
            screen.write_at(
                buffer_kind.blue().bold().reverse().to_string(),
                Coords::from(x, status_height),
            );
        }

        let x = if editor.buffer.name.len() > 0 { x + file_name.len() } else { x + buffer_kind.len() };
        screen.write_at(
            " ".repeat(screen.size.width - x).reverse().to_string(),
            Coords::from(x, status_height),
        );

        Ok(())
    }
}
