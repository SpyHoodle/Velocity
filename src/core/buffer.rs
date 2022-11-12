use std::path::PathBuf;

pub struct Buffer<'a> {
    pub data: Vec<String>,
    pub path: PathBuf,
    pub name: &'a str,
}

impl<'a> Buffer<'a> {
    pub fn new(dir_path: PathBuf, file_name: &'a str) -> Self {
        let name = if file_name.len() > 0 {
            file_name
        } else {
            "[No Name]"
        };

        Self {
            data: vec![String::from("")],
            path: dir_path,
            name,
        }
    }
}
