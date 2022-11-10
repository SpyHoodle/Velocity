use crate::tui::utils;
use crate::tui::ui::Component;
use crate::core::editor::Editor;
use crate::terminal::screen::{Coords, Screen};
use crossterm::style::Stylize;

pub struct WelcomeMessage<'a> {
    title: String,
    message: [&'a str; 5],
}

impl<'a> WelcomeMessage<'a> {
    pub fn new(editor: &'a Editor<'a>) -> Self {
        let title = format!("{} {}", editor.config.logo, editor.config.friendly_name);

        // The welcome message
        let message: [&str; 5] = [
            "Hackable text editor for nerds",
            "",
            "Type :help to open the README.md document",
            "Type :o <file> to open a file and edit",
            "Type :q! or <C-c> to quit lambda",
        ];
        Self {
            title,
            message,
        }
    }
}

impl<'a> Component for WelcomeMessage<'a> {
    fn draw(&self, screen: &mut Screen, _editor: &Editor) -> Result<(), ()> {
        // If the screen is big enough, we can draw
        if screen.size.width > utils::longest_element_in_vec(self.message.to_vec()) && screen.size.height > self.message.len() + 4 {
            // The starting y position in the centre of the screen
            let mut y = (screen.size.height / 2) - (self.message.len() / 2) - 2;

            // Calculate where to place the title
            let x = utils::calc_centered_x(screen.size.width, self.title.len());

            // Write the title to the screen
            screen.write_at(&self.title.clone().yellow().to_string(), Coords::from(x, y));

            for line in &self.message {
                // Each line has different width so requires a different x position to center it
                let x = utils::calc_centered_x(screen.size.width, line.len()) ;

                // For each line we move downwards so increment y
                y += 1;

                // Write the line to the screen at position (x, y)
                screen.write_at(&line.to_string(), Coords::from(x, y));
            };

            Ok(())

        } else {
            Err(())
        }
    }
}
