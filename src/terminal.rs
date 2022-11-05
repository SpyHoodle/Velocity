use crossterm::terminal;
use crossterm::{execute, ErrorKind};
use crossterm::style::Print;
use crossterm::cursor::{CursorShape, MoveTo};
use std::io::{stdout, Write};

pub struct Size {
    pub width: usize,
    pub height: usize,
}

pub struct Coords {
    pub x: usize,
    pub y: usize,
}

impl Coords {
    pub fn from(x: usize, y: usize) -> Self {
        Self {
            x: 0,
            y: 0,
        }
    }
}

pub struct Cursor {
    pub position: Coords,
    pub shape: CursorShape,
}

impl Cursor {
    pub fn new() -> Result<Self, ErrorKind> {
        let cursor = Self {
            position: Coords::from(0, 0),
            shape: CursorShape::Block,
        };
        Cursor::move_to(&mut cursor, 0, 0);
        Ok(cursor)
    }

    pub fn move_to(&mut self, x: u16, y: u16) {
        self.position = Coords::from(x as usize, y as usize);
        execute!(stdout(), MoveTo(x, y)).unwrap()
    }
}

pub struct Terminal {
    pub size: Size,
    pub cursor: Cursor,
}

impl Terminal {
    pub fn new() -> Result<Self, ErrorKind> {
        let size = terminal::size()?;
        Terminal::clear();
        Terminal::enter();
        Ok(Self {
            size: Size {
                width: size.0 as usize,
                height: size.1 as usize,
            },
            cursor: Cursor::new().unwrap(),
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

    pub fn write(text: String) {
        // Writes a line to a current cursor position
        execute!(stdout(), Print(text)).unwrap();
    }

    pub fn clear() {
        // Clears the terminal screen
        execute!(stdout(), terminal::Clear(terminal::ClearType::All)).unwrap();
    }
}
