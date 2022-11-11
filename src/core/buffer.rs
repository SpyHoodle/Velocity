use std::path::Path;
use std::env;

pub struct Buffer<'a> {
    pub data: Vec<String>,
    pub name: &'a str,
    pub path: &'a Path,
}

impl<'a> Buffer<'a> {
    pub fn new(file_path: &'a str) -> Self {
        let name = if file_path.len() > 0 {
            Path::new(file_path).file_name().unwrap().to_str().unwrap()
        } else {
            "[No Name]"
        };

        let path = if file_path.len() > 1 { 
            Path::new(file_path)
        } else {
            env::current_dir().unwrap().parent().unwrap().to_str()
        };
        
        Self {
            data: vec![String::from("")],
            name,
            path,
        }
    }
}