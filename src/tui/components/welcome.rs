use crossterm::style::Stylize;
use crate::core::editor::Editor;
use crate::terminal::screen::{Coords, Screen};
use crate::tui::utils;

pub fn draw(screen: &mut Screen, editor: &Editor) {
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
    if screen.size.width > utils::longest_element_in_vec(message.to_vec()) && screen.size.height > message.len() + 4 {
        // The starting y position in the centre of the screen
        let mut y = (screen.size.height / 2) - (message.len() / 2) - 2;

        // Calculate where to place the title
        let x = utils::calc_centred_x(screen.size.width, title.len());

        // Write the title to the screen
        screen.write_at(title.yellow().to_string(), Coords::from(x, y));

        for line in message {
            // Each line has different width so requires a different x position to center it
            let x = utils::calc_centred_x(screen.size.width, line.len()) ;

            // For each line we move downwards so increment y
            y += 1;

            // Write the line to the screen at position (x, y)
            screen.write_at(line.to_string(), Coords::from(x, y));
        }
    }
}
