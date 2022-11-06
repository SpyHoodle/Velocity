use crossterm::cursor::{Hide, MoveTo, Show};
use crossterm::style::Print;
use crossterm::terminal;
use crossterm::{execute, ErrorKind};
use std::io::stdout;

// Struct for holding coordinates
#[derive(Copy, Clone)]
pub struct Coords {
    pub x: usize,
    pub y: usize,
}

// Creating a coordinates from two values
impl Coords {
    pub fn from(x: usize, y: usize) -> Self {
        Self { x, y }
    }
}

// A cursor for writing to the terminal screen
#[derive(Copy, Clone)]
pub struct Cursor {
    pub position: Coords,
    pub hidden: bool,
}

// When a cursor is created
impl Cursor {
    pub fn new() -> Result<Self, ErrorKind> {
        let mut cursor = Self {
            position: Coords::from(0, 0),
            hidden: true,
        };
        Cursor::move_to(&mut cursor, Coords::from(0, 0));
        Cursor::hide(&mut cursor);
        Ok(cursor)
    }
}

// Cursor methods
impl Cursor {
    pub fn move_to(&mut self, position: Coords) {
        // Set the new position of the cursor
        self.position = position;

        // Move the cursor to the desired posiition in the terminal
        execute!(stdout(), MoveTo(position.x as u16, position.y as u16)).unwrap();
    }

    pub fn hide(&mut self) {
        // Remember that the cursor is hidden
        self.hidden = true;

        // Hide the cursor from the terminal screen
        execute!(stdout(), Hide).unwrap();
    }

    pub fn show(&mut self) {
        // Remember that the cursor isn't hidden
        self.hidden = false;

        // Show the cursor to the terminal screen
        execute!(stdout(), Show).unwrap();
    }
}

// A struct for holding the size of the terminal
pub struct Size {
    pub width: usize,
    pub height: usize,
}

// The terminal screen
pub struct Screen {
    pub size: Size,
    pub cursor: Cursor,
}

// For when a new terminal screen is created
impl Screen {
    pub fn new() -> Result<Self, ErrorKind> {
        // Get the size of the terminal
        let size = terminal::size()?;

        // Define a new terminal screen struct
        let mut screen = Self {
            size: Size {
                width: size.0 as usize,
                height: size.1 as usize,
            },
            cursor: Cursor::new().unwrap(),
        };

        // Empty the terminal screen
        Screen::clear();

        // Enter the terminal screen
        screen.enter();

        // Return a result containing the terminal
        Ok(screen)
    }
}

// Terminal functions and methods for managing the terminal
impl Screen {
    pub fn enter(&mut self) {
        // Hide the cursor
        self.cursor.hide();

        // Enter the terminal screen
        terminal::enable_raw_mode().unwrap();
        execute!(stdout(), terminal::EnterAlternateScreen).unwrap();
    }

    pub fn exit(&mut self) {
        // Show the cursor
        self.cursor.show();

        // Exit the terminal screen
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

    pub fn write_at(&mut self, text: String, position: Coords) {
        // Writes a line at a set of coordinates
        self.cursor.move_to(position);
        Screen::write(text);
    }
}
