enum Mode {
    Normal,
    Insert,
    Select
}

struct Buffer<'a> {
    data: Vec<String>,
    name: &'a str,
    path: &'a str,
}

struct Editor<'a> {
    buffer: Buffer<'a>,
    cursor: [i32; 2],
    mode: Mode,
}

fn main() {
    let bufffer = Buffer {
        data: Vec::from([String::from("Hello"), String::from("World")]),
        name: "[No Name]",
        path: "/home/spy",
    };

    let editor = Editor {
        buffer: bufffer,
        cursor: [0, 0],
        mode: Mode::Normal,
    };

    println!("{}", editor.buffer.data[0])
}
