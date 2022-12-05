use std::path::PathBuf;

#[derive(PartialEq)]
pub enum BufferKind {
    Scratch,
    Write,
    Read,
}

impl BufferKind {
    pub fn as_str(&self) -> &str {
        match self {
            BufferKind::Scratch => "*scratch*",
            BufferKind::Write => "write",
            BufferKind::Read => "read",
        }
    }
}

pub struct Buffer<'a> {
    pub data: Vec<String>,
    pub path: PathBuf,
    pub kind: BufferKind,
    pub name: &'a str,
}

impl<'a> Buffer<'a> {
    pub fn new(path: PathBuf, name: &'a str, kind: BufferKind) -> Self {
        // Return a buffer
        Self {
            data: vec![String::from("")],
            path,
            kind,
            name,
        }
    }
}
