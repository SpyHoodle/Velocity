use std::path::PathBuf;
use crate::core::buffer::Buffer;
use crate::core::buffer::BufferKind;

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
    pub fn new(path: PathBuf, buffer_name: &'a str) -> Self {
        let buffer_kind = if path.to_str().unwrap().len() > 1 { BufferKind::Write } else { BufferKind::Scratch };
        Editor {
            config: Config::new(),
            buffer: Box::new(Buffer::new(path, buffer_name, buffer_kind)),
            cursors: Vec::from([0]),
            mode: Mode::Normal,
        }
    }
}
