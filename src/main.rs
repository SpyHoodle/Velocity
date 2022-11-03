struct Buffer {
    data: Vec<String>,
    name: &str,
}

struct Editor {
    buffer: Buffer,
}

fn main() {
    let bufffer = Buffer {
        data: Vec::from([String::from("a test")]),
        name: "uhh"
    };

    let editor = Editor {
        buffer: bufffer,
    };

    println!("{}", editor.buffer.data[0])
}
