use crossterm::terminal;
use crossterm::{execute, ErrorKind};
use std::io::{stdout, Write};

#[derive(Debug)]
pub struct Size {
    pub width: usize,
    pub height: usize,
}

#[derive(Debug)]
pub struct Terminal {
    pub size: Size,
}

impl Terminal {
    pub fn new() -> Result<Self, ErrorKind> {
        let size = terminal::size()?;
        Terminal::enter();
        Ok(Self {
            size: Size {
                width: size.0 as usize,
                height: size.1 as usize,
            },
        })
    }

    pub fn enter() {
        // Enter the current terminal
        terminal::enable_raw_mode().unwrap();
        execute!(stdout(), terminal::EnterAlternateScreen).unwrap();
    }

    pub fn exit() {
        // Exit the current terminal
        execute!(stdout(), terminal::LeaveAlternateScreen).unwrap();
        terminal::disable_raw_mode().unwrap();
    }
}
