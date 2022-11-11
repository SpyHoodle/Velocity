use crate::core::buffer::Buffer;

pub struct Config<'a> {
    pub logo: &'a str,
    pub friendly_name: &'a str,
}

impl<'a> Config<'a> {
    pub fn new() -> Self {
        Self {
            logo: "λ",
            friendly_name: "Lambda",
        }
    }
}

#[allow(dead_code)]
pub enum Mode {
    Normal,
    Insert,
    Select,
    Command,
}

impl Mode {
    pub fn as_str(&self) -> &str {
        match self {
            Mode::Normal => "NORMAL",
            Mode::Insert => "INSERT",
            Mode::Select => "SELECT",
            Mode::Command => "COMMAND",
        }
    }
}

pub struct Editor<'a> {
    pub config: Config<'a>,
    pub buffer: Box<Buffer<'a>>,
    pub cursors: Vec<i32>,
    pub mode: Mode,
}

impl<'a> Editor<'a> {
    pub fn new(file_path: &'a str) -> Self {
        Editor {
            config: Config::new(),
            buffer: Box::new(Buffer::new(file_path)),
            cursors: Vec::from([0]),
            mode: Mode::Normal,
        }
    }
}
