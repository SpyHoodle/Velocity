enum Mode {
    Normal,
    Insert,
    Select
}

pub struct Buffer<'a> {
    pub data: Vec<String>,
    pub name: &'a str,
    pub path: &'a str,
}

pub struct Editor<'a> {
    pub buffer: Buffer<'a>,
    pub cursor: [i32; 2],
    mode: Mode,
}

impl<'a> Editor<'a> {
    pub fn new() -> Self {
        Editor {
            buffer: Buffer {
                data: Vec::from([String::from("Hello"), String::from("World")]),
                name: "[No Name]",
                path: "/home/spy",
            },
            cursor: [0, 0],
            mode: Mode::Normal,
        }
    }
}
